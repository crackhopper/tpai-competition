# -*- coding:utf-8 -*-
# This is the default configuration file for `run_1_extract_features.py`

# default config
from competition.extractors import *
extractDir = './_extracted/'
extractFile = 'clickTimeConverted.db'
extractor = Combine([Raw(),ConvertClickTime()])

# load custom config
import os
if os.path.exists('config1_rc.py'):
  from config1_rc import *

