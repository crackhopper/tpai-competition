
from competition.extractors.Base import BaseExtractor
import pandas as pd
import numpy as np
import os

class AppCvr(BaseExtractor):
    def __init__(self,X,y):
        key = "appID"
        dfTrain = X.copy()
        dfTrain['label']=y.copy()
        self.dfCvr = dfTrain.groupby(key).apply(lambda df: np.mean(df["label"])).reset_index()
        self.dfCvr.columns=['appID','appCvr']

    def get_train(self,X,y,raw_data):
        return self._extract(X,y,raw_data)

    def get_test(self,X,y,raw_data):
        return self._extract(X,y,raw_data)

    def _extract(self,X,y,raw_data):
        newX = pd.merge(X,self.dfCvr,on='appID',how='left')
        return newX,y,raw_data