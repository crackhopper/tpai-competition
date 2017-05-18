# -*- coding:utf-8 -*-
import pandas as pd
import os

def extract_features(extractor,extractor_name,store, raw_data):
  print 'extracting features...'
  trainX,trainY = extractor.get_train(raw_data)
  testX,testY  = extractor.get_test(raw_data)

  fname = './_extracted/%s.db'%extractor_name
  if os.path.exists(fname):
    raise RuntimeError("%s exists"%fname)

  print 'saving features into %s'%fname
  extracted = pd.HDFStore(fname)
  extracted['trX']=trainX
  extracted['trY']=trainY
  extracted['teX']=testX
  extracted.close()
  print 'extracting features...done'

if __name__ == '__main__':
  from config import *
  from data import store,  raw_data
  extract_features(extractor,extractor_name, store, raw_data)
