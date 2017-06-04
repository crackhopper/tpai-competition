# -*- coding:utf-8 -*-
from Base import BaseExtractor
import pandas as pd

class Merge(BaseExtractor):
  def __init__(self,store):
    app_categories = store['app_categories']
    new_app_categories = app_categories.copy()
    appCate1=app_categories['appCategory']//100
    appCate1.head()
    new_app_categories.insert(0,'appCate1',appCate1)
    appCate2=app_categories['appCategory']%100
    appCate2.head()
    new_app_categories.insert(0,'appCate2',appCate2)
    self.appFeature = new_app_categories

    def _aggfunc(x):
      if x.name == 'count':
        return x.count()
      elif x.name == 'appCate1':
        return x.value_counts().index[0]
    res = store['user']
    print 'concluding user_app_actions..'
    df = store['user_app_actions']
    df = pd.merge(df,new_app_categories,how='left',left_on='appID',right_on='appID')
    df['count']=df.index
    grouped = df.groupby('userID')['appCate1','count'].agg(_aggfunc)
    grouped=grouped.reset_index(level=['userID'])
    res = pd.merge(res,grouped,how='left',left_on='userID',right_on='userID')

    print 'concluding user_installedapps'
    df = store['user_installedapps']
    df = pd.merge(df,new_app_categories,how='left',left_on='appID',right_on='appID')
    df['count']=df.index
    grouped = df.groupby('userID')['appCate1','count'].agg(_aggfunc)
    grouped=grouped.reset_index(level=['userID'])
    res = pd.merge(res,grouped,how='left',left_on='userID',right_on='userID',suffixes=('_act', '_inst'))

    self.userFeature = res

    print 'conclude ad feature'
    res = store['ad']
    res = pd.merge(res,new_app_categories,how='left',left_on='appID',right_on='appID')
    self.adFeature = res

    print 'conclude pos feature'
    self.posFeature = store['position']

  def get_train(self,X,y,raw_data):
    return self._get(X,y,raw_data)

  def get_test(self,X,y,raw_data):
    return self._get(X,y,raw_data)

  def _get(self,X,y,raw_data):
    print 'merging features...'
    X = pd.merge(X,self.userFeature,how='left',left_on='userID',right_on='userID')
    X = pd.merge(X,self.adFeature,how='left',left_on='creativeID',right_on='creativeID')
    X = pd.merge(X,self.posFeature,how='left',left_on='positionID',right_on='positionID')
    return X,y,raw_data

