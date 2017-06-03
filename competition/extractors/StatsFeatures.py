from competition.extractors.Base import BaseExtractor
import pandas as pd
import numpy as np
import os

def CvrStatisticsByKey(train_label,X,key):
    dfCvr = train_label.groupby(key).apply(lambda df: np.mean(df["label"])).reset_index()
    dfCvr.columns=[key,key+'Cvr']
    newX = pd.merge(X,dfCvr,on=key,how='left')
    return newX

def split_time(tm):
    day=(tm//10000)%7
    hour = (tm%10000)//100
    minute = (tm%100)
    return (day,minute,hour)

def convertTime(df):
    timeInfo = df.apply(lambda row: split_time(row['clickTime']), axis=1)
    df['clickDay'],df['clickHour'],df['clickMin']=zip(*timeInfo)
    return df

def stats_extract(X,y,raw_data,dfTrain):
    newX = convertTime(X)
    newX = X
    newX = CvrStatisticsByKey(dfTrain,newX,'appID')
    newX = CvrStatisticsByKey(dfTrain,newX,'positionID')
    newX = CvrStatisticsByKey(dfTrain,newX,'connectionType')
    newX = CvrStatisticsByKey(dfTrain,newX,'camgaignID')
    newX = CvrStatisticsByKey(dfTrain,newX,'count_act')
    newX = CvrStatisticsByKey(dfTrain,newX,'clickDay')
    del newX['clickTime']
    del newX['appID']
    return newX,y,raw_data

class StatsFeatures(BaseExtractor):
    def __init__(self,X,y):
        self.dfTrain = convertTime(X.copy())
        self.dfTrain['label']=y.copy()

    def get_train(self,X,y,raw_data):
        return self._extract(X,y,raw_data)

    def get_test(self,X,y,raw_data):
        return self._extract(X,y,raw_data)

    def _extract(self,X,y,raw_data):
        return stats_extract(X,y,raw_data,self.dfTrain)