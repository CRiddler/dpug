# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information ------------------------------------------------

project = "Davis PUG"
copyright = "2021, UC Davis DataLab, Python User Group"
author = "Cameron Riddell"

import pydata_sphinx_theme  # noqa: E402 (ignore "import not at top")

version = pydata_sphinx_theme.__version__.replace("dev0", "")

# -- General configuration ----------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_external_toc",
    "sphinx_panels",
    "sphinx_togglebutton",
]

# -- myst_nb/jupyter_cache configuration --------------------------------
jupyter_execute_notebooks = "cache"
execution_excludepatterns = []
execution_in_temp = False
execution_allow_errors = False

# -- myst specific extensions --------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    # "amsmath",
    "colon_fence",
    # "deflist",
    "dollarmath",
    # "html_admonition",
    # "html_image",
    # "linkify",
    # "replacements",
    # "smartquotes",
    # "substitution",
    # "tasklist",
]

myst_update_mathjax = False
# URI schemes that will be recognised as external URLs in Markdown links
myst_url_schemes = ["mailto", "http", "https"]

# -- myst_nb/jupyter_cache configuration --------------------------------
jupyter_execute_notebooks = "cache"
execution_excludepatterns = []
execution_in_temp = False
execution_allow_errors = False

# -- sphinx_external_toc configuration ----------------------------------
external_toc_path = "_toc.yml"
external_toc_exclude_missing = False

# -- Internationalization ------------------------------------------------
# specifying the natural language populates some key tags
language = "en"

autosummary_generate = True

# -- Build Options ------------------------------------------------
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".ipynb_checkpoints"]

# -- Sidebar composition ------------------------------------------------
html_sidebar_default = ["navbar-logo", "search-field", "sidebar-nav-bs"]
html_sidebar_binder = ["navbar-logo", "search-field", "binder-button", "sidebar-nav-bs"]
html_sidebars = {
    "index": ["navbar-logo", "search-field"],
    "get_started/*": html_sidebar_default,
    "series/**": html_sidebar_binder,
    "workshops/*": html_sidebar_binder,
    "people": html_sidebar_default,
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_logo = "_static/images/logo.png"

html_theme_options = {
    "external_links": [
        {
            "url": "https://datalab.ucdavis.edu/davis-python-users-group/",
            "name": "DataLab",
        }
    ],
    "icon_links": [
        {
            "name": "github",
            "url": "https://github.com/criddler/dpug",
            "icon": "fab fa-github",
        }
    ],
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_start": ["project-title"],
    "footer_items": ["copyright", "sphinx-version"],
}


html_context = {
    "github_user": "criddler",
    "github_repo": "dpug",
    "github_version": "main",
    "doc_path": "unconverted",
    # For use binder button in "_templates/binder-button.html"
    "binder_url": "https://mybinder.org/v2/gh",
    "binder_branch": "participant",
    "edit_page_url_template": "https://github.com/{{ github_user }}/"
    + "{{ github_repo }}/edit/{{ github_version }}"  # noqa: W503
    + "/{{ doc_path }}{{ file_name.replace('.rst', '.md') }}",  # noqa: W503
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/custom.css", "css/theme.css", "css/ansi.css"]
html_copy_source = False

# Bootstrap is included in the theme already
panels_add_bootstrap_css = False
