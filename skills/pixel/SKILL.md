---
name: pixel
description: >
  Produit les 7 MASTER PROMPTS photoréalistes du carrousel produit e-commerce — après avoir
  creusé l'avatar client comme un copywriter senior, lu la vraie fiche technique, extrait le
  style/les couleurs/la police/la langue du site, et choisi ce que le client doit VOIR pour
  acheter, image par image, dans le bon ordre. Utilise ce skill CHAQUE FOIS que l'utilisateur
  demande des prompts d'images produit, un carrousel photo, des visuels de fiche produit
  (PDP), des packshots, ou dit "génère les prompts", "master prompt", "images prod", "shoote
  le produit", "carrousel de [produit]" — même sans prononcer "prompt" ni "pixel". Livre des
  prompts prêts à coller dans n'importe quel générateur (Codex, etc.) ; ne lance PAS la
  génération sauf demande explicite. Impose : image 1 = packshot fond blanc pur sans texte,
  photoréalisme pro anti-slop IA, specs réelles uniquement, image source produit obligatoire.
---

# Pixel — Master prompts carrousel produit (7 images)

Ce skill ne génère pas d'images. Il produit le livrable en amont : **7 master prompts de
niveau photographe commercial**, construits sur une vraie recherche avatar, la vraie fiche
technique et l'identité réelle du site. La sortie est un fichier `prompts-<slug>.md` prêt à
coller dans n'importe quel générateur. La génération elle-même n'est lancée que si
l'utilisateur le demande explicitement (voir tout en bas).

Le but n'est pas "une belle image du produit". Le but est une séquence de 7 photos qui
**vendent** : chaque image répond à une question précise que l'avatar se pose, dans l'ordre
où il se la pose. Une image qui ne prouve rien est une image décorative — à refaire.

## Phase 0 — Collecte et analyse des références (bloquante, dans cet ordre)

Ne rien écrire tant que ces cinq entrées ne sont pas réunies. S'il en manque une, la
chercher dans le projet, puis la demander.

1. **Photos source produit** — collecter toutes les vraies photos fournisseur/fabricant
   disponibles, noter leur chemin précis et les REGARDER : packshot, dos, dessus, détails,
   accessoires et pièces. Chaque prompt cite au moins une référence visuelle obligatoire.
   Une slide qui montre une pièce, un détail ou un angle absent du packshot principal doit
   citer une photo additionnelle qui le montre réellement. Si elle n'existe pas, bloquer la
   génération de cette slide et demander la photo ; ne jamais extrapoler depuis un autre
   produit ou générer "de mémoire".
2. **Fiche technique réelle** — dimensions, puissance, matières, contenu du carton,
   features. Sources : script de build du projet, page produit, données fournisseur, admin.
   Toute spec affichée ou évoquée doit exister ici. Jamais de spec inventée ni arrondie.
3. **Identité du site** — `config/settings_data.json` (Shopify) ou CSS : couleur primaire,
   palette, police titres, police corps. La DA des images doit prolonger l'univers du site,
   pas le contredire.
4. **Langue du site** — tout texte prévu dans l'image (titres, bullets) est rédigé dans la
   langue du site (allemand pour un site .de, etc.), pas dans la langue de la conversation.
5. **Références visuelles fournies** — les analyser avant le plan : relever les mécanismes
   de preuve, l'alternance des cadrages, les hiérarchies et le rythme. Réutiliser les
   mécanismes pertinents, jamais la palette, les textes, badges, typographies, formes de
   marque ou compositions identitaires de la référence.

**Le texte est rendu PAR le modèle image, directement dans le visuel final.** Ce skill
produit des prompts destinés à des outils grand public (ChatGPT/GPT Image, Nano Banana,
etc.) où il n'y a pas de deuxième passe d'overlay derrière — le prompt doit donc décrire
noir sur blanc le texte exact à écrire dans l'image, sa taille, sa position et son style.
Un prompt qui interdit le texte et compte sur un post-traitement produira des images sans
aucun texte si personne ne fait tourner ce post-traitement — c'est visible et inutilisable
en carrousel. Voir Phase 3 pour le bloc TEXT obligatoire.

## Phase 1 — Avatar : creuser comme un copywriter senior

Si un skill de recherche persona/e-commerce est disponible, l'utiliser pour accélérer cette
phase. Sinon, mener directement la recherche terrain décrite ci-dessous. Si le persona est
déjà documenté dans le projet, reprendre le brief existant et vérifier qu'il est sourcé.
Il faut, avant d'écrire le moindre prompt, pouvoir répondre à ceci par écrit (5-10 lignes) :

