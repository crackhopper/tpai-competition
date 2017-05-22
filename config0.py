# -*- coding:utf-8 -*-
# This is the default configuration file for `run_0_convert_data.py`

dataDir = './_data/'
dataFile = 'store.db'
infoFile = 'info.pkl'

# load custom config
import os
if os.path.exists('config0_rc.py'):
  from config0_rc import *


