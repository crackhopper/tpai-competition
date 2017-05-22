from BaseExtractor import BaseExtractor
import pandas as pd

class Combine(BaseExtractor):
  def __init__(self,extractors):
    self.extractors = extractors

  def get_train(self,X,y,raw_data):
    for ex in self.extractors:
      X,y,raw_data = ex.get_train(X,y,raw_data)
    return X,y,raw_data

  def get_test(self,X,y,raw_data):
    for ex in self.extractors:
      X,y,raw_data = ex.get_test(X,y,raw_data)
    return X,y,raw_data

