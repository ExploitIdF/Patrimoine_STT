Pour votre projet "Patrimoine du STT" hébergé sur GitHub, vous avez une solution "en ligne" très efficace qui ne nécessite pas d'installer LaTeX (très lourd) sur votre machine.

Comme vous utilisez déjà le thème **Furo**, voici la stratégie la plus simple pour obtenir un PDF via GitHub Actions :

### 1. La Solution "GitHub Actions" (Automatisée)

Cette méthode va créer le PDF automatiquement à chaque "Push" sur GitHub et le rendre disponible dans l'onglet **Actions** de votre dépôt.

Créez un fichier `.github/workflows/pdf_build.yml` dans votre dépôt :

```yaml
name: Generation PDF
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install sphinx furo sphinx-simplepdf

      - name: Build PDF
        run: |
          # sphinx-simplepdf utilise un moteur léger sans LaTeX
          sphinx-build -b simplepdf . _build/simplepdf

      - name: Upload PDF
        uses: actions/upload-artifact@v4
        with:
          name: Patrimoine-STT-PDF
          path: _build/simplepdf/*.pdf

```

---

### 2. Modification de votre `conf.py`

Pour que cela fonctionne avec l'extension légère `sphinx-simplepdf` (qui est bien plus facile à gérer en ligne que LaTeX), ajoutez ceci à votre configuration :

```python
extensions = [
    'sphinx_simplepdf',
    # vos autres extensions...
]

# Optionnel : Personnaliser le PDF pour qu'il ressemble à votre charte
simplepdf_vars = {
    'primary': '#333333', # Couleur principale
    'links': '#0055aa',   # Couleur des liens
    'cover-bg': 'url(logoTunnel.jpg) no-repeat center',
}

```

---

### 3. Comment récupérer votre PDF ?

Une fois que vous avez envoyé (push) ces fichiers sur GitHub :

1. Allez sur l'onglet **Actions** de votre dépôt GitHub.
2. Cliquez sur le dernier "workflow" qui vient de tourner.
3. En bas de la page, dans la section **Artifacts**, vous trouverez un lien pour télécharger votre PDF.

### Pourquoi cette solution ?

* **Zéro installation :** Tout se passe sur les serveurs de GitHub.
* **Léger :** Pas besoin de TeXLive (2Go+).
* **Gratuit :** GitHub Actions est gratuit pour les dépôts publics.

> **Note sur votre lien :** `:doc:Croisement CI-TEX SIRIUS 2025<35_comparaison>` fonctionnera parfaitement dans le PDF généré par cette méthode. Les liens internes seront convertis en hyperliens cliquables à l'intérieur du document.

Souhaitez-vous que je vous aide à personnaliser la page de garde (titre, logo) pour que le PDF soit prêt à être imprimé ?