
train_feat = [u'label', u'clickTime', u'conversionTime', u'creativeID', u'userID',
       u'positionID', u'connectionType', u'telecomsOperator']

test_feat = [u'instanceID', u'label', u'clickTime', u'creativeID', u'userID',
       u'positionID', u'connectionType', u'telecomsOperator']

label_feat = u'label'

class Preprocess(object):
  def get_train(self,dataframe):
    raise NotImplementedError

  def get_test(self,dataframe):
    raise NotImplementedError

