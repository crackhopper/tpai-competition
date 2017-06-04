from xgboost.sklearn import XGBModel
import os
bestPara = {'colsample_bylevel': 0.8,
 'max_depth': 5,
 'n_estimators': 50,
 'objective': 'binary:logistic',
 'subsample': 0.8}
estimator = XGBModel(**bestPara)
estimator_name = 'tune_1_xgb'