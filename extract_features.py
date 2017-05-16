# -*- coding:utf-8 -*-
import pandas as pd
from data import store,  raw_data
from config import *

prep = Extractor(raw_data)
trainX,trainY = prep.get_train()
testX,testY  = prep.get_train()

extracted = pd.HDFStore('./_extracted/%s.db'%extractor_name)
extracted['trX']=trainX
extracted['trY']=trainY
extracted['teX']=testX
extracted.close()
