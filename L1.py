#Action1: 求2+4+6+8+...+100的和
sum = 0
number = 2
while number < 101:
    sum = sum + number
    number = number + 2
print('Sum=',sum)

#Action2: 统计全班成绩
import pandas as pd
data = pd.read_csv('.\score.csv', encoding='gbk')
print(data)
print('语文平均分=', pd.DataFrame.mean(data['语文']))
print('数学平均分=', pd.DataFrame.mean(data['数学']))
print('英语平均分=', pd.DataFrame.mean(data['英语']))
print('语文最低分=', pd.DataFrame.min(data['语文']))
print('数学最低分=', pd.DataFrame.min(data['数学']))
print('英语最低分=', pd.DataFrame.min(data['英语']))
print('语文最高分=', pd.DataFrame.max(data['语文']))
print('数学最高分=', pd.DataFrame.max(data['数学']))
print('英语最高分=', pd.DataFrame.max(data['英语']))
print('语文方差=', pd.DataFrame.var(data['语文']))
print('数学方差=', pd.DataFrame.var(data['数学']))
print('英语方差=', pd.DataFrame.var(data['英语']))
print('语文标准差=', pd.DataFrame.std(data['语文']))
print('数学标准差=', pd.DataFrame.std(data['数学']))
print('英语标准差=', pd.DataFrame.std(data['英语']))
data['总分'] = data.sum(axis=1)
print('按总分从高到低排列')
print(data.sort_values(by=['总分'], ascending=False))

#Action3: 汽车质量数据统计
df = pd.read_csv('.\car_data_analyze\car_complain.csv', encoding='utf-8')
df = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))
#df.to_csv('.\output.csv')
#print(df)
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x
df['brand'] = df['brand'].apply(f)
#print(df)
result = df.groupby(['brand'])['id'].agg(['count'])
result2 = df.groupby(['car_model'])['id'].agg(['count'])
print('品牌投诉总数')
print(result)
print('车型投诉总数')
print(result2)
#各品牌+车型的投诉数量
result3 = df.groupby(['brand','car_model'])['id'].agg(['count'])
#print(result3)
#品牌平均车型投诉排行，从高到低
result4 = result3.groupby(['brand'])['count'].mean().sort_values(ascending=False)
print('品牌平均车型投诉排行，从高到低')
print(result4)


