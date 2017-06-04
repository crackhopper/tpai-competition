# -*- coding:utf-8 -*-
# This is the default configuration file for `run_2_predict.py`

from competition.models.xgb import estimator,estimator_name
extracted_dir = './_extracted/'
input_file = 'first_two_day_cvr.db'
bShuffle = False
bProb = True

# load custom config
import os
if os.path.exists('config2_rc.py'):
  from config2_rc import *


