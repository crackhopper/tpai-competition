# -*- coding:utf-8 -*-
import pandas as pd
import os
from config1 import extractDir

def extract_features(extractor, filename, raw_data, X=None, y=None):
  print 'extracting features...'
  trainX,trainY,_ = extractor.get_train(X,y,raw_data)
  testX,testY,_  = extractor.get_test(X,y,raw_data)

  fname = os.path.join(extractDir,filename)
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
  extract_features(extractor,extractFile, raw_data)
