# -*- coding:utf-8 -*-
from Base import BaseExtractor
import pandas as pd
import numpy as np

class Wrapper(BaseExtractor):
  def __init__(self,trX,trY,teX):
    self.trX = trX
    self.trY = trY
    self.teX = teX
    self.teY = pd.DataFrame(-1*np.ones([teX.shape[0],1]))

  def get_train(self,X,y,raw_data):
    return self.trX,self.trY,raw_data

  def get_test(self,X,y,raw_data):
    return self.teX,self.teY,raw_data


