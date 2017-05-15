# -*- coding:utf-8 -*-
import pandas as pd
from ..config import *

extractDir = '../'+extractdir
db_user = pd.HDFStore(extractDir+userStoreFile)
db_ad = pd.HDFStore(extractDir+adStoreFile)
db_pos = pd.HDFStore(extractDir+posStoreFile)



