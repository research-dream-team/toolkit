# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Research Dream Team Toolkit'
copyright = '2023, Research Dream Team'
author = 'Research Dream Team'

release = '1.0.1'
version = '1.0.1'

# -- General configuration

extensions = [
    'sphinx.ext.todo',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_css_files = ['css/custom.css']

# -- Options for EPUB output

epub_show_urls = 'footnote'

# -- Options for todo items

todo_include_todos = True
todo_link_only = True