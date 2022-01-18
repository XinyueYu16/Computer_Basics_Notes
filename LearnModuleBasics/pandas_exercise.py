#encoding: utf-8
'''
习题来源：
1. LintCode人工智能学习：https://www.lintcode.com/learn/
'''

import pandas as pd
import numpy as np

'''
Multi-Indexing:
df[] 切片直接引用列名，若列名为list则该列index的等级必须相同
df.loc[,] 索引查找行名，若行为list则该列index的等级必须相同，逗号后可引用列名，要求同上
当想要下钻到下一层index时，必须在先创建只有该层index的df
# 但即使是Multi-Indexing如下，ndim依然为2
'''

def generate_mutiindex_example():
    data = np.random.randint(10, 20, (6, 9))  # [10， 20)之间的随机整数
    index = [["first", "first", "second", "second", "third", "third"], ["male", "female", "male", "female", "male", "female"]]
    columns = [["Ch", "Ch", "Ch", "Ma", "Ma", "Ma", "En", "En", "En"], ["A", "B", "C", "A", "B", "C", "A", "B", "C"]]
    df = pd.DataFrame(data, index=index, columns=columns)
    return df

def layers_index():
    """
    获取二班数学A等学生的数量

    :param data: the source data
    :return: return a Series
    """
    # -- write your code here --
    data = generate_mutiindex_example()
    return data.loc["second", "Ma"]["A"]

