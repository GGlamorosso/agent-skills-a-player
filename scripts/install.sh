#!/usr/bin/env bash
set -eu

target=""
scope="global"
selected_skill="all"
force="false"

usage() {
  printf '%s\n' \
    "Usage: ./scripts/install.sh --target codex|claude [--scope global|project]" \
    "       [--skill pixel|copywriting-a-player|conversion-copy-design|ontological-reasoning|all] [--force]"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target) target="${2:-}"; shift 2 ;;
    --scope) scope="${2:-}"; shift 2 ;;
    --skill) selected_skill="${2:-}"; shift 2 ;;
    --force) force="true"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) printf 'Argument inconnu: %s\n' "$1" >&2; usage >&2; exit 2 ;;
  esac
done

case "$target:$scope" in
  codex:global) destination="${CODEX_HOME:-$HOME/.codex}/skills" ;;
  codex:project) destination="$(pwd)/.agents/skills" ;;
  claude:global) destination="$HOME/.claude/skills" ;;
  claude:project) destination="$(pwd)/.claude/skills" ;;
  *) printf '%s\n' "Choisis --target codex|claude et --scope global|project." >&2; exit 2 ;;
esac

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
repo_root="$(CDPATH= cd -- "$script_dir/.." && pwd)"
skills_root="$repo_root/skills"
available_skills="pixel copywriting-a-player conversion-copy-design ontological-reasoning"

if [ "$selected_skill" = "all" ]; then
  install_list="$available_skills"
else
  case " $available_skills " in
    *" $selected_skill "*) install_list="$selected_skill" ;;
    *) printf 'Skill inconnu: %s\n' "$selected_skill" >&2; exit 2 ;;
  esac
fi

mkdir -p "$destination"

for skill_name in $install_list; do
  source_dir="$skills_root/$skill_name"
  target_dir="$destination/$skill_name"

  if [ -e "$target_dir" ]; then
    if [ "$force" = "true" ]; then
      timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
      backup_dir="$target_dir.backup-$timestamp"
      mv "$target_dir" "$backup_dir"
      printf 'Sauvegarde: %s\n' "$backup_dir"
    else
      printf 'Déjà présent, ignoré: %s (utilise --force pour remplacer)\n' "$target_dir"
      continue
    fi
  fi

  cp -R "$source_dir" "$target_dir"
  printf 'Installé: %s\n' "$target_dir"
done
