project = "Patrimoine du STT"
copyright = '2026-02, on'
author = 'Olivier Nalin'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_css_files = ['custom.css']
html_favicon = './_static/logoTunnel.jpg'
html_static_path = ['_static']
html_show_copyright = False
html_show_sphinx = False
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "logo.jpg",
    "dark_logo": "logo.jpg",   
}
# -- Options pour le format PDF (LaTeX) --------------------------------------
latex_engine = 'pdflatex' # ou 'xelatex' pour un meilleur support des polices
latex_documents = [
    ('index', 'PatrimoineSTT.tex', 'Patrimoine du STT', author, 'manual'),
]

# Optionnel : Personnaliser la page de garde
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
        \usepackage{fourier} % Une police élégante pour le patrimoine
        \setlength{\headheight}{14pt}
    ''',
}

