# -*- coding:utf-8 -*-
class BaseExtractor(object):
  def get_train(self,raw_data):
    raise NotImplementedError

  def get_test(self,raw_data):
    raise NotImplementedError

