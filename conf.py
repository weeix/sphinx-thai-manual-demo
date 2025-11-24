# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'Thai Manual Demo'
copyright = '2024, Author'
author = 'Author'

language = 'th'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'

html_static_path = ['_static']

todo_include_todos = True

# LaTeX settings for Thai PDF output
latex_engine = 'lualatex'
latex_use_xindy = False
latex_elements = {
    'babel': '\\usepackage[thai]{babel}',
    'fontpkg': '\\setmainfont{TH Sarabun New}',
    'preamble': '\\babelprovide[import, main]{thai}',
}
