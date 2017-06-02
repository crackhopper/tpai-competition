from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from xgboost.sklearn import XGBModel
from sklearn.ensemble import RandomForestClassifier
import os
estimators = [('xgb', XGBModel())]

estimator = Pipeline(estimators)
estimator_name = os.path.basename(__file__).split('.')[0]