# -*- coding:utf-8 -*-

# define at you will
# this file is intended to be used by the scripts in this folder


# convert_data, load_data
dataDir = './_data/'
extractDir = './_extracted/'
resultDir = './_result/'

dataFile = 'store.db'
infoFile = 'info.pkl'

# extract_features
from competition.featExtract.simple_features import SimpleFeatures as Extractor
extractor_name = 'simple_features'

# build_model
from competition.models.impute_rf import estimator,tuned_parameters
estimator_name = 'impute_rf'

# other configs
bShuffle = True
