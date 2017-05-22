from BaseExtractor import BaseExtractor
import pandas as pd
import os
class ConvertClickTime(BaseExtractor):
  def get_train(self,X,y,raw_data):
    return self._get(X,y,raw_data)

  def get_test(self,X,y,raw_data):
    return self._get(X,y,raw_data)

  def _get(self,X,y,raw_data):
    def split_time(tm):
      day=(tm//10000)%7
      hour = (tm%10000)//100
      minute = (tm%100)
      return (day,minute,hour)
    df = X
    df2 = df.apply(lambda row: split_time(row['clickTime']), axis=1)
    df['clickDay'],df['clickHour'],df['clickMin']=zip(*df2)
    del df['clickTime']
    return df,y

