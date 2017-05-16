# -*- coding:utf-8 -*-

# Do not modify this file, and make your own config file in custom_config.py.
# (which would not be tracked by git)

# This file is provided as a default configuration file.

# convert_data, load_data
dataDir = './_data/'
extractDir = './_extracted/'
resultDir = './_result/'

dataFile = 'store.db'
infoFile = 'info.pkl'

# extract_features
from competition.featExtract.raw import Raw as Extractor
extractor_name = 'raw'

# build_model
from competition.models.impute_rf import estimator,tuned_parameters
estimator_name = 'impute_rf'

# other configs
bShuffle = True

import os
if os.path.exists('custom_config.py'):
  from custom_config import *


