import numpy as np
from scipy.signal import argrelextrema

# 加载数据
data = np.load('./data_pr/data.npy')

# 找到所有波峰的索引
maxn = argrelextrema(data, np.greater)
# 找到所有波谷的索引
minn = argrelextrema(data, np.less)

# 输出波峰索引和对应的值
print("波峰索引和对应的值:")
for idx in maxn[0]:
    print(f"索引: {idx}, 值: {data[idx]}")

# 输出波谷索引和对应的值
print("\n波谷索引和对应的值:")
for idx in minn[0]:
    print(f"索引: {idx}, 值: {data[idx]}")