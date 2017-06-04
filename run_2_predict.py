# -*- coding:utf-8 -*-
import os
import numpy as np
import pandas as pd
import pickle
from config2 import *
from sklearn.metrics import classification_report
from competition.models import official_score

extracted = pd.HDFStore(os.path.join(extracted_dir,input_file))
destdir = './_results/%s-%s/'%(input_file,estimator_name)
if not os.path.exists(destdir):
    os.mkdir(destdir)
if os.path.exists(os.path.join(destdir,'model.pkl')):
    raise RuntimeError("%s exists"%os.path.join(destdir,'model.pkl'))

X_train = extracted['trX']
y_train = extracted['trY']
X_test = extracted['teX']

if bShuffle:
    N = X_train.shape[0]
    idx = np.random.permutation(N)
    X_train = X_train.iloc[idx,:]
    y_train = y_train.as_matrix()[idx]

score = official_score

print "fit with full data"
clf = estimator
clf.fit(X_train, y_train)

if bProb:
    print 'output probability, no classification report yet'
else:
    y_true, y_pred = y_train, clf.predict(X_train)
    print classification_report(y_true, y_pred)

print -official_score(clf,X_train,y_train)

with open(os.path.join(destdir,'model.pkl'),'wb') as f:
    pickle.dump(clf,f)

### saving the result
print 'predicting....'
curdir = os.getcwd()
os.chdir(destdir)

X_test = extracted['teX']
testY = clf.predict(X_test)
fname = 'submission.csv'
fnamezip = fname+'.zip'

try:
    if os.path.exists(fname):
        os.chdir(curdir)
        raise RuntimeError("%s exsits, cannot overwrite"%fname)
except Exception,e:
    os.chdir(curdir)
    raise e

with open(fname,'w') as f:
    f.write('instanceId,prob\n')
    for i,y in enumerate(testY):
        f.write('%d,%.6f\n'%(i+1,y))

if os.path.exists(fnamezip):
    os.remove(fnamezip)

os.system('zip %s %s'%(fnamezip,fname))
os.chdir(curdir)
print 'done'
extracted.close()
