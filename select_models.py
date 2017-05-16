# -*- coding:utf-8 -*-
import os
import numpy as np
from config import *
from extracted import extracted
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from competition.models import official_score
import numpy as np
import pickle

destdir = './_results/%s-%s/'%(extractor_name,estimator_name)
if not os.path.exists(destdir):
    os.mkdir(destdir)

X_train = extracted['trX']
y_train = extracted['trY']
X_test = extracted['teX']

bShuffle = True
if bShuffle:
    N = X_train.shape[0]
    idx = np.random.permutation(N)
    X_train = X_train.as_matrix()[idx]
    y_train = y_train.as_matrix()[idx]

score = official_score

print "# Tuning hyper-parameters for %s" % score
clf = GridSearchCV(estimator, tuned_parameters, cv=5, scoring= score)

print "fitting"
clf.fit(X_train, y_train)

print "Best parameters set found on development set:",
print clf.best_params_
print "Grid scores on development set:"
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print "%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params),
print ''

print "Detailed classification report:"
print "The model is trained on the full development set."
print "The scores are computed on the full evaluation set."
y_true, y_pred = y_train, clf.predict(X_train)
print classification_report(y_true, y_pred)
print -official_score(clf,X_train,y_train)

with open(os.path.join(destdir,'model.pkl'),'wb') as f:
    pickle.dump(clf,f)
