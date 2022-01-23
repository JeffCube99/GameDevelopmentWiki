# Configuration file for the Sphinx documentation builder.


###################### Fetching images stored through GitLFS ######################
import sys
import os

# PYTHONPATH = docs/source
DOC_SOURCES_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(DOC_SOURCES_DIR))
sys.path.insert(0, DOC_SOURCES_DIR)
print('PROJECT_ROOT_DIR', PROJECT_ROOT_DIR)

# If runs on ReadTheDocs environment
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Hack for lacking git-lfs support ReadTheDocs
if on_rtd:
    print('Fetching files with git_lfs')
    from git_lfs import fetch
    fetch(PROJECT_ROOT_DIR)

########################################################################################

# -- Project information

project = 'GameDevelopmentWiki'
copyright = '2022, JeffCube'
author = 'JeffCube'

version = '0.0.1'
release = version

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
