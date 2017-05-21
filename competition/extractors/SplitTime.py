from competition.extractors.base import BaseExtractor
import pandas as pd
import os
class SplitTime(BaseExtractor):
    def get_train(self,raw_data):
        self.init(raw_data)
        X,y = self._get(self.raw_data.store['train'])
        X = self.merge_tables(X)
        return X,y

    def get_test(self,raw_data):
        self.init(raw_data)
        X,y = self._get(self.raw_data.store['test'])
        X = self.merge_tables(X)
        return X,y

    def _get(self,dataframe,timelimit=None):
        X = dataframe[self.raw_data.common_feat]
        y = dataframe[self.raw_data.label_name]
        if timelimit:
            idx = X['clickTime']<timelimit
            X=X[idx]
            y=y[idx]
            
        def split_time(tm):
            day=(tm//10000)%7
            hour = (tm%10000)//100
            minute = (tm%100)
            return (day,minute,hour)
        df = X
        df2 = df.apply(lambda row: split_time(row['clickTime']), axis=1)
        df['clickDay'],df['clickHour'],df['clickMin']=zip(*df2)
        del df['clickTime']
        return df,y

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

# must provide extractor and extractor_name
extractor = SplitTime()
extractor_name = SplitTime.__name__