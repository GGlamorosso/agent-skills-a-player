# Agent Skills A-Player

Quatre skills autonomes pour Codex, Claude Code et tout agent capable de lire un `SKILL.md` : carrousels produit, copywriting de vente, design orienté conversion et raisonnement stratégique rigoureux.

Chaque skill est prêt à installer, déclenchable automatiquement par sa description et utilisable explicitement avec `$nom-du-skill`. Le dépôt ne dépend d'aucun second brain privé et ne contient aucun secret.

## Skills inclus

| Skill | Rôle | Déclencheurs typiques |
| --- | --- | --- |
| [`pixel`](skills/pixel/) | Construit 7 master prompts photoréalistes pour un carrousel PDP qui vend | « carrousel produit », « prompts d'images », « packshots », « images PDP » |
| [`copywriting-a-player`](skills/copywriting-a-player/) | Recherche l'avatar puis écrit ou réécrit le copy complet | « écris ma landing », « améliore cette offre », « cette page ne vend pas » |
| [`conversion-copy-design`](skills/conversion-copy-design/) | Conçoit ou audite des pages et sections claires, crédibles et anti-slop IA | « redesign la page », « refais le hero », « améliore la conversion » |
| [`ontological-reasoning`](skills/ontological-reasoning/) | Reconstruit une réponse stratégique ou causale au lieu de résumer des experts | « pourquoi ? », « que décider ? », « diagnostique », « compare ces modèles » |

## Installation rapide

```bash
git clone https://github.com/GGlamorosso/agent-skills-a-player.git
cd agent-skills-a-player
```

Installer les quatre skills globalement dans Codex :

```bash
./scripts/install.sh --target codex --scope global
```

Installer les quatre skills globalement dans Claude Code :

```bash
./scripts/install.sh --target claude --scope global
```

Installer un seul skill dans le projet courant :

```bash
./scripts/install.sh --target codex --scope project --skill pixel
./scripts/install.sh --target claude --scope project --skill copywriting-a-player
```

L'installateur ne remplace jamais silencieusement un skill existant. Ajoute `--force` pour déplacer l'ancienne version vers une sauvegarde horodatée avant l'installation.

### Installation manuelle

| Agent | Global | Projet |
| --- | --- | --- |
| Codex | `~/.codex/skills/<skill>/` | `.agents/skills/<skill>/` |
| Claude Code | `~/.claude/skills/<skill>/` | `.claude/skills/<skill>/` |

Copie simplement le dossier voulu depuis `skills/` vers la destination correspondante.

### Installation par un agent

Tu peux donner cette instruction à un agent ayant accès au terminal :

> Installe le skill `pixel` depuis `https://github.com/GGlamorosso/agent-skills-a-player` dans mes skills de projet, puis valide son `SKILL.md` sans modifier les autres skills.

## Utilisation

Les descriptions frontmatter permettent le déclenchement automatique. Pour forcer un skill :

```text
Utilise $pixel pour préparer le carrousel de ce produit à partir de ces photos et de cette fiche technique.
Utilise $copywriting-a-player pour réécrire cette landing page après une vraie recherche avatar.
Utilise $conversion-copy-design pour refaire ce hero sans slop IA et avec un copy orienté conversion.
Utilise $ontological-reasoning pour décider si cette niche reste défendable à 24 mois.
```

## Prérequis et comportement

- `copywriting-a-player` : accès web recommandé pour recueillir le langage réel du marché. Sans web, l'agent doit construire le brief avec l'utilisateur et signaler la limite.
- `conversion-copy-design` : fonctionne en conseil, audit ou production HTML/CSS/Liquid. Ses références incluent des patterns de sections prêts à adapter.
- `pixel` : produit d'abord les prompts. La génération d'images ne démarre que sur demande explicite. `scripts/overlay_text.py` nécessite Pillow ; `scripts/gen_carousel.py` nécessite le CLI Codex et un outil d'image disponible.
- `ontological-reasoning` : fonctionne avec n'importe quel corpus. Il sépare faits, sources, hypothèses, inférences et inconnus, puis teste un modèle rival et un falsificateur.

## Structure

```text
agent-skills-a-player/
├── catalog.json
├── skills/
│   ├── pixel/
│   ├── copywriting-a-player/
│   ├── conversion-copy-design/
│   └── ontological-reasoning/
└── scripts/
    └── install.sh
```

Chaque dossier de skill reste volontairement minimal : `SKILL.md`, `agents/openai.yaml`, puis uniquement les `references/` ou `scripts/` nécessaires à son exécution.

## Principes de qualité

- Aucune preuve, statistique, urgence, garantie ou caractéristique inventée.
- Recherche et diagnostic avant production.
- Sorties complètes et directement exploitables, pas seulement des outlines.
- Références chargées à la demande pour préserver le contexte de l'agent.
- Scripts optionnels exécutés avec des permissions limitées au workspace.

## Licence

MIT — voir [`LICENSE`](LICENSE).
