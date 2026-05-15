#!/usr/bin/env python3
"""
Script pour créer la structure multilingue du site PD2i
Duplique toutes les pages HTML dans /en/, /fr/, /zh/ et ajuste les chemins relatifs
"""

import os
import re
import shutil
from pathlib import Path

# Configuration
ROOT_DIR = Path(__file__).parent
LANGUAGES = ['en', 'fr', 'zh']
HTML_FILES = [
    'index.html', 'about-us.html', 'contacts.html', 'cookies.html', 'dlc.html',
    'download.html', 'edge-preparation.html', 'greenclean-ultrasonic-cleaning.html',
    'legal.html', 'news.html', 'plasma-nitriding.html', 'privacy.html',
    'pvd-cutting-tools.html', 'pvd-molds-dies.html', 'services.html',
    'turnkey-solutions.html', '404.html',
    'art-competence-center.html', 'art-dlc-indonesia.html',
    'art-grinding-hub-2026.html', 'art-news-edgeprep.html'
]

def adjust_paths(content, lang):
    """
    Ajuste les chemins relatifs dans le contenu HTML pour la langue spécifiée
    """
    # Chemins à ajuster : assets/, components/ -> ../assets/, ../components/
    content = re.sub(r'href="(assets/)', r'href="../\1', content)
    content = re.sub(r'src="(assets/)', r'src="../\1', content)
    content = re.sub(r'href="(components/)', r'href="../\1', content)
    content = re.sub(r'src="(components/)', r'src="../\1', content)
    
    # Liens vers autres pages HTML (sauf ceux qui commencent par http ou #)
    # index.html -> ../index.html (mais pas si c'est déjà ../ ou http://)
    def replace_html_link(match):
        prefix = match.group(1)  # href=" ou src="
        link = match.group(2)     # le lien
        if link.startswith(('http://', 'https://', '#', '/', '../')):
            return match.group(0)  # Ne pas modifier
        if link.endswith('.html'):
            return f'{prefix}../{link}'
        return match.group(0)
    
    content = re.sub(r'(href=")([^"]+\.html)', replace_html_link, content)
    
    # Mettre à jour les URLs absolues dans les balises hreflang et canonical
    base_url = 'https://www.pd2i.com'
    
    # Hreflang : ajouter /lang/ dans l'URL
    def update_hreflang(match):
        lang_code = match.group(1)
        url = match.group(2)
        if lang_code == lang:
            # URL de la langue actuelle
            new_url = url.replace('https://www.pd2i.com/', f'https://www.pd2i.com/{lang}/')
        else:
            # URL des autres langues
            if lang_code == 'en':
                new_url = url.replace('https://www.pd2i.com/', 'https://www.pd2i.com/en/')
            elif lang_code == 'fr':
                new_url = url.replace('https://www.pd2i.com/', 'https://www.pd2i.com/fr/')
            elif lang_code == 'zh':
                new_url = url.replace('https://www.pd2i.com/', 'https://www.pd2i.com/zh/')
            else:
                new_url = url
        return f'<link rel="alternate" hreflang="{lang_code}" href="{new_url}">'
    
    content = re.sub(
        r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"',
        update_hreflang,
        content
    )
    
    # Canonical : ajouter /lang/ dans l'URL
    def update_canonical(match):
        url = match.group(1)
        new_url = url.replace('https://www.pd2i.com/', f'https://www.pd2i.com/{lang}/')
        return f'<link rel="canonical" href="{new_url}">'
    
    content = re.sub(
        r'<link rel="canonical" href="([^"]+)"',
        update_canonical,
        content
    )
    
    # Corriger les doubles >> qui peuvent apparaître
    content = re.sub(r'>>', '>', content)
    
    # Mettre à jour og:url et autres meta tags avec URLs
    content = re.sub(
        r'(<meta property="og:url" content=")(https://www\.pd2i\.com/)([^"]+)"',
        lambda m: f'{m.group(1)}{m.group(2)}{lang}/{m.group(3)}"',
        content
    )
    
    # Mettre à jour le lang dans <html lang="...">
    content = re.sub(
        r'<html lang="[^"]*"',
        f'<html lang="{lang}"',
        content,
        count=1
    )
    
    # Mettre à jour og:locale
    locale_map = {'en': 'en_US', 'fr': 'fr_FR', 'zh': 'zh_CN'}
    content = re.sub(
        r'(<meta property="og:locale" content=")[^"]*"',
        f'\\1{locale_map.get(lang, "en_US")}"',
        content
    )
    
    return content

def update_header_footer_config(content, lang):
    """
    Met à jour la configuration du Header et Footer pour pointer vers les bonnes URLs
    """
    # Mettre à jour les liens dans navigationItems
    def update_nav_link(match):
        href = match.group(1)
        if href.startswith('http') or href == '#' or href.startswith('/'):
            return match.group(0)
        if href.endswith('.html'):
            return f'href: \'../{href}\''
        return match.group(0)
    
    content = re.sub(
        r"href: '([^']+\.html)'",
        update_nav_link,
        content
    )
    
    # Mettre à jour logoLink
    content = re.sub(
        r"logoLink: 'index\.html'",
        f"logoLink: '../index.html'",
        content
    )
    
    return content

def process_file(html_file, lang):
    """
    Traite un fichier HTML pour une langue donnée
    """
    source_path = ROOT_DIR / html_file
    if not source_path.exists():
        print(f"⚠️  Fichier non trouvé: {html_file}")
        return False
    
    target_dir = ROOT_DIR / lang
    target_dir.mkdir(exist_ok=True)
    target_path = target_dir / html_file
    
    # Lire le contenu source
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ajuster les chemins
    content = adjust_paths(content, lang)
    content = update_header_footer_config(content, lang)
    
    # Écrire dans le dossier langue
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {lang}/{html_file}")
    return True

def main():
    """
    Fonction principale
    """
    print("🚀 Démarrage de la création de la structure multilingue...\n")
    
    # Créer les dossiers
    for lang in LANGUAGES:
        lang_dir = ROOT_DIR / lang
        lang_dir.mkdir(exist_ok=True)
        print(f"📁 Dossier créé: {lang}/")
    
    print()
    
    # Traiter chaque fichier HTML pour chaque langue
    total_files = len(HTML_FILES) * len(LANGUAGES)
    processed = 0
    
    for lang in LANGUAGES:
        print(f"\n🌐 Traitement pour la langue: {lang.upper()}")
        print("-" * 50)
        
        for html_file in HTML_FILES:
            if process_file(html_file, lang):
                processed += 1
    
    print(f"\n\n✨ Terminé! {processed}/{total_files} fichiers créés")
    print("\n📝 Prochaines étapes:")
    print("   1. Vérifier quelques pages dans /en/, /fr/, /de/")
    print("   2. Traduire le contenu dans /fr/ et /de/")
    print("   3. Mettre à jour le Header.js pour gérer le changement de langue")
    print("   4. Mettre à jour le sitemap.xml")

if __name__ == '__main__':
    main()

