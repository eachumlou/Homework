from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt

# 导入数据
data = pd.read_csv('car_data.csv', encoding = 'gbk')
train_x = data[['人均GDP', '城镇人口比重', '交通工具消费价格指数', '百户拥有汽车量']]

# 数据规范化到[0,1]的空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
# pd.DataFrame(train_x).to_csv('temp.csv', index=False)
# print(train_x)

# K-Means手肘法判断n_cluster的合适值
sse = []
for k in range(1,11):
    # KMeans算法
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    # 计算inertia簇内误差平方和
    sse.append(kmeans.inertia_)
x = range(1,11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x,sse,'o-')
plt.show()
# 取n_cluster=4

# 使用KMeans聚类
kmeans = KMeans(n_clusters=4)
predict_y = kmeans.fit_predict(train_x)
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0:u'聚类结果'}, axis=1, inplace=True)
result.sort_values(by='聚类结果', ascending=True, inplace=True)
pd.DataFrame(result).to_excel('result.xlsx', index=False)
print(result)