- **Qui achète**, dans quelle situation de vie, et quel est le rêve concret derrière l'achat
  (pas "boire du jus" — "le petit-déjeuner calme avant que les enfants se lèvent").
- **Le doute n°1** qui empêche l'achat (trop compliqué à nettoyer ? trop gros ? gadget ?).
- **Les 2-3 objections secondaires** et leur vocabulaire exact (celui des avis concurrents).
- **Ce que le client doit VOIR de ses yeux pour croire** — pas lire : voir. Un doute sur le
  nettoyage se tue avec une photo de pièces démontées sous l'eau, pas avec un badge.
- **Le niveau d'awareness** du trafic (froid Google Ads = montrer le problème résolu, pas
  la marque).

Ce brief pilote tout : le choix des scènes, l'ordre des preuves, les textes overlay. Le
noter en tête du fichier livré, pour que l'utilisateur voie sur quoi reposent les choix.

## Phase 2 — Système adaptatif hybride premium + plan des 7 images

Adopter par défaut un **hybride premium adaptatif** : une seule identité de marque, mais
sept silhouettes de slides volontairement différentes. La cohérence ne signifie jamais
répéter sept fois « produit à droite + texte à gauche ».

### Analyser sans copier

Pour toute référence de carrousel fournie, produire d'abord une note courte : mécanismes
utilisés, type de plan, hiérarchie, nature de la preuve, alternance clair/sombre et rythme.
Traduire ensuite ces principes dans l'identité réelle du site et les preuves réelles du
produit. Ne reprendre ni couleurs, ni textes, ni badges, ni formes propriétaires. Lire
`references/hybrid-premium-mechanisms.md` au moment de construire le plan et choisir les
mécanismes selon l'avatar, le produit et les sources disponibles — jamais mécaniquement.

### Verrouiller les invariants

Répéter mot pour mot dans les 7 prompts les éléments qui font la famille visuelle :

- produit réel et traitement photographique fidèle ;
- palette de marque et couple typographique ;
- recette de lumière, température et douceur d'ombre ;
- texture ou matière de fond ;
- marges extérieures et densité graphique ;
- grain, contraste, rendu des matériaux et niveau de retouche.

Le fond reste un système studio continu clair, proche du blanc ou de la crème du site.
Une rupture sombre peut signaler une slide de confiance si elle reprend exactement la
même lumière, les mêmes marges et les mêmes codes. Éviter cuisine complète, fenêtre ou
décor envahissant ; une scène résultat peut être plus éditoriale, mais doit rester dans le
même langage de fond, de lumière et de traitement.

### Faire varier obligatoirement les silhouettes

Changer volontairement d'une slide à l'autre :

- échelle du produit (plein cadre, secondaire, macro, absent si le résultat suffit) ;
- angle caméra (frontal, trois-quarts, dessus, macro rasante) ;
- cadrage et répartition des masses ;
- structure graphique (plein cadre, panneau partagé, séquence, grille, callouts) ;
- mécanisme de preuve (résultat, chiffre, démonstration, comparaison, pièces, faits).

Ne jamais utiliser plus de deux fois dans le carrousel la composition « produit à droite +
texte à gauche ». Deux slides consécutives ne doivent partager ni le même type de plan ni
la même structure graphique.

### Conserver l'arc de vente, adapter le mécanisme

Images 1-4 : identification, projection, avantage dominant, compréhension d'usage.
Images 5-7 : objection principale, confiance, décision. L'ordre psychologique reste
stable ; le mécanisme visuel est choisi en fonction du produit :

| # | Slot | Question client | Familles de mécanismes possibles |
| --- | --- | --- | --- |
| 1 | `packshot` | « C'est quoi ? » | Packshot pur — **produit seul, fond blanc pur, ombre douce, aucun texte.** |
| 2 | `situation` | « Est-ce que je me vois vivre avec ? » | Scène résultat, geste ou résultat éditorial. |
| 3 | `feature` | « Qu'est-ce qui change vraiment ? » | Macro avec chiffre dominant, comparaison ou callout unique. |
| 4 | `action` | « Comment ça marche ? » | Séquence numérotée, geste en action ou vue du dessus. |
| 5 | `details` | « Mon doute n°1 est-il levé ? » | Pièces éclatées, détail annoté, comparaison oui/non. |
| 6 | `proof` | « Puis-je faire confiance ? » | Faits contractuels, preuve sociale réelle ou garanties réelles. |
| 7 | `closing` | « Est-ce le bon choix pour moi ? » | Guide idéal/pas pour, grille de faits ou contenu réel du carton. |

