# -*- coding:utf-8 -*-
from model import destdir,clf
from extracted import extracted
import os

curdir = os.getcwd()
os.chdir(destdir)

X_test = extracted['teX']

testY = clf.predict(X_test)
fname = 'submission.csv'
fnamezip = fname+'.zip'
if os.path.exists(fname):
    raise RuntimeError("%s exsits, cannot overwrite"%fname)
with open(fname,'w') as f:
    f.write('instanceId,prob\n')
    for i,y in enumerate(testY):
        f.write('%d,%.2f\n'%(i+1,y))

if os.path.exists(fnamezip):
    os.remove(fnamezip)

os.system('zip %s %s'%(fnamezip,fname))
os.chdir(curdir)
print 'done'
