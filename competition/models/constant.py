from sklearn.base import BaseEstimator
import numpy as np

class Constant(BaseEstimator):
    def __init__(self,val=0):
        self.val = val
    def fit(self,X,y):
        return self
    def predict(self,X):
        return self.fit_predict(X)

# must provide extractor and extractor_name
extractor = Constant()
extractor_name = Constant.__name__