Présenter le plan dans un tableau contenant au minimum : n°, question client, bénéfice,
objection tuée, **mécanisme visuel**, **type de plan**, **preuve montrée**, scène et texte
exact. Ne pas confondre diversité et remplissage : chaque mécanisme doit répondre à une
question de l'avatar et reposer sur une preuve disponible.

### Test miniature obligatoire

Simuler les sept slides en vignettes, sans lire leur texte : chacune doit être identifiable
par sa silhouette, son échelle et sa structure. Les sept réunies doivent pourtant sembler
appartenir à la même marque grâce aux invariants. Si deux slides se confondent, changer le
plan ou le mécanisme ; si l'ensemble se disperse, corriger les invariants, pas uniformiser
les compositions.

**Règles d'honnêteté, non négociables** : aucun avis, note, témoignage, remise, origine
d'expédition, performance ou garantie inventé. Champ de preuve vide → preuve légale réelle
ou mécanisme de substitution honnête, jamais un chiffre plausible.

### Chaque image (sauf l'image 1) porte une grande phrase

Une image sans texte est une image qu'on regarde une seconde et qu'on oublie. Sauf le
packshot (règle absolue, zéro texte), **les 6 autres images portent chacune une grande
phrase** — un vrai titre, visuellement dominant, pas un sous-titre discret planqué en bas.
Cette phrase n'est jamais générique : elle applique la formule **bénéfice + objection**.

- **Le bénéfice** : ce que ça change concrètement pour le client, ressenti à la première
  personne, pas une caractéristique. "1,2 L" n'est pas un bénéfice ; "assez pour toute la
  famille en une pressée" en est un.
- **L'objection tuée** : à quel doute précis du brief avatar (Phase 1) cette image répond.
  Chaque grande phrase doit pouvoir se relier à une ligne du brief — si elle ne tue aucune
  objection et ne porte aucun bénéfice, ce n'est pas une grande phrase, c'est un slogan
  creux, à réécrire.

Formule courte : **[Bénéfice ressenti]. [Objection nommée et retournée].** — en une phrase
ou deux courtes, dans la langue du site, assez GRANDE et GRASSE pour se lire en un coup
d'œil en miniature (vignette carrousel) — c'est la plainte la plus fréquente d'un premier
jet raté : texte minuscule ou absent qu'on ne voit même pas en scrollant. Une ligne de
contexte/preuve ou une liste à puces peut suivre en corps plus petit mais toujours net et
lisible (specs, bullets, garanties) — jamais du texte décoratif qu'on devine à peine.

Exemple (presse-agrumes, doute = pièces pas lave-vaisselle) : titre **"Rien à laver à la
main."** sous-texte "Toutes les pièces passent au lave-vaisselle, sauf le bloc moteur." —
pas juste "In die Spülmaschine damit." qui nomme la fonctionnalité sans porter le bénéfice
ressenti ni convoquer explicitement l'objection.

Sur les images à specs (5) et contenu (7), les bullets sont une vraie liste visible dans
l'image — 3 à 5 lignes courtes, puce ou tiret, alignées, pas un paragraphe.

Présenter ce plan avec toutes les colonnes exigées en Phase 2 avant de rédiger les prompts
complets si l'utilisateur n'a pas déjà dit "go direct".

## Phase 3 — Écriture des 7 master prompts

C'est le cœur du skill. Chaque prompt est une fiche de shooting complète, pas une phrase.
Structure imposée, dans cet ordre :

```
ONE image. Photorealistic commercial e-commerce photography.

REFERENCE — visual reference input (mandatory): <chemin image source>
Reproduce THE SAME product exactly: same shape, same colours, same proportions,
same control layout, manufacturer wordmark visible and unaltered. Do not redesign,
restyle, or re-brand it.

VISUAL MECHANISM — <rôle graphique précis et mécanisme de preuve : macro chiffrée,
séquence 1-2-3, pièces éclatées, comparaison, grille de faits, etc. Expliquer pourquoi ce
mécanisme est différent des six autres.>

SCENE — <la scène, écrite pour l'avatar : précise, sensorielle, crédible.
Qui/quoi/où, quel résultat visible, quels micro-détails de vie réelle.>

CAMERA & LIGHT — <objectif, ouverture, lumière : direction, qualité, température.>

STYLE — <bloc DA commun : décor, palette (hex du site), ambiance. Identique sur les 7.>

LAYOUT SYSTEM — <hiérarchie, type de plan, angle caméra, échelle du produit, répartition
des panneaux, chiffres, callouts et zone de texte. Rappeler le fond studio continu, les
marges communes et la silhouette distincte en vue miniature.>

COMPOSITION — <cadrage précis, point focal, profondeur, masses visuelles et placement de
chaque objet. Pour les images 2 à 7, réserver une zone réellement lisible au texte.>

TEXT — <UNIQUEMENT sur les images 2 à 7 (jamais sur l'image 1). Render ONLY this exact
[headline / headline + bullet list] directly in the image, LARGE and bold, perfectly
spelled character-for-character, with correct accents, punctuation, capitalization and
line breaks, in <langue du site> : "<texte exact>". Do not translate, paraphrase, add,
remove or duplicate any word. Typography: <description stylistique —
ex. "bold modern serif display type, like a premium editorial headline">, colour <hex du
site>, positioned in the reserved calm zone, sized so it reads clearly even at thumbnail
size — this is the most important legibility requirement in the whole prompt.>

NEGATIVE — no CGI, no 3D render look, no illustration, no oversaturated colours,
no plastic-smooth surfaces, no floating product, no impossible reflections, no fake
certification badges, no watermarks, no added logos, no recognisable faces (hands are
fine)<, no text> (ajouter "no text" UNIQUEMENT sur l'image 1 packshot — sur les images
2 à 7 le texte est voulu et décrit dans le bloc TEXT ci-dessus).

FORMAT — aspect ratio 1:1 (square), generated natively (no padding, no letterboxing,
no cropping a different ratio down to square).
```

