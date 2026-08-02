# Workflow Shopify — banque de sections obligatoire

Utiliser ce workflow dès que la sortie touche un thème Shopify : section Liquid, template JSON,
landing page, PDP, home, collection ou modification visuelle d'un composant. Le but est de relier
le diagnostic conversion à des composants existants, testés et adressables — pas de générer une
nouvelle section plausible à chaque demande.

## 1. Résoudre le kit

Chercher dans cet ordre :

1. le chemin fourni par le projet ou l'utilisateur ;
2. la variable `SHOPIFY_SECTION_KIT` si elle existe ;
3. `~/dev/shopify-section-kit` ;
4. un dossier frère `shopify-section-kit/` ;
5. le dépôt public `https://github.com/GGlamorosso/shopify-section-kit`.

Pour coder, disposer d'une copie locale à jour. Si elle manque, proposer ou effectuer dans le
périmètre autorisé un clone du dépôt public. Pour un audit sans écriture, l'API GitHub ou `gh`
peut suffire.

Définir ensuite un chemin explicite, sans deviner :

```bash
KIT_ROOT=/chemin/absolu/vers/shopify-section-kit
```

Lire au minimum :

- `README.md` — architecture Structure / Message / Binding ;
- `docs/SECTION-CONTRACT.md` — contrat technique non négociable ;
- `docs/GOTCHAS.md` — pièges Shopify/Envy vérifiés ;
- `recipes/brand-platform.json` — archétypes et règle de fond ;
- `docs/MESSAGE-LAYER.md` si promo, preuve, garantie, livraison ou bénéfices sont concernés.

## 2. Définir le job avant de chercher

Transformer la demande en un job unique par section : preuve sociale, objection prix, bénéfice,
usage, comparaison, réassurance, offre, liaison visuelle, etc. Une demande à plusieurs jobs doit
devenir plusieurs sections. Écrire pour chaque job :

- intention de conversion ;
- avatar et objection visés ;
- preuve réelle disponible ;
- emplacement dans la séquence de page ;
- contenu transverse consommé depuis la couche Message.

Ne jamais chercher « une belle section ». Chercher le job, la preuve et le mécanisme.

## 3. Interroger la banque

Commencer large, puis filtrer avec au moins deux requêtes pertinentes :

```bash
python3 "$KIT_ROOT/tools/catalog.py" --list
python3 "$KIT_ROOT/tools/catalog.py" --find "<job ou mécanisme en français>"
python3 "$KIT_ROOT/tools/catalog.py" --categorie media
python3 "$KIT_ROOT/tools/catalog.py" --style sombre_premium
python3 "$KIT_ROOT/tools/catalog.py" --section ks-<famille>
```

Utiliser selon le besoin `--categorie`, `--style`, `--brand` et `--section`. Pour chaque candidat,
ouvrir sa fiche, sa capture/référence, sa section `sections/ks-*.liquid`, son registre dans
`variants/` et les recettes qui l'emploient. Vérifier le piège documenté, les `CONSUMES`, les
slots image, le ratio, la dette éventuelle et les sites où la variante est déjà déployée.

## 4. Produire la décision de banque avant de coder

Rendre ce bloc court dans le plan ou le compte rendu :

```text
BANK DECISION
Job :
Requêtes exécutées :
Candidats examinés :
Section/variante retenue :
Pourquoi elle correspond à l'avatar et à la preuve :
Adaptations autorisées : copy lié, images, ordre, tokens, réglages schema
Éléments interdits : preuves/specs inventées, couleurs/polices en dur, CSS dupliqué
```

L'absence de ce bloc signifie que la recherche n'est pas prouvée. Ne pas commencer le Liquid.

## 5. Réutiliser sans dégrader

- Copier ou instancier la famille/variante retenue ; ne pas réécrire sa structure de mémoire.
- Conserver un seul job, l'en-tête `ID / VARIANT / JOB / IMAGES / CONSUMES`, le schema et les presets.
- Utiliser `snippets/ks-tokens.liquid` et les assets mutualisés ; aucune couleur ou police en dur.
- Lier promo, note, nombre d'avis, garantie, livraison et bénéfices à la couche Message.
- Garder les images en `image_picker`, avec ratio et placeholder.
- Ne jamais coller du HTML/CSS/SVG récurrent dans `custom_liquid`.
- Adapter le copy à l'avatar et aux preuves disponibles ; masquer le bloc si la preuve manque.

Le kit fournit le squelette et le contrat. Le skill fournit l'angle, le message, l'ordre des
preuves et la cohérence avec le reste de la page.

## 6. Si aucun pattern ne convient

Ne pas improviser. Exécuter dans cet ordre :

1. lire `variants/<famille>/` et confirmer que la direction est réellement absente ;
2. inspecter les teardowns et sources déjà stockés dans le kit ;
3. étudier des références live dans la niche et au moins une catégorie hors niche ;
4. proposer trois directions transférables, dont une hors niche ;
5. obtenir l'arbitrage humain ;
6. construire avec `docs/SECTION-CONTRACT.md` et les outils du kit ;
7. enregistrer la nouvelle variante et sa provenance dans `variants/`.

Aucune nouvelle section ne doit être écrite avant l'étape 5. La nouveauté vient d'un transfert
documenté, pas d'une invention sans source.

## 7. Valider avant livraison ou push

```bash
python3 "$KIT_ROOT/tools/check.py" --theme /chemin/absolu/vers/theme --strict
```

Puis :

1. exécuter `shopify theme check` si disponible et séparer dette préexistante / régression créée ;
2. vérifier desktop et mobile sur une preview réelle ;
3. contrôler le contraste, la lisibilité, les états sans image/preuve et l'absence de débordement ;
4. vérifier que le copy transverse n'est pas dupliqué dans plusieurs templates ;
5. signaler explicitement tout contrôle impossible au lieu de déclarer le rendu validé.

## Interdictions

- Inventer une section parce que sa structure « semble logique ».
- Inventer avis, note, volume client, certification, délai, garantie, remise ou performance.
- Mélanger code et modifications admin dans une même tâche.
- Contourner une famille existante avec un blob `custom_liquid`.
- Présenter un contrôle statique comme une QA visuelle.
- Pousser avant que le contrat du kit soit vert.
