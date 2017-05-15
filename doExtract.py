from loadData import store, file_info,field_info

from featExtract import *
import pandas as pd

Extractor = SimpleFeatures
Extractor_name = SimpleFeatures.__module__.__name__

prep = Extractor()

trainX,trainY = prep.get_train(store['train'])
testX,testY  = prep.get_train(store['test'])

extracted = pd.HDFStore('./_extracted/%s.db'%Extractor_name)
extracted['trX']=trainX
extracted['trY']=trainY
extracted['teX']=testX

extracted.close()
