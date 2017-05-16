from sklearn.base import BaseEstimator
import numpy as np

class Constant(BaseEstimator):
    def __init__(self,val=0):
        self.val = val
    def fit(self,X,y):
        return self
    def predict(self,X):
        return self.fit_predict(X)
    def fit_predict(self,X):
        N = X.shape[0]
        return np.ones([N])*self.val

estimator = Constant()
tuned_parameters = [{
        'val':[0,1],
},]
