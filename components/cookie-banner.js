/**
 * Cookie Consent Banner - PD2i Website
 * Script JavaScript pour la gestion de la bannière de consentement aux cookies
 * ====================================================
 * 
 * Fonctionnalités :
 * - Affichage automatique au premier chargement
 * - Stockage du consentement dans localStorage
 * - Ne réapparaît pas si l'utilisateur a déjà accepté
 * - Animation fluide d'apparition
 * - Fermeture automatique après acceptation
 * - Support multilingue (FR/EN)
 * - Accessible (ARIA compliant)
 */

(function() {
    'use strict';

    /**
     * Classe CookieBanner
     * Gère l'affichage et le comportement de la bannière de cookies
     */
    class CookieBanner {
        constructor() {
            // Clé de stockage dans localStorage
            this.STORAGE_KEY = 'pd2i_cookie_consent';
            
            // Valeurs possibles du consentement
            this.CONSENT_ACCEPTED = 'accepted';
            this.CONSENT_DECLINED = 'declined';
            
            // Délai avant affichage (en millisecondes)
            this.SHOW_DELAY = 500;
            
            // Références aux éléments DOM
            this.banner = null;
            this.acceptButton = null;
            this.learnMoreLink = null;
            
            // Langue actuelle (détectée automatiquement)
            this.currentLang = this.detectLanguage();
            
            // Initialisation
            this.init();
        }
        
        /**
         * Détecte la langue du navigateur
         * @returns {string} 'fr' ou 'en'
         */
        detectLanguage() {
            const browserLang = navigator.language || navigator.userLanguage;
            const lang = browserLang.toLowerCase().split('-')[0];
            
            // Vérifier si la langue est définie dans l'URL ou dans un élément HTML
            const htmlLang = document.documentElement.lang;
            if (htmlLang) {
                const htmlLangCode = htmlLang.toLowerCase().split('-')[0];
                if (htmlLangCode === 'fr' || htmlLangCode === 'en') {
                    return htmlLangCode;
                }
            }
            
            // Retourner 'fr' par défaut, sinon 'en'
            return (lang === 'fr') ? 'fr' : 'en';
        }
        
        /**
         * Initialise la bannière
         */
        init() {
            // Attendre que le DOM soit chargé
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => this.setupBanner());
            } else {
                this.setupBanner();
            }
        }
        
        /**
         * Configure la bannière
         */
        setupBanner() {
            // Récupérer les éléments DOM
            this.banner = document.getElementById('cookieBanner');
            
            if (!this.banner) {
                console.warn('Cookie banner element not found');
                return;
            }
            
            this.acceptButton = document.getElementById('cookieBannerAccept');
            this.learnMoreLink = document.getElementById('cookieBannerLearnMore');
            
            // Vérifier si l'utilisateur a déjà donné son consentement
            const consent = this.getConsent();
            
            if (consent === this.CONSENT_ACCEPTED) {
                // L'utilisateur a déjà accepté, ne pas afficher la bannière
                this.hideBanner();
                return;
            }
            
            // Configurer la langue
            this.setLanguage(this.currentLang);
            
            // Ajouter les écouteurs d'événements
            this.attachEventListeners();
            
            // Afficher la bannière après un court délai
            setTimeout(() => {
                this.showBanner();
            }, this.SHOW_DELAY);
        }
        
        /**
         * Configure la langue de la bannière
         * @param {string} lang - Code de langue ('fr' ou 'en')
         */
        setLanguage(lang) {
            const isFrench = lang === 'fr';
            
            // Afficher/masquer les textes selon la langue
            const frTexts = this.banner.querySelectorAll('.cookie-banner__text-fr, .cookie-banner__btn-text-fr');
            const enTexts = this.banner.querySelectorAll('.cookie-banner__text-en, .cookie-banner__btn-text-en');
            
            frTexts.forEach(el => {
                el.style.display = isFrench ? 'inline' : 'none';
            });
            
            enTexts.forEach(el => {
                el.style.display = isFrench ? 'none' : 'inline';
            });
            
            // Mettre à jour les attributs ARIA
            if (this.acceptButton) {
                this.acceptButton.setAttribute(
                    'aria-label',
                    isFrench ? 'Accepter tous les cookies' : 'Accept all cookies'
                );
            }
            
            if (this.learnMoreLink) {
                this.learnMoreLink.setAttribute(
                    'aria-label',
                    isFrench ? 'En savoir plus sur notre politique de cookies' : 'Learn more about our cookie policy'
                );
            }
        }
        
        /**
         * Ajoute les écouteurs d'événements
         */
        attachEventListeners() {
            // Bouton "Accepter"
            if (this.acceptButton) {
                this.acceptButton.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.acceptCookies();
                });
            }
            
            // Lien "En savoir plus" - pas besoin d'écouteur, c'est un lien normal
            // Mais on peut ajouter un tracking si nécessaire
            
            // Écouter les changements de langue (si le site a un sélecteur de langue)
            document.addEventListener('languageChanged', (event) => {
                if (event.detail && event.detail.language) {
                    const lang = event.detail.language.toLowerCase().split('-')[0];
                    if (lang === 'fr' || lang === 'en') {
                        this.setLanguage(lang);
                    }
                }
            });
        }
        
        /**
         * Affiche la bannière avec animation
         */
        showBanner() {
            if (!this.banner) return;
            
            // Ajouter la classe pour l'animation
            this.banner.classList.add('cookie-banner--visible');
            
            // Annoncer aux lecteurs d'écran
            this.banner.setAttribute('aria-hidden', 'false');
        }
        
        /**
         * Masque la bannière avec animation
         */
        hideBanner() {
            if (!this.banner) return;
            
            // Retirer la classe pour l'animation
            this.banner.classList.remove('cookie-banner--visible');
            
            // Après l'animation, masquer complètement
            setTimeout(() => {
                if (this.banner) {
                    this.banner.style.display = 'none';
                    this.banner.setAttribute('aria-hidden', 'true');
                }
            }, 400); // Correspond à la durée de l'animation CSS
        }
        
        /**
         * Gère l'acceptation des cookies
         */
        acceptCookies() {
            // Sauvegarder le consentement
            this.saveConsent(this.CONSENT_ACCEPTED);
            
            // Masquer la bannière
            this.hideBanner();
            
            // Émettre un événement personnalisé pour que d'autres scripts puissent réagir
            const event = new CustomEvent('cookieConsentAccepted', {
                detail: {
                    consent: this.CONSENT_ACCEPTED,
                    timestamp: new Date().toISOString()
                }
            });
            document.dispatchEvent(event);
            
            // Log pour le débogage (peut être retiré en production)
            if (console && console.log) {
                console.log('Cookie consent accepted and saved');
            }
        }
        
        /**
         * Récupère le consentement depuis localStorage
         * @returns {string|null} Le statut du consentement ou null
         */
        getConsent() {
            try {
                return localStorage.getItem(this.STORAGE_KEY);
            } catch (e) {
                // localStorage non disponible (mode privé, etc.)
                console.warn('localStorage not available:', e);
                return null;
            }
        }
        
        /**
         * Sauvegarde le consentement dans localStorage
         * @param {string} consent - Le statut du consentement
         */
        saveConsent(consent) {
            try {
                localStorage.setItem(this.STORAGE_KEY, consent);
                
                // Ajouter également une date d'expiration (optionnel, pour conformité RGPD)
                const expirationDate = new Date();
                expirationDate.setFullYear(expirationDate.getFullYear() + 1); // 1 an
                localStorage.setItem(this.STORAGE_KEY + '_expires', expirationDate.toISOString());
            } catch (e) {
                console.warn('Could not save consent to localStorage:', e);
            }
        }
        
        /**
         * Vérifie si le consentement a expiré
         * @returns {boolean} True si expiré ou inexistant
         */
        isConsentExpired() {
            try {
                const expirationDate = localStorage.getItem(this.STORAGE_KEY + '_expires');
                if (!expirationDate) return true;
                
                const expiration = new Date(expirationDate);
                return new Date() > expiration;
            } catch (e) {
                return true;
            }
        }
        
        /**
         * Réinitialise le consentement (utile pour les tests ou la conformité)
         */
        resetConsent() {
            try {
                localStorage.removeItem(this.STORAGE_KEY);
                localStorage.removeItem(this.STORAGE_KEY + '_expires');
            } catch (e) {
                console.warn('Could not reset consent:', e);
            }
        }
    }
    
    // Initialiser la bannière lorsque le script est chargé
    // Utiliser une fonction auto-exécutée pour éviter les conflits de scope
    (function() {
        // Attendre que le DOM soit prêt
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                window.cookieBanner = new CookieBanner();
            });
        } else {
            window.cookieBanner = new CookieBanner();
        }
    })();
    
    // Exposer une méthode globale pour réinitialiser le consentement (utile pour les tests)
    window.resetCookieConsent = function() {
        if (window.cookieBanner) {
            window.cookieBanner.resetConsent();
            // Recharger la page pour réafficher la bannière
            window.location.reload();
        }
    };
    
})();






