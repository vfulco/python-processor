# -*- coding: utf-8 -*-
import re
import os
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon'
]
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = '.rst'
master_doc = 'index'
project = u'processor'
copyright = u'2015, Alexander Artemenko'
version = release = re.findall(
    'version="(.*)"',
    open(os.path.join(os.path.dirname(__file__), '../setup.py')).read()
)[0]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd:
    # workaround for making build on read the docs pass
    # see issue https://github.com/rtfd/readthedocs.org/issues/1202
    html_theme = 'sphinx_rtd_theme'
else:
    import sphinx_py3doc_enhanced_theme
    html_theme = "sphinx_py3doc_enhanced_theme"
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
    html_theme_options = {
        'githuburl': 'https://github.com/svetlyak40wt/python-processor/'
    }


pygments_style = 'trac'
templates_path = ['.']
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