**Format : toujours 1:1.** Toutes les images du carrousel, sans exception, sont carrées —
c'est le format universel des carrousels PDP et Google Shopping. Ne jamais varier le ratio
d'une image à l'autre dans un même set.

Ce qui sépare un master prompt du slop IA :

- **Un seul univers visuel, sept silhouettes.** Conserver fond, lumière, texture, marges,
  palette et traitement photo ; changer échelle, angle, cadrage, structure et preuve.
  L'image 6 peut utiliser la version sombre du même système. Une scène résultat reste
  éditoriale et contenue, sans cuisine ou décor qui devienne le sujet.
- **Langage de photographe, pas d'adjectifs creux.** "85mm, f/5.6, one large overhead
  softbox, white side fill" bat "beautiful professional lighting". Repères : packshot et
  plan large → 85-100mm, f/8-f/11, lumière studio homogène ; action/geste → 50mm, f/3.5-f/4 ;
  macro détail → 100mm macro, f/5.6, lumière rasante qui révèle la matière. Toujours le
  même type de source (softbox large, diffusion douce) sur les 7 images.
- **Micro-détails de vie réelle** : gouttes de condensation, pulpe dans le jus, grain du
  bois, miettes — c'est ce qui fait "photo" au lieu de "rendu". Un par scène suffit.
- **La scène vient du brief avatar, mais reste dans le système studio.** L'image 2 met en
  scène le rêve du client (le résultat : jus servi, plat prêt) posé sur le fond studio, pas
  une reconstitution de cuisine. Les mains de l'image 4 ont l'âge et le contexte de l'avatar.
