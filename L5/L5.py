import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
# nltk.download('punkt')

# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
# print(data)

# 将数据存放到transactions中
transactions = []
# 存储字典 key:value
item_count = {}
for i in range(data.shape[0]):
    temp = []
    for j in range(data.shape[1]):
        item = str(data.values[i, j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transactions.append(temp)
# print(transactions)
# print(item_count)

# 导入词云模块和自定义函数
from wordcloud import WordCloud


# 去掉停用词，即常用的虚词，口语等
def remove_stop_words(f):
    stop_words = []
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


def create_word_cloud(f):
    f = remove_stop_words(f)
    cut_text = word_tokenize(f)
    cut_text = " ".join(cut_text)
    wc = WordCloud(
        max_words=100,
        width=2000,
        height=1200,
    )
    wordcloud = wc.generate(cut_text)
    wordcloud.to_file("wordcloud.jpg")


# 生成词云
all_word = ''.join('%s' % item for item in transactions)
# print(all_word)
create_word_cloud(all_word)

# Top10商品是哪些
item_count_sorted = sorted(item_count.items(), key=lambda x:x[1], reverse=True)
print('Top 10 items & counts are:', item_count_sorted[:10])
