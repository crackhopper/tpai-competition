# -*- coding:utf-8 -*-
# This is the default configuration file for `run_0_convert_data.py`
from competition.models.xgb import estimator,estimator_name
tuned_parameters = [{
    'xgb__colsample_bytree': [0.5],
    'xgb__gamma': [0],
    'xgb__learning_rate': [0.1],
    'xgb__max_depth': [3],
    'xgb__min_child_weight': [1],
    'xgb__objective': ['binary:logistic'],
    'xgb__subsample': [1]
},]
input_file = 'first_two_day_cvr.db'
para_name = '0'
bShuffle = False
bProb = True
# load custom config
import os
if os.path.exists('config2_rc.py'):
  from config2_rc import *


