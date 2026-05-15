#!/usr/bin/env python3
"""
Script pour mettre à jour les langues dans toutes les pages HTML
Ajoute ZH et détecte automatiquement la langue depuis l'URL
"""

import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).parent
LANGUAGES = ['en', 'fr', 'zh']

def update_language_config(content, lang):
    """
    Met à jour la configuration de langue dans le Header
    """
    lang_upper = lang.upper()
    
    # Mettre à jour currentLang pour détecter depuis l'URL
    # D'abord essayer de détecter depuis l'URL, sinon utiliser la langue du dossier
    detect_lang_script = f"""
        // Détecter la langue depuis l'URL
        const pathParts = window.location.pathname.split('/').filter(p => p);
        let detectedLang = '{lang_upper}';
        if (pathParts.length > 0) {{
            const firstPart = pathParts[0].toLowerCase();
            if (['en', 'fr', 'de'].includes(firstPart)) {{
                detectedLang = firstPart.toUpperCase();
            }}
        }}
"""
    
    # Remplacer currentLang: 'EN' par la détection automatique
    content = re.sub(
        r"currentLang:\s*'[^']*'",
        f"currentLang: detectedLang || '{lang_upper}'",
        content
    )
    
    # Mettre à jour languages pour inclure ZH
    content = re.sub(
        r"languages:\s*\[('[^']*',?\s*)+'?[^']*'?\]",
        "languages: ['EN', 'FR', 'ZH']",
        content
    )
    
    # Ajouter le script de détection avant window.headerInstance
    if 'window.headerInstance = new Header' in content and 'detectedLang' not in content:
        # Trouver la position juste avant window.headerInstance
        match = re.search(r'(// Initialisation du header.*?\n)', content, re.DOTALL)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + detect_lang_script + content[insert_pos:]
    
    return content

def process_file(html_file, lang):
    """
    Traite un fichier HTML pour une langue donnée
    """
    source_path = ROOT_DIR / lang / html_file
    if not source_path.exists():
        return False
    
    # Lire le contenu
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mettre à jour la configuration
    content = update_language_config(content, lang)
    
    # Écrire le fichier mis à jour
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {lang}/{html_file}")
    return True

def main():
    """
    Fonction principale
    """
    print("🚀 Mise à jour des configurations de langue...\n")
    
    html_files = [
        'index.html', 'about-us.html', 'contacts.html', 'cookies.html', 'dlc.html',
        'download.html', 'edge-preparation.html', 'greenclean-ultrasonic-cleaning.html',
        'legal.html', 'news.html', 'plasma-nitriding.html', 'privacy.html',
        'pvd-cutting-tools.html', 'pvd-molds-dies.html', 'services.html',
        'turnkey-solutions.html', '404.html',
        'art-competence-center.html', 'art-dlc-indonesia.html',
        'art-grinding-hub-2026.html', 'art-news-edgeprep.html'
    ]
    
    processed = 0
    for lang in LANGUAGES:
        print(f"\n🌐 Traitement pour: {lang.upper()}")
        print("-" * 50)
        for html_file in html_files:
            if process_file(html_file, lang):
                processed += 1
    
    print(f"\n\n✨ Terminé! {processed} fichiers mis à jour")

if __name__ == '__main__':
    main()

