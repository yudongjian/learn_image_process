import torch
import pandas as pd
import datetime
import numpy as np
from sklearn import preprocessing

temp_df = pd.read_csv('temps.csv')
print(temp_df.head())

years = temp_df['year']
months = temp_df['month']
days = temp_df['day']

dates = [str(year) + '-' + str(month) + '-' + str(day) for year, month, day in zip(years, months, days)]

dates = [datetime.datetime.strptime(i, '%Y-%m-%d') for i in dates]
print(dates)

# 把数据转化为可以构建成网络模型的数据（独热编码）
# 这里是把字符串星期几 转化为 标签值
#
features = pd.get_dummies(temp_df)
print(features.head(5))

labels = np.array(features['actual'])
features = features.drop('actual', axis=1)

# 对数据进行标准化, sklearn.preprocessing 包提供了几个常用的实用函数和转换器类
# fit_transform是fit和transform的组合，既包括了训练又包含了转换。
input_features = preprocessing.StandardScaler().fit_transform(features)
print(input_features[0])

# 输入 和 实际值
x = torch.tensor(input_features, dtype=float)
y = torch.tensor(labels, dtype=float)

#
weights = torch.randn((14, 128), dtype=float, requires_grad=True)
biases = torch.randn(128, dtype=float, requires_grad=True)

# 回归任务
weights2 = torch.randn((128, 1), dtype=float, requires_grad=True)
biases2 = torch.randn(1, dtype=float, requires_grad=True)

learn_rate = 0.001
losses = []

for i in range(1000):

    # 计算隐层
    hidden = x.mm(weights) + biases
    # 激活函数，非线性变化
    hidden = torch.relu_(hidden)
    # 预测结果
    pre_data = hidden.mm(weights2) + biases2

    # 计算损失
    loss = torch.mean((pre_data - y) ** 2)
    losses.append(loss.data.numpy())

    if i % 100 == 0:
        print('loss:  ', loss)

    # 反向传播   更新参数
    loss.backward()

    weights.data.add_(-learn_rate * weights.grad.data)
    biases.data.add_(-learn_rate * biases.grad.data)
    weights2.data.add_(-learn_rate * weights2.grad.data)
    biases2.data.add_(-learn_rate * biases2.grad.data)

    weights.grad.data.zero_()
    biases.grad.data.zero_()
    weights2.grad.data.zero_()
    biases2.grad.data.zero_()
