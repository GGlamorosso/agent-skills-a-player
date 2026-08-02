#!/usr/bin/env python3
"""Driver carrousel produit : génère les images via `codex exec`, séquentiellement,
avec back-off exponentiel et récupération depuis le cache codex. Résumable.

Usage:
    python3 gen_carousel.py <carousel.json> [--dry-run]

Le config est relatif à son propre dossier (ref, out_dir). Toute image déjà
présente (> 50 Ko) est skippée : safe à relancer après un crash ou un throttle.

Format carousel.json :
{
  "slug": "juicer",
  "ref": "images-source/src-juicer.jpg",
  "out_dir": "carousel",
  "aspect": "square 1:1",                  # défaut global, surchargable par image
  "style": "<bloc de style DA commun>",    # collé dans chaque prompt non-packshot
  "images": [
    {"n": 1, "name": "packshot", "scene": "...", "use_ref": true, "aspect": "..."}
  ]
}
"""
import json
import glob
import os
import shutil
import subprocess
import sys
import time

PACKSHOT_STYLE = """Style: clean studio packshot on a PURE WHITE seamless background, product isolated, with a clearly visible soft contact shadow on the ground. Realistic product photography, NOT a 3D render. No text, no badges, no watermarks.

CRITICAL - product fidelity: reproduce the product EXACTLY as in the reference image: same shape, same colours, same proportions, same manufacturer wordmark visible and unaltered."""

FIDELITY = """CRITICAL - product fidelity: reproduce the product EXACTLY as in the reference image: same shape, same colours, same proportions, same control layout, and its own manufacturer wordmark visible and unaltered. Do not redesign it, do not restyle it, do not remove or replace the brand marking. Never add any text overlay, badge, watermark, spec number or added logo."""


def newest_codex_png(since):
    best, best_t = None, since
    for p in glob.glob(os.path.expanduser("~/.codex/generated_images/*/*.png")):
        t = os.path.getmtime(p)
        if t > best_t:
            best, best_t = p, t
    return best


def build_prompt(cfg, img, target_rel):
    # Mode master prompt : le prompt complet vient du skill (pixel), le driver
    # n'ajoute que la consigne d'écriture du fichier.
    if "prompt" in img:
        return "\n".join([
            "Use your image_gen tool to generate ONE image.", "",
            img["prompt"], "",
            f"Save the result to: {target_rel}",
            "Report the final file path when done."])
    is_packshot = img.get("name") == "packshot" or img.get("n") == 1
    use_ref = img.get("use_ref", True)
    aspect = img.get("aspect", cfg.get("aspect", "square 1:1"))
    parts = ["Use your image_gen tool to generate ONE image.", ""]
    if use_ref:
        parts += [
            f"Reference image (MUST be used as the visual reference input): {cfg['ref']}",
            "Reproduce THE SAME product exactly as in that reference. Do not redesign it, do not remove or change its brand marking.",
            "",
        ]
    parts += [f"Scene: {img['scene']}", ""]
    parts += [f"Aspect ratio: {aspect}. Generate natively at this aspect ratio - do NOT pad, stretch or letterbox a different canvas to reach it.", ""]
    if is_packshot:
        parts += [PACKSHOT_STYLE]
    else:
        parts += [cfg["style"], "", FIDELITY]
    parts += ["", f"Save the result to: {target_rel}", "Report the final file path when done."]
    return "\n".join(parts)


def target_path(root, cfg, img):
    return os.path.join(cfg["out_dir"], f"{cfg['slug']}-{img['n']:02d}-{img['name']}.png")


def done(root, rel):
    p = os.path.join(root, rel)
    return os.path.exists(p) and os.path.getsize(p) > 50000


def run_one(root, cfg, img):
    rel = target_path(root, cfg, img)
    if done(root, rel):
        print(f"SKIP  {rel} (exists)", flush=True)
        return True
    prompt = build_prompt(cfg, img, rel)
    print(f"GEN   {rel} ...", flush=True)
    t0 = time.time()
    try:
        subprocess.run(
            ["codex", "exec", "--skip-git-repo-check", "--sandbox", "workspace-write",
             "-C", root, prompt],
            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            timeout=900, cwd=root)
    except subprocess.TimeoutExpired:
        print(f"      timeout après {int(time.time() - t0)}s - vérification du fichier quand même", flush=True)
    if done(root, rel):
        print(f"OK    {rel} ({int(time.time() - t0)}s)", flush=True)
        return True
    cand = newest_codex_png(t0)
    if cand:
        shutil.copy(cand, os.path.join(root, rel))
        print(f"OK    {rel} (récupéré du cache codex, {int(time.time() - t0)}s)", flush=True)
        return True
    print(f"FAIL  {rel} ({int(time.time() - t0)}s)", flush=True)
    return False


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry = "--dry-run" in sys.argv
    if len(args) != 1:
        sys.exit(__doc__)
    cfg_path = os.path.abspath(args[0])
    root = os.path.dirname(cfg_path)
    with open(cfg_path) as f:
        cfg = json.load(f)
    if cfg.get("ref") and not os.path.exists(os.path.join(root, cfg["ref"])):
        sys.exit(f"ERREUR: image source introuvable: {cfg['ref']} (relative à {root})")
    os.makedirs(os.path.join(root, cfg["out_dir"]), exist_ok=True)

    if dry:
        for img in cfg["images"]:
            rel = target_path(root, cfg, img)
            print(f"=== {rel} ===")
            print(build_prompt(cfg, img, rel))
            print()
        return

    # Boucle patiente : le générateur d'images throttle après ~12 rendus (les
    # appels image pendent 9+ min). Un seul flux séquentiel, back-off croissant.
    backoff = 120
    MAX_BACKOFF = 1800
    while True:
        todo = [i for i in cfg["images"] if not done(root, target_path(root, cfg, i))]
        if not todo:
            print("ALL DONE", flush=True)
            return
        print(f"--- passe : {len(todo)} image(s) restante(s) ---", flush=True)
        progress = False
        for img in todo:
            if run_one(root, cfg, img):
                progress = True
                backoff = 120
                time.sleep(10)
            else:
                print(f"      throttle probable - pause {backoff}s", flush=True)
                time.sleep(backoff)
                backoff = min(backoff * 2, MAX_BACKOFF)
        if not progress:
            print(f"      aucune progression sur la passe - pause {backoff}s", flush=True)
            time.sleep(backoff)
            backoff = min(backoff * 2, MAX_BACKOFF)


if __name__ == "__main__":
    main()
