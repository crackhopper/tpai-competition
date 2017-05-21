# -*- coding:utf-8 -*-
from config import *
import pandas as pd
import os
extracted = pd.HDFStore(os.path.join(extractDir,'%s.db'%extractor_name))

def load_extract_by_name(name):
  return pd.HDFStore(os.path.join(extractDir,'%s.db'%name))
