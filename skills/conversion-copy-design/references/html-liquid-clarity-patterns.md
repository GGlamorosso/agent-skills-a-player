# Patterns HTML/Liquid — clarté anti-slop

Gabarits directement utilisables (HTML + CSS inline en `<style>` de démo — à déplacer dans le fichier CSS du thème en prod). Conformes aux règles de la section 4 du `SKILL.md` : radius minimal, couleurs pleines, bordures visibles plutôt qu'ombres flottantes, texte dense. Chaque bloc indique où insérer les tags Liquid Shopify pour le rendre dynamique.

Variables de style communes à réutiliser (adapte les valeurs à la marque, mais garde la logique : radius faible, une seule couleur d'accent, bordures fines) :

```css
:root {
  --color-text: #1a1a1a;
  --color-text-muted: #5a5a5a;
  --color-bg: #ffffff;
  --color-bg-alt: #f5f3ef;
  --color-accent: #1e3a5f;      /* une seule couleur d'accent, pleine */
  --color-border: #d8d4cc;
  --radius: 4px;                 /* jamais > 8px sauf avatar digital-native confirmé */
  --font-heading: Georgia, "Times New Roman", serif; /* ou un slab épais */
  --font-body: -apple-system, "Segoe UI", Arial, sans-serif;
}
```

## Hero

```html
<section class="hero">
  <div class="hero__media">
    <!-- Liquid: {{ section.settings.hero_image | image_url: width: 1200 | image_tag }} -->
    <img src="product-real-photo.jpg" alt="Photo réelle du produit en situation">
  </div>
  <div class="hero__content">
    <h1>{{ section.settings.headline }}</h1>
    <!-- headline = bénéfice dominant en phrase complète, pas un fragment -->
    <p class="hero__subhead">{{ section.settings.subheadline }}</p>
    <a href="{{ section.settings.cta_url }}" class="btn btn--primary">{{ section.settings.cta_label }}</a>
    <p class="hero__proof">★★★★★ {{ shop.metafields.reviews.rating }}/5 · {{ shop.metafields.reviews.count }} avis vérifiés</p>
  </div>
</section>

<style>
.hero { display: grid; grid-template-columns: 1.1fr 1fr; gap: 0; border-bottom: 1px solid var(--color-border); }
.hero__media img { width: 100%; height: 100%; object-fit: cover; display: block; }
.hero__content { padding: 48px; background: var(--color-bg-alt); display: flex; flex-direction: column; justify-content: center; gap: 16px; }
.hero__content h1 { font-family: var(--font-heading); font-size: clamp(28px, 4vw, 44px); font-weight: 700; color: var(--color-text); margin: 0; line-height: 1.15; }
.hero__subhead { font-family: var(--font-body); font-size: 17px; line-height: 1.6; color: var(--color-text-muted); margin: 0; max-width: 46ch; }
.hero__proof { font-size: 14px; color: var(--color-text-muted); margin: 0; }
</style>
```

## Bandeau réassurance

Rectangles à bordure fine, jamais de fond coloré plein ni de pilule — voir Étude B dans `case-studies.md`.

```html
<ul class="trust-bar">
  {% for item in section.blocks %}
    <li class="trust-bar__item">
      <span class="trust-bar__icon">{{ item.settings.icon }}</span>
      <span class="trust-bar__label">{{ item.settings.label }}</span>
    </li>
  {% endfor %}
</ul>

<style>
.trust-bar { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0; list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border); }
.trust-bar__item { display: flex; align-items: center; gap: 10px; padding: 16px 20px; border-right: 1px solid var(--color-border); font-size: 14px; color: var(--color-text); }
.trust-bar__item:last-child { border-right: none; }
</style>
```

## Bullets USP (au-dessus du CTA d'achat)

Format bénéfice-en-gras : preuve — jamais une feature nue (voir le skill `copywriting-a-player` inclus dans ce dépôt pour approfondir le copy).

```html
<ul class="usp-list">
  {% for block in section.blocks %}
    <li class="usp-list__item">
      <strong>{{ block.settings.benefit }} :</strong> {{ block.settings.proof }}
    </li>
  {% endfor %}
</ul>

<style>
.usp-list { list-style: none; margin: 0 0 24px; padding: 0; display: flex; flex-direction: column; gap: 10px; }
.usp-list__item { padding-left: 22px; position: relative; font-size: 15px; line-height: 1.5; color: var(--color-text); }
.usp-list__item::before { content: "✓"; position: absolute; left: 0; color: var(--color-accent); font-weight: 700; }
</style>
```

## Tableau comparatif

```html
<table class="compare-table">
  <thead>
    <tr>
      <th></th>
      <th>Alternative bon marché</th>
      <th class="compare-table__highlight">{{ shop.name }}</th>
      <th>Alternative complexe/chère</th>
    </tr>
  </thead>
  <tbody>
    {% for row in section.blocks %}
    <tr>
      <td>{{ row.settings.criterion }}</td>
      <td>{{ row.settings.cheap_value }}</td>
      <td class="compare-table__highlight">{{ row.settings.our_value }}</td>
      <td>{{ row.settings.complex_value }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<style>
.compare-table { width: 100%; border-collapse: collapse; font-size: 14px; }
.compare-table th, .compare-table td { border: 1px solid var(--color-border); padding: 12px 14px; text-align: left; }
.compare-table th { background: var(--color-bg-alt); font-family: var(--font-heading); font-weight: 700; }
.compare-table__highlight { background: #eef3f8; font-weight: 600; }
</style>
```

## FAQ accordéon

Utilise `<details>`/`<summary>` natif plutôt qu'un accordéon JS custom — accessible par défaut, comportement prévisible (attendu par un avatar web classique).

```html
<div class="faq">
  {% for block in section.blocks %}
    <details class="faq__item">
      <summary>{{ block.settings.question }}</summary>
      <p>{{ block.settings.answer }}</p>
    </details>
  {% endfor %}
</div>

<style>
.faq__item { border-bottom: 1px solid var(--color-border); padding: 16px 0; }
.faq__item summary { cursor: pointer; font-weight: 600; font-size: 15px; color: var(--color-text); list-style: none; }
.faq__item summary::-webkit-details-marker { display: none; }
.faq__item summary::before { content: "+ "; color: var(--color-accent); font-weight: 700; }
.faq__item[open] summary::before { content: "– "; }
.faq__item p { margin: 10px 0 0; font-size: 14px; line-height: 1.6; color: var(--color-text-muted); }
</style>
```

## Bloc add-to-cart PDP

```html
<div class="atc-block">
  <p class="atc-block__rating">★★★★★ {{ product.metafields.reviews.rating }}/5 · {{ product.metafields.reviews.count }} avis</p>
  <h1 class="atc-block__title">{{ product.title }}</h1>
  <p class="atc-block__price">{{ product.price | money }}</p>

  <ul class="usp-list">
    <!-- réutilise le pattern usp-list ci-dessus -->
  </ul>

  {% form 'product', product %}
    <button type="submit" class="btn btn--primary btn--full">Ajouter au panier</button>
  {% endform %}

  <ul class="atc-block__badges">
    <li>Livraison gratuite — 2 à 5 jours</li>
    <li>Garantie 2 ans</li>
    <li>Retour 30 jours</li>
  </ul>
</div>

<style>
.atc-block__rating { font-size: 13px; color: var(--color-text-muted); margin: 0 0 6px; }
.atc-block__title { font-family: var(--font-heading); font-size: 26px; margin: 0 0 8px; }
.atc-block__price { font-size: 22px; font-weight: 700; color: var(--color-text); margin: 0 0 20px; }
.atc-block__badges { list-style: none; margin: 16px 0 0; padding: 12px 0 0; border-top: 1px solid var(--color-border); display: flex; flex-direction: column; gap: 6px; font-size: 13px; color: var(--color-text-muted); }
</style>
```

## Bouton — le composant le plus souvent transformé en pilule slop par défaut

```css
.btn {
  display: inline-block;
  padding: 14px 28px;
  border-radius: var(--radius); /* jamais 999px/pilule par défaut */
  font-weight: 600;
  font-size: 15px;
  text-decoration: none;
  text-align: center;
  border: none;
  cursor: pointer;
}
.btn--primary { background: var(--color-accent); color: #fff; }
.btn--full { width: 100%; }
/* Pas de box-shadow colorée flottante, pas de dégradé. Un hover simple suffit : */
.btn--primary:hover { background: color-mix(in srgb, var(--color-accent) 85%, black); }
```

## Rappel

Ces gabarits sont un point de départ structurel, pas un habillage à copier tel quel. Ajuste les couleurs/polices à la marque réelle, mais garde la logique anti-slop : radius faible, bordures visibles, une seule couleur d'accent, texte dense en phrases complètes, `<details>` natif plutôt que du JS custom pour les interactions simples.
