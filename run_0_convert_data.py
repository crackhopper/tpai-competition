
# -*- coding:utf-8 -*-
import pandas as pd
from config import *
import os
import pickle

store = pd.HDFStore(os.path.join(dataDir,dataFile))
info = open(os.path.join(dataDir,infoFile),'wb')

# please re-write following codes for different competitions

####################################################################
################## load initial data
####################################################################
file_tb={
  'ad':'广告特征文件\n每行描述一条广告素材，各字段之间由逗号分隔，顺序依次为“creativeID，adID，camgaignID，advertiserID，appID，appPlatform”',
  'app_categories':'App特征文件\n每行代表一个App，各字段之间由逗号分隔，顺序依次为：“appID，appCategory”',
  'app_categories':'广告位特征文件\n每行描述一个广告位，各字段之间由逗号分隔，顺序依次为：“positionID，sitesetID，positionType”。',
  'user': '用户基础特征文件\n每行代表一个用户，各字段之间由逗号分隔，顺序依次为：“userID，age，gender，education，marriageStatus，haveBaby，hometown，residence”。',
  'user_app_actions':'用户App安装流水文件\n每行代表一个用户的单个App操作流水，各字段之间由逗号分隔，顺序依次为：“userID，installTime，appID”。\n特别的，我们提供了训练数据开始时间之前16天开始连续30天的操作流水，即第1天0点到第31天0点。',
  'user_installedapps':'用户App安装列表文件\n每行代表一个用户安装的单个App，各字段之间由逗号分隔，顺序依次为：“userID，appID”。\n特别的，我们提供了截止到第1天0点用户全部的App安装列表。',
  'position':'广告位特征文件\n每行描述一个广告位，各字段之间由逗号分隔，顺序依次为：“positionID，sitesetID，positionType”。',
  'train':'训练样本文件',
  'test':'测试样本文件',
}

pickle.dump(file_tb,info)

for n,s in file_tb.items():
    store[n]=pd.read_csv(dataDir+n+'.csv')
store.flush(fsync=True)


####################################################################
# merge some tables to get a better start point for feature engineer.
####################################################################

# process the app_categories table
app_categories = store['app_categories']
new_app_categories = app_categories.copy()
appCate1=app_categories['appCategory']//100
appCate1.head()
new_app_categories.insert(0,'appCate1',appCate1)
appCate2=app_categories['appCategory']%100
appCate2.head()
new_app_categories.insert(0,'appCate2',appCate2)

# extract user's feature
print "extract user's feature"

res = store['user']
df = store['user_app_actions']
df = pd.merge(df,new_app_categories,how='left',left_on='appID',right_on='appID')
df['count']=df.index

def _aggfunc(x):
    if x.name == 'count':
        return x.count()
    elif x.name == 'appCate1':
        return x.value_counts().index[0]
grouped = df.groupby('userID')['appCate1','count'].agg(_aggfunc)
grouped=grouped.reset_index(level=['userID'])
res = pd.merge(res,grouped,how='left',left_on='userID',right_on='userID')
df = store['user_installedapps']
df = pd.merge(df,new_app_categories,how='left',left_on='appID',right_on='appID')
df['count']=df.index
grouped = df.groupby('userID')['appCate1','count'].agg(_aggfunc)
grouped=grouped.reset_index(level=['userID'])
res = pd.merge(res,grouped,how='left',left_on='userID',right_on='userID',suffixes=('_act', '_inst'))

store['feat-user-default']=res

# extract ad feature
print 'extract ad feature'
res = store['ad']
res = pd.merge(res,new_app_categories,how='left',left_on='appID',right_on='appID')

store['feat-ad-default']=res

# extract pos feature
print 'extract pos feature'
res = store['pos']

store['feat-pos-default']=res

store.close()
info.close()