# -*- coding:utf-8 -*-
from config import *
import pandas as pd
import os
import pickle
store = pd.HDFStore(os.path.join(dataDir,dataFile))
with open(os.path.join(dataDir,infoFile),'rb') as f:
  info = pickle.load(f)

# the key of train and test set should not be changed
train = store['train']
test = store['test']

train_feats = train.columns
test_feats = test.columns
label_name = 'label'
common_feat = list(set(train_feats).intersection(set(test_feats)))
common_feat.remove(label_name)
class RawData(object):
    pass
raw_data = RawData()
raw_data.store = store

# this two field is required by default extractor.
# ensure the train and test have common features.
raw_data.label_name = label_name
raw_data.common_feat = common_feat

