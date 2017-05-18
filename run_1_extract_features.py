# -*- coding:utf-8 -*-
import pandas as pd
from data import store,  raw_data
from config import *
import os

prep = Extractor(raw_data)
trainX,trainY = prep.get_train()
testX,testY  = prep.get_test()

fname = './_extracted/%s.db'%extractor_name
if os.path.exists(fname):
  raise RuntimeError("%s exists"%s)

extracted = pd.HDFStore(fname)
extracted['trX']=trainX
extracted['trY']=trainY
extracted['teX']=testX
extracted.close()
