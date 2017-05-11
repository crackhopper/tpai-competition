from base import Preprocess,train_feat,test_feat,label_feat

class UseRawInput(Preprocess):
    def __init__(self):
        self.common = list(set(train_feat).intersection(set(test_feat)))
        self.common.remove(label_feat)

    def get_train(self,dataframe):
        return self._get(dataframe)

    def get_test(self,dataframe):
        return self._get(dataframe)

    def _get(self,dataframe):
        X = dataframe[self.common]
        y = dataframe[label_feat]
        return X,y
