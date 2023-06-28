# -*- coding: utf-8 -*-
#
# English Language RTD & Sphinx config file
#
# Uses ../conf_common.py for most non-language-specific settings.

# Importing conf_common adds all the non-language-specific
# parts to this conf module
import sys, os
sys.path.insert(0, os.path.abspath('../'))
from conf_common import *

# General information about the project.
project = u'ESP-IoT-Solution'
copyright = u'2016 - 2022, Espressif Systems (Shanghai) CO., LTD'
pdf_title = u'ESP-IoT-Solution User Guide'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'ReadtheDocsTemplate.tex', u'ESP-IoT-Solution',
   u'2016 - 2022, Espressif Systems (Shanghai) CO., LTD', 'manual'),
]
