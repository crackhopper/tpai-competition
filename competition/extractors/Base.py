# -*- coding:utf-8 -*-
import os
import pandas as pd
class BaseExtractor(object):
  def get_train(self,X,y,raw_data):
    # should return X,y,raw_data
    raise NotImplementedError

  def get_test(self,X,y,raw_data):
    # should return X,y,raw_data
    raise NotImplementedError

  def run(self,all_data,save_file):
    print 'extracting features...'
    trainX,trainY,_ = self.get_train(None,None,all_data)
    testX,testY,_  = self.get_test(None,None,all_data)
    fname = save_file
    if os.path.exists(fname):
      raise RuntimeError("%s exists"%fname)

    print 'saving features into %s'%fname
    extracted = pd.HDFStore(fname)
    extracted['trX']=trainX
    extracted['trY']=trainY
    extracted['teX']=testX
    extracted.close()
    print 'extracting features...done'

