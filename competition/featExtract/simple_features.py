
from competition.featExtract.base import Extractor
import pandas as pd



class SimpleFeatures(Extractor):
    def __init__(self, raw_data):
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

    def get_train(self):
        X,y = self._get(self.raw_data.store['train']) 
        X = self.merge_tables(X)
        return X,y

    def get_test(self,dataframe):
        X,y = self._get(self.raw_data.store['test']) 
        X = self.merge_tables(X)
        return X,y

    def _get(self,dataframe):
        X = dataframe[self.raw_data.common_feat]
        y = dataframe[self.raw_data.label_name]
        return X,y