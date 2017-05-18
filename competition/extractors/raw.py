# -*- coding:utf-8 -*-
from competition.featExtract.base import BaseExtractor
import pandas as pd

class Raw(BaseExtractor):
  def get_train(self,raw_data):
    X,y = self._get(raw_data,raw_data.store['train'])
    return X,y

  def get_test(self,raw_data):
    X,y = self._get(raw_data,raw_data.store['test'])
    return X,y

  def _get(self,raw_data,dataframe):
    X = dataframe[raw_data.common_feat]
    y = dataframe[raw_data.label_name]
    return X,y

# must provide extractor and extractor_name
extractor = Raw()
extractor_name = Raw.__name__
