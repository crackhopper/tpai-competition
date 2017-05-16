# -*- coding:utf-8 -*-
import os
import numpy as np
from config import resultDir, estimator_name, extractor_name,bShuffle
from extracted import extracted
import pickle

destdir = './_results/%s-%s/'%(extractor_name,estimator_name)
with open(os.path.join(destdir,'model.pkl'),'rb') as f:
    clf = pickle.load(f)

curdir = os.getcwd()
os.chdir(destdir)

X_test = extracted['teX']

testY = clf.predict(X_test)
fname = 'submission.csv'
fnamezip = fname+'.zip'
with open(fname,'w') as f:
    f.write('instanceId,prob\n')
    for i,y in enumerate(testY):
        f.write('%d,%.2f\n'%(i+1,y))

if os.path.exists(fnamezip):
    os.remove(fnamezip)

os.system('zip %s %s'%(fnamezip,fname))
os.chdir(curdir)
print 'done'
