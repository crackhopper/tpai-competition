# -*- coding:utf-8 -*-
from featExtract import *
from featExtract.base import Preprocess,train_feat,test_feat,label_feat
import pandas as pd

common_feat = list(set(train_feat).intersection(set(test_feat)))
common_feat
def merge_tables(X):
    # user
    X = pd.merge(X,f_user,how='left',left_on='userID',right_on='userID')
    del X['userID']
    # ad
    X = pd.merge(X,f_ad,how='left',left_on='creativeID',right_on='creativeID')
    del X['creativeID']
    # pos
    X = pd.merge(X,f_pos,how='left',left_on='positionID',right_on='positionID')
    del X['positionID']

    return X

class SimpleFeatures(Preprocess):
    def __init__(self):
        self.common = list(set(train_feat).intersection(set(test_feat)))
        self.common.remove(label_feat)

    def get_train(self,dataframe):
        X,y = self._get(dataframe) 
        X = merge_tables(X)
        return X,y

    def get_test(self,dataframe):
        X,y = self._get(dataframe)
        return X,y

    def _get(self,dataframe):
        X = dataframe[self.common]
        y = dataframe[label_feat]
        return X,y

