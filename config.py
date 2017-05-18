# -*- coding:utf-8 -*-

# Do not modify this file, and make your own config file in
# `cfg_extractor.py`. (which would not be tracked by git)

# This file is provided as a default configuration file.

# convert_data, load_data
dataDir = './_data/'
extractDir = './_extracted/'
resultDir = './_result/'

dataFile = 'store.db'
infoFile = 'info.pkl'

# extractor
from competition.extractors.raw import extractor,extractor_name

# models
from competition.models.impute_rf import estimator,estimator_name
tuned_parameters = [{},]

# other configs
bShuffle = True
bProb = False

# load custom config
import os
if os.path.exists('configCustom.py'):
  from configCustom import *


