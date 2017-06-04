import pandas as pd
import os
import numpy as np
import pickle
from config import *

def _makeDestDir(extractFile,estimator_name,para_name=''):
  destdir = os.path.join(resultDir,'%s-%s%s'%(extractFile,estimator_name,para_name))
  print 'destdir: %s'%(destdir)
  if not os.path.exists(destdir):
    os.mkdir(destdir)
  return destdir

def getSubmission(extractFile,estimator_name,para_name=''):
  destdir = _makeDestDir(extractFile,estimator_name,para_name)
  return pd.read_csv(os.path.join(destdir,'submission.csv'))

def saveModel(estimator,extractFile,estimator_name,para_name=''):
  destdir = _makeDestDir(extractFile,estimator_name,para_name)
  if os.path.exists(os.path.join(destdir,'model.pkl')):
    raise RuntimeError("%s exists"%os.path.join(destdir,'model.pkl'))
  with open(os.path.join(destdir,'model.pkl'),'wb') as f:
    pickle.dump(estimator,f)
  print 'modeled saved'

def loadModel(extractFile,estimator_name,para_name=''):
  destdir = _makeDestDir(extractFile,estimator_name,para_name)
  with open(os.path.join(destdir,'model.pkl'),'rb') as f:
    return pickle.load(f)

def predictResult(estimator,extractFile,estimator_name,para_name=''):
  curdir = os.getcwd()
  clf = estimator
  destdir = _makeDestDir(extractFile,estimator_name,para_name)
  try:
    print 'loading input from %s'%(extractFile)
    extracted = loadExtracted(extractFile)

    print 'checking if the result exists'
    os.chdir(destdir)
    fname = 'submission.csv'
    fnamezip = fname+'.zip'
    if os.path.exists(fname):
      raise RuntimeError("%s exsits, cannot overwrite"%fname)

    print 'predicting..'
    X_test = extracted['teX']
    testY = clf.predict(X_test)

    print 'saving..'
    with open(fname,'w') as f:
      f.write('instanceId,prob\n')
      for i,y in enumerate(testY):
        f.write('%d,%.6f\n'%(i+1,y))

    print 'zipping...'
    if os.path.exists(fnamezip):
      os.remove(fnamezip)
    os.system('zip %s %s'%(fnamezip,fname))

  except Exception,e:
    os.chdir(curdir)
    raise e
  os.chdir(curdir)
  print 'done'


def loadExtracted(fname):
  f=os.path.join(extractedDir,fname)
  return pd.HDFStore(f)

def loadCVStore():
  return pd.HDFStore(cvDB)

def getTrainAndVal(extractFile, cvKey):
  extracted = loadExtracted(extractFile)
  cvStore=loadCVStore()
  dfcv = cvStore[cvKey]
  cvSet = []
  for train_idx,val_idx in dfcv.as_matrix():
    trX = extracted['trX'].iloc[train_idx,:]
    trY = extracted['trY'].iloc[train_idx]
    valX = extracted['trX'].iloc[val_idx,:]
    valY = extracted['trY'].iloc[val_idx]
    cvSet.append([trX,trY,valX,valY])
  return cvSet

def loadDataStore():
  f=os.path.join(convertedDir,convertedFile)
  return pd.HDFStore(f)

def loadInfo():
  with open(os.path.join(convertedDir,convertedInfoFile),'rb') as f:
    info = pickle.load(f)
  return info


class AllData(object):
  pass

def loadAll():
  store = loadDataStore()
  info = loadInfo()

  # the key of train and test set should not be changed
  #----------- the following part need refactor when next competition (move to the `convert` module)
  train = store['train']
  test = store['test']

  train_feats = train.columns
  test_feats = test.columns
  label_name = 'label'
  common_feat = list(set(train_feats).intersection(set(test_feats)))
  common_feat.remove(label_name)
  #----------- end

  all_data = AllData()

  all_data.store = store
  all_data.info = info
  all_data.label_name = label_name
  all_data.common_feat = common_feat
  return all_data
