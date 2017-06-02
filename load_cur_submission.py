from config2 import input_file,estimator_name,para_name
import pandas as pd
destdir = './_results/%s-%s%s/'%(input_file,estimator_name,para_name)
submission = pd.read_csv(destdir+'submission.csv')

