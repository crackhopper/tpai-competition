# -*- coding:utf-8 -*-
class SelectByClickTime(BaseExtractor):
  def __init__(self,timelimit):
    self.timelimit = timelimit

  def extract_train(self,X,y,raw_data):
    return self._extract(X,y,raw_data)

  def extract_test(self,X,y,raw_data):
    return X,y,raw_data

  def _extract(self,X,y,raw_data):
    idx = (X['clickTime']>=self.timelimit[0]) & (X['clickTime']<self.timelimit[1])
    X=X[idx]
    y=y[idx]
    return X,y,raw_data

