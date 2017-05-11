# -*- coding:utf-8 -*-
from config import *
import pandas as pd
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

info = {
  'user':{
    'userID':'用户ID',
    'age':'年龄：取值范围[0, 80]，其中0表示未知。',
    'gender':'性别：取值包括男，女，未知。',
    'education':'学历：取值包括小学，初中，高中，专科，本科，硕士，博士，未知',
    'marriageStatus':'婚恋状态：取值包括单身，新婚，已婚，未知。',
    'haveBaby':'育儿状态：取值包括孕育中，宝宝0~6个月，宝宝6~12个月，宝宝1~2岁，宝宝2~3岁，育儿但宝宝年龄未知，未知。',
    'hometown':'籍贯：千位百位数表示省份，十位个位数表示省内城市。如1806表示省份编号为18，城市编号是省内的6号，编号0表示未知。',
    'residence':'常住地：编码方式与家乡相同',
  },
  'user_installedapps':{
    'userID':'用户ID',
    'appID':'截止到某一时间点用户安装的App(appID)，已过滤高频和低频App。'
  },
  'user_app_actions':{
    'userID':'用户ID',
    'installTime':'安装时间',
    'appID':'appid',
  },
  'app_categories':{
    'appID':'广告推广的目标,i.e.,具体的App。多个推广计划或广告可以同时推广同一个App。',
    'appCategory':'App类目标签:3位数字编码，百位数表示一级类目，十位个位数表示二级类目;类目未知或者无法获取时，标记为0',
  },
  'ad':{
    'creativeID':'展示给用户直接看到的广告内容，一条广告下可以有多组素材。',
    'adID':'广告ID',
    'campaignID':'推广计划是广告的集合，广告主可以将条件相同的广告放在同一个推广计划中，方便管理。',
    'advertiserID':'一家特定的广告主',
    'appID':'广告推广的目标,i.e.,具体的App。多个推广计划或广告可以同时推广同一个App。',
    'appPlatform':'App所属操作系统平台，取值为Android，iOS，未知。同一个appID只会属于一个平台。',
  },
  'position':{
    'positionID':'广告位置id。',
    'sitesetID':'多个广告位的聚合，如QQ空间。注意：0不代表未知',
    'positionType':'对于某些站点，人工定义的一套广告位规格分类，如Banner广告位。',
  },
  'train':{
    'label':'取值0或1，其中0表示点击后没有发生转化，1表示点击后有发生转化',
    'clickTime':'格式均为DDHHMM，其中DD代表第几天，HH代表小时，MM代表分钟',
    'conversionTime':'当label=0时，conversionTime字段为空字符串。',
    'creativeID':'展示给用户直接看到的广告内容，一条广告下可以有多组素材。',
    'userID':'用户ID',
    'positionID':'广告位置id。',
    'connectionType':'移动设备当前使用的联网方式，取值包括2G，3G，4G，WIFI，未知',
    'telecomsOperator':'移动设备当前使用的运营商，取值包括中国移动，中国联通，中国电信，未知',
  },
  'test':{
    'instanceID':'样本标识',
    'label':'取值0或1，其中0表示点击后没有发生转化，1表示点击后有发生转化',
    'clickTime':'格式均为DDHHMM，其中DD代表第几天，HH代表小时，MM代表分钟',
    'creativeID':'展示给用户直接看到的广告内容，一条广告下可以有多组素材。',
    'userID':'用户ID',
    'positionID':'广告位置id。',
    'connectionType':'移动设备当前使用的联网方式，取值包括2G，3G，4G，WIFI，未知',
    'telecomsOperator':'移动设备当前使用的运营商，取值包括中国移动，中国联通，中国电信，未知',
  },
}

store = pd.HDFStore(datadir+storefile)
for n,s in file_tb.items():
  store[n]=pd.read_csv(datadir+n+'.csv')

store.flush(fsync=True)
store.close()

import pickle
with open(datadir+infofile,'wb') as f:
    pickle.dump([file_tb,info],f)
