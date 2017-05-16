from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.ensemble import RandomForestClassifier

estimators = [('impute', Imputer(missing_values='NaN', strategy='most_frequent', axis=0)),
              ('clf', RandomForestClassifier())]

estimator = Pipeline(estimators)

tuned_parameters = [{
        'impute__copy':[False],
        'clf__n_estimators': [10],
        'clf__min_samples_split':[2],
        'clf__min_samples_leaf':[1],
        'clf__min_weight_fraction_leaf':[0],
        'clf__max_leaf_nodes':[None],
        'clf__min_impurity_split':[1e-7],
        'clf__warm_start':[False],
        'clf__oob_score':[False],
        'clf__class_weight':['balanced']
},]
