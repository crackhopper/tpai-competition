# -*- coding:utf-8 -*-
import pandas as pd
import os

def extract_features(extractor, filename, raw_data, X=None, y=None):
  print 'extracting features...'
  trainX,trainY = extractor.get_train(X,y,raw_data)
  testX,testY  = extractor.get_test(X,y,raw_data)

  fname = filename
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
  from config1 import *
  from data import raw_data
  extract_features(extractor,extractFile, store, raw_data)
