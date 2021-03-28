import pandas as pd
train = pd.read_csv('./train.csv')
# print(train)
# 将日期格式转化为pandas格式
train['Datetime'] = pd.to_datetime(train['Datetime'])
# 将列Datetime作为index
train.index = train['Datetime']
# 去除多余的ID、Datetime两列
train.drop(['ID', 'Datetime'], axis=1, inplace=True)
# 以天为单位进行采样
daily_train = train.resample('D').sum()
# print(daily_train)
daily_train['ds'] = daily_train.index
daily_train['y'] = daily_train['Count']
daily_train.drop(['Count'], axis=1, inplace=True)
# print(daily_train)
from fbprophet import Prophet
# 创建模型
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
m.fit(daily_train)
# 预测未来7个月，213天
future = m.make_future_dataframe(periods=213)
forecast = m.predict(future)
m.plot_components(forecast).savefig('1.png')