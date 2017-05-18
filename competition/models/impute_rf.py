from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier
import os
estimators = [('impute', Imputer(missing_values='NaN', strategy='most_frequent', axis=0)),
              ('clf', RandomForestClassifier())]

estimator = Pipeline(estimators)
estimator_name = os.path.basename(__file__).split('.')[0]
