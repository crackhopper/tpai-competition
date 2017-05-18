# this is an example extractor, and you should develop your own according to the
# dataset.
from base import BaseExtractor
import os
import pandas as pd

class SimpleFeatures(BaseExtractor):
    def get_train(self,raw_data):
        self.init(raw_data)
        X,y = self._get(raw_data,raw_data.store['train'])
        X = self.merge_tables(X)
        return X,y

    def get_test(self,raw_data):
        self.init(raw_data)
        X,y = self._get(raw_data,raw_data.store['test'])
        X = self.merge_tables(X)
        return X,y

    def init(self, raw_data):
        if hasattr(self,'bInit'):
            return
        self.raw_data = raw_data
        store = raw_data.store
        f_user = store['feat-user-default']
        f_ad = store['feat-ad-default']
        f_pos = store['position']
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
        self.merge_tables = merge_tables
        self.bInit=True

    def _get(self,raw_data,dataframe):
        X = dataframe[raw_data.common_feat]
        y = dataframe[raw_data.label_name]
        return X,y

# must provide extractor and extractor_name
extractor = SimpleFeatures()
extractor_name = SimpleFeatures.__name__
