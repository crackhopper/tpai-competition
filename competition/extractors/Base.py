# -*- coding:utf-8 -*-
class BaseExtractor(object):
  def get_train(self,X,y,raw_data):
    # should return X,y,raw_data
    raise NotImplementedError
  def get_test(self,X,y,raw_data):
    # should return X,y,raw_data
    raise NotImplementedError

