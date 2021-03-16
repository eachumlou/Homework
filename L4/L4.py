import pandas as pd
# 数据加载
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
pd.set_option('max_columns', None) # 设置pd显示格式：完全显示列
# print(dataset)
# print(dataset.shape) # 7501, 20

# 数据处理、清洗
transactions = []
# 按照行进行遍历
for i in range(0, dataset.shape[0]):
    # 创建空的临时列表，构建每一行组成的transaction
    temp = []
    # 按照列进行遍历
    for j in range(0, dataset.shape[1]):
        if str(dataset.values[i, j]) != 'nan':
            temp.append(dataset.values[i, j])
        # print(temp)
    transactions.append(temp)
    # print(transaction)

# 使用Apriori算法做关联分析
from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.35)
print('频繁项集：', itemsets)
print('关联规则：', rules)
