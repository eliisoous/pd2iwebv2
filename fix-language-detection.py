#!/usr/bin/env python3
"""
Script pour ajouter la détection automatique de langue dans toutes les pages
"""

import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).parent
LANGUAGES = ['en', 'fr', 'zh']

def add_language_detection(content):
    """
    Ajoute le code de détection de langue si absent
    """
    # Vérifier si la détection existe déjà
    if 'const pathParts = window.location.pathname' in content:
        return content
    
    # Code de détection à ajouter
    detection_code = """        // Détecter la langue depuis l'URL
        const pathParts = window.location.pathname.split('/').filter(p => p);
        let detectedLang = 'EN';
        if (pathParts.length > 0) {
            const firstPart = pathParts[0].toLowerCase();
            if (['en', 'fr', 'zh'].includes(firstPart)) {
                detectedLang = firstPart.toUpperCase();
            }
        }
        
"""
    
    # Trouver la position juste avant "// Initialisation du header"
    pattern = r'(// Initialisation du header avec la configuration PD2i)'
    match = re.search(pattern, content)
    
    if match:
        insert_pos = match.start()
        content = content[:insert_pos] + detection_code + content[insert_pos:]
    
    return content

def process_file(html_file, lang):
    """
    Traite un fichier HTML
    """
    source_path = ROOT_DIR / lang / html_file
    if not source_path.exists():
        return False
    
    # Lire le contenu
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ajouter la détection si nécessaire
    if 'currentLang: detectedLang' in content and 'const pathParts' not in content:
        content = add_language_detection(content)
        
        # Écrire le fichier mis à jour
        with open(source_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {lang}/{html_file}")
        return True
    
    return False

def main():
    """
    Fonction principale
    """
    print("🚀 Ajout de la détection de langue...\n")
    
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

