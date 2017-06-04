from config2 import input_file,estimator_name
import pandas as pd
destdir = './_results/%s-%s/'%(input_file,estimator_name)
submission = pd.read_csv(destdir+'submission.csv')

