# -*- coding:utf-8 -*-
from Base import BaseExtractor
import pandas as pd

class Raw(BaseExtractor):
  def get_train(self,X,y,raw_data):
    return self._get(raw_data,'train')

  def get_test(self,X,y,raw_data):
    return self._get(raw_data,'test')

  def _get(self,raw_data,key):
    dataframe = raw_data.store[key]
    X = dataframe[raw_data.common_feat]
    y = dataframe[raw_data.label_name]
    return X,y,raw_data

