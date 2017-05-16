# -*- coding:utf-8 -*-
from competition.featExtract.base import Extractor
import pandas as pd

class Raw(Extractor):
  def __init__(self, raw_data):
    self.raw_data = raw_data
  def get_train(self):
    X,y = self._get(self.raw_data.store['train'])
    return X,y

  def get_test(self):
    X,y = self._get(self.raw_data.store['test'])
    return X,y

  def _get(self,dataframe):
    X = dataframe[self.raw_data.common_feat]
    y = dataframe[self.raw_data.label_name]
    return X,y
