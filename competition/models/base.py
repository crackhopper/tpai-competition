
from sklearn.base import BaseEstimator

class BaseModel(BaseEstimator): # compatible with sklearn
  def fit(self,X,y):
    raise NotImplementedError
  def predict(self,X):
    raise NotImplementedError
  def fit_predict(self,X):
    raise NotImplementedError