- **Palette ancrée au site** : citer les hex du fond studio (clair = crème/blanc du site,
  sombre = charbon pour l'image 6) pour que le carrousel prolonge la page qui l'affiche.
- **Le modèle ÉCRIT le texte, gros et net, directement dans l'image.** C'est le livrable
  final tel quel (usage ChatGPT/GPT Image, Nano Banana, etc. — pas de deuxième passe). Le
  bloc TEXT donne le texte EXACT entre guillemets (jamais de paraphrase possible côté
  modèle), une description stylistique du lettrage (pas un nom de police précis — un
  modèle image ne charge pas de fichier TTF, mais il suit "bold modern serif display" ou
  "clean modern sans-serif list" de façon fiable), la couleur en hex, et l'exigence de
  lisibilité en miniature. Si le projet dispose du pipeline Codex + `overlay_text.py`
  (police TTF exacte, hex exacts, zéro risque de faute), cette route reste disponible sur
  demande — mais elle n'est plus le chemin par défaut.
- **Cohérence inter-images explicite** : répéter le bloc STYLE mot pour mot dans les 7
  prompts et rappeler les invariants dans chaque LAYOUT SYSTEM. Vérifier en parallèle que
  VISUAL MECHANISM et LAYOUT SYSTEM produisent sept silhouettes distinctes.

## Phase 4 — Livraison

Écrire `prompts-<slug>.md` dans le projet, contenant dans cet ordre :

1. **Brief avatar** (le résumé de Phase 1) et le système studio choisi (clair/sombre,
   hex), en 10 lignes.
2. **Tableau des 7 images** : n°, question du client, bénéfice, objection tuée, mécanisme
   visuel, type de plan, preuve montrée, scène en une ligne, grande phrase prévue (dans la
   langue du site).
3. **Les 7 master prompts complets**, chacun dans un bloc de code, prêts à coller tels
   quels, avec le nom de fichier cible (`<slug>-01-packshot.png` → `<slug>-07-closing.png`).
4. **Annexe texte** : pour chaque image 2 à 7, la grande phrase exacte, le bénéfice et
   l'objection qu'elle porte, la ligne de contexte/bullets si utile, les hex, la zone
   (top/bottom) — en résumé de ce que chaque bloc TEXT contient déjà dans le prompt.

Puis montrer à l'utilisateur le tableau + un des prompts en entier dans la réponse, et
donner le chemin du fichier.

## Génération (UNIQUEMENT sur demande explicite)

Ce skill s'arrête aux prompts. Si — et seulement si — l'utilisateur demande de lancer la
génération (ex. "envoie chez codex") : `scripts/gen_carousel.py` prend un `carousel.json`
où chaque image porte son master prompt complet (clé `"prompt"`), tourne en séquentiel avec
back-off (le générateur throttle après ~12 rendus), récupère les fichiers depuis
`~/.codex/generated_images/` en cas de timeout, et skippe l'existant. Jamais en parallèle.

## Erreurs classiques à éviter

- Écrire les prompts avant le brief avatar → 7 jolies images qui ne vendent rien.
- **Confondre cohérence et répétition** : réutiliser « produit à droite + texte à gauche »
  sur presque toutes les slides. Conserver les invariants de marque, varier les silhouettes.
- **Sortir de l'univers visuel** : introduire une cuisine, une fenêtre, un plan de travail
  envahissant ou une lumière différente. Une scène résultat peut varier son cadrage, pas
  son langage de marque.
- Montrer des pièces, accessoires, détails ou angles absents des références disponibles →
  collecter une photo source additionnelle ou bloquer la slide, jamais inventer.
- **Oublier le bloc TEXT sur une image 2 à 7, ou le laisser vague ("add a nice headline")**
  → le modèle image n'écrit rien ou improvise un texte creux. Le bloc TEXT doit citer le
  texte EXACT entre guillemets, sinon le carrousel sort sans aucun texte lisible — c'est
  l'échec le plus fréquent et le plus visible de tous.
- Laisser une image 2 à 7 sans grande phrase, ou écrire une phrase générique qui ne porte
  ni bénéfice ni objection ("Qualité premium", "Le meilleur choix") → texte décoratif inutile.
- Scènes génériques ("on a nice kitchen counter") → slop. Chaque scène doit contenir le
  rêve ou tuer un doute précis.
- Adjectifs à la place de choix techniques ("stunning", "high quality") → rendu CGI.
- Changer de ratio d'une image à l'autre → toujours 1:1.
- Un texte prévu dans la langue de la conversation au lieu de celle du site.
- Une feature illustrée mais pas nommée en toutes lettres dans le bloc TEXT — le client
  doit pouvoir comprendre le bénéfice sans deviner, même en scrollant vite sur mobile.
- Inventer une spec, une note, un avis, une origine d'expédition ou une garantie — jamais.

## Checklist finale avant de livrer un fichier `prompts-<slug>.md`

- [ ] Chaque produit a sa propre fiche technique et son propre brief avatar — jamais de
      copier-coller de bénéfices/objections d'un produit à l'autre.
- [ ] Image 1 : zéro texte. Images 2 à 7 : un bloc TEXT présent, avec le texte EXACT entre
      guillemets, dans la langue du site.
- [ ] Les 7 prompts contiennent VISUAL MECHANISM et LAYOUT SYSTEM.
- [ ] Les 7 images partagent les invariants (produit, palette, typographies, lumière,
      texture, marges, traitement photo), sauf le virage clair→sombre voulu sur l'image 6.
- [ ] Échelle, angle, cadrage, structure et mécanisme de preuve varient volontairement ;
      jamais plus de deux compositions « produit à droite + texte à gauche ».
- [ ] Test miniature réussi : 7 silhouettes distinguables sans lire, une seule marque en grille.
- [ ] Format 1:1 sur les 7 images, sans exception.
- [ ] Le produit reste identifiable et fidèle à l'image source sur les 7 images (forme,
      couleurs, logo).
- [ ] Toute pièce, tout détail ou angle absent du packshot dispose d'une référence photo
      correspondante ; sinon la génération de la slide est explicitement bloquée.
- [ ] L'arc émotion (1-4) → rationnel (5-7) est respecté, avec une grande phrase qui monte
      la valeur perçue sur 1-4 et qui rassure sur 5-7.
- [ ] Aucune remise, performance, spec, avis, note ou garantie absente des sources réelles.
