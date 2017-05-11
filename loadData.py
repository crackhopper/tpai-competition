# -*- coding:utf-8 -*-
from config import *
import pandas as pd
import pickle
basedir = './'

store = pd.HDFStore(basedir+datadir+storefile)
with open(basedir+datadir+infofile,'rb') as f:
  file_info,field_info = pickle.load(f)

