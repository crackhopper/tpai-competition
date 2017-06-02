# -*- coding:utf-8 -*-
from config1 import *
import pandas as pd
import os

def loadFile(fname=extractFile):
  return pd.HDFStore(os.path.join(extractDir,fname))
