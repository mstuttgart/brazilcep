# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import logging
import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

sys.path.insert(0, os.path.abspath("../../"))

import brazilcep

# -- Project information -----------------------------------------------------

project = "BrazilCEP"
copyright = f"{datetime.today().year}, Michell Stuttgart"
author = "Michell Stuttgart"
version = brazilcep.__version__
release = brazilcep.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.doctest",
    "sphinx_copybutton",
    "sphinx_autodoc_typehints",
]

# Tell myst-parser to assign header anchors for h1-h3.
myst_heading_anchors = 3

# suppress_warnings = ["myst.header"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

source_suffix = [".rst", ".md"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    # Uncomment these if you use them in your codebase:
    #  "torch": ("https://pytorch.org/docs/stable", None),
    #  "datasets": ("https://huggingface.co/docs/datasets/master/en", None),
    #  "transformers": ("https://huggingface.co/docs/transformers/master/en", None),
}

# By default, sort documented members by type within classes and modules.
autodoc_member_order = "groupwise"

# Include default values when documenting parameter types.
typehints_defaults = "comma"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

html_title = f"brazilcep v{brazilcep.__version__}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_css_files = ["css/custom.css"]

html_favicon = "_static/favicon.ico"

html_theme_options = {
    "logo": "logo.png",
    "show_powered_by": False,
    "github_user": "mstuttgart",
    "github_repo": "brazilcep",
    "github_banner": True,
    "show_related": False,
    "note_bg": "#FFF59C",
}

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    # "index": ["sidebar-intro.html"],
    "**": [
        'sidebar-intro.html', 
        'globaltoc.html', 
        'sidebar-links.html', 
        'searchbox.html',
    ],
}

# -- Hack to get rid of stupid warnings from sphinx_autodoc_typehints --------


class ShutupSphinxAutodocTypehintsFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if "Cannot resolve forward reference" in record.msg:
            return False
        return True


logging.getLogger("sphinx.sphinx_autodoc_typehints").addFilter(ShutupSphinxAutodocTypehintsFilter())
