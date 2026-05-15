# 🌐 Configuration Multilingue - PD2i Website

## Structure

Le site est maintenant organisé en 3 langues :

```
/
├── en/          # Pages en anglais
├── fr/          # Pages en français  
├── zh/          # Pages en chinois
├── assets/      # Ressources partagées (images, CSS, JS)
├── components/  # Composants partagés (Header, Footer)
└── index.html   # Page de redirection automatique
```

## Fonctionnalités

### 1. Détection automatique de langue
- La page `index.html` à la racine détecte la langue du navigateur
- Redirige automatiquement vers `/en/`, `/fr/` ou `/zh/`

### 2. Changement de langue
- Le sélecteur de langue dans le Header redirige vers la même page dans l'autre langue
- Exemple : `/en/services.html` → clic sur FR → `/fr/services.html`
- Exemple : `/fr/services.html` → clic sur ZH → `/zh/services.html`

### 3. Chemins relatifs
- Toutes les pages dans `/en/`, `/fr/`, `/de/` utilisent `../assets/` et `../components/`
- Les liens entre pages utilisent `../page.html`

## Scripts disponibles

### `setup-multilang.py`
Duplique toutes les pages HTML dans chaque dossier langue et ajuste les chemins.

**Usage :**
```bash
python3 setup-multilang.py
```

### `update-languages.py`
Met à jour la configuration des langues dans toutes les pages (ajoute ZH, détection automatique).

**Usage :**
```bash
python3 update-languages.py
```

## Prochaines étapes

1. ✅ Structure créée
2. ✅ Chemins ajustés
3. ✅ Header mis à jour
4. ✅ Sitemap mis à jour
5. ⏳ **Traduire le contenu dans `/fr/` et `/zh/`**
   - Les pages sont prêtes, il ne reste plus qu'à traduire le texte
   - Vous pouvez utiliser un traducteur professionnel ou un service comme DeepL
   - **Vous vous occupez de la traduction** ✅

## Notes importantes

- Les pages dans `/fr/` et `/zh/` sont actuellement en anglais (copies de `/en/`)
- Une fois traduites, elles resteront figées (pas de synchronisation automatique)
- Pour mettre à jour le site anglais, modifiez uniquement les fichiers dans `/en/`
- Les autres langues ne seront pas affectées

## URLs

- Anglais : `https://www.pd2i.com/en/index.html`
- Français : `https://www.pd2i.com/fr/index.html`
- Chinois : `https://www.pd2i.com/zh/index.html`
- Racine : `https://www.pd2i.com/` (redirige automatiquement)

## SEO

- Toutes les pages ont des balises `hreflang` correctement configurées
- Le sitemap.xml inclut toutes les versions linguistiques
- Les URLs canoniques pointent vers la bonne version linguistique

