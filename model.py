# -*- coding:utf-8 -*-
import os
import numpy as np
from config import resultDir, estimator_name, extractor_name,bShuffle
from extracted import extracted
import pickle

destdir = './_results/%s-%s/'%(extractor_name,estimator_name)
with open(os.path.join(destdir,'model.pkl'),'rb') as f:
    clf = pickle.load(f)