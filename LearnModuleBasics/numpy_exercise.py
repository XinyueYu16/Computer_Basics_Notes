#encoding: utf-8
'''
习题来源：
1. LintCode人工智能学习：https://www.lintcode.com/learn/
'''

import numpy as np

'''
np.array 和 np.ndarray 的区别: 结果一样

ndarray是一个类，np.ndarray()其实是它的构造函数，得到一个 ndarray 对象，而 array() 其实是为了便于创建一个 ndarray对象的函数。两者得到的结果其实是一样的。
np.ndarray()构造函数相对更麻烦也更低级一些，使用默认构造函数创建的ndarray对象的数组元素是随机值，
而 numpy提供了一系列的创建 ndarray对象的函数，array()就是其中的一种；使用来构造ndarray对象会更方便一些。

ndarray参数： np.ndarray( shape=, dtype=, buffer= , offset=, order=) 
- buffer： 用于初始化数组的buffer，通常是一个array
- order: 'C':行优先；'F':列优先

array参数：np.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
'''

array = np.array([np.random.randint(1, 10, 3), np.random.randint(1, 10, 3)])
array_nd = np.ndarray(shape = (2, 3), buffer = np.array(range(0, 7)), offset = 0, dtype= int) # ndarray在生成时只能指定大小和buffer


'''
np.dtype

可以设定复合数据结构
'''
rgba_type = np.dtype([('r', 'int'), ('g', 'int'), ('b', 'int'), ('a', 'int')])
rgba_ex = np.array([(255,255,255,1)], dtype = rgba_type)
print(rgba_ex.dtype)


'''
创建array

- np.ndarray
- np.array
- np.empty：未初始化array，显示随机值
- np.zeros：初始化为0
- np.ones：初始化为1
- np.ones_like：取传入np的shape，填充为1
- np.arrange
- np.random.randint
- np.tile: 重复输入的ndarray, 
    reps为1维的时候，np.array里面的每个list进行广播,
    reps为2维的时候，则reps的第二位表示列复制，第一位表示行复制,
    reps为3+维的时候，则reps的最后一位表示列复制，倒数第二位表示行复制, 倒数第三位及之前表示维度复制
    执行顺序从后往前 (..., 维度, 行, 列)
- ...

'''

'''
创建8x8棋盘 matrix
'''
np_init = np.zeros(shape = (8,8 ))
def create_matrix1() -> np.ndarray:
    """
        :return: Return an 8x8 chess board matrix
        """
    # -- write your code here --
    np_init = np.zeros(shape = (8,8), dtype = int)
    for i in range(0, len(np_init), 2):
        np_init[i, range(1, len(np_init), 2)] = 1
    for i in range(1, len(np_init), 2):
        np_init[i, range(0, len(np_init), 2)] = 1
    return np_init

def create_matrix2() -> np.ndarray:
    matrix = np.ones((8,8),dtype=int)
    matrix[::2,::2] = 0
    matrix[1::2,1::2] = 0
    return matrix

def create_matrix3() -> np.ndarray:
    '''
    np.tile example:

    np.tile(np.array([[0, 1], [1, 0]]),  (4, 2))
    array([[0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]])


    np.tile(np.array([[0, 1], [1, 0]]), (3, 1))
    array([[0, 1],
       [1, 0],
       [0, 1],
       [1, 0],
       [0, 1],
       [1, 0]])
    
    '''
    return np.tile(np.array([[0,1], [1, 0]], reps = (4,4)))

def create_matrix4() -> np.ndarray:
    # 根据位置index
    df1 = np.arange(0,8)
    df2 = np.arange(1,9)
    df3 =df1%2
    df4 =df2%2
    df5 =np.array([df3,df4,df3,df4,df3,df4,df3,df4])
    return df5


'''
np array 变形
'''
mat_o = np.array(np.arange(0, 35)).reshape(5, -1)
# reshape第一个参数为行(必须可被整除)，第二个参数为-1可以自动计算整除后每行的长度，但是当第一个参数不能被整除时，不可使用-1
# reshape要求新旧数组元素一致，resize则不，会按照顺序提取或填充
arr = np.arange(6).reshape(2,3)
new_arr = np.resize(arr, (3,2))
print(new_arr)
new_arr = np.resize(arr, (3,3))
print(new_arr)
new_arr = np.resize(arr, (2,2))
print(new_arr)

print(mat_o[:, 1])
print(mat_o[1, :])
# 切片取数和dataframe的规则一致


'''
numpy random 切片和索引

切片：取出ndarray的视图，对视图赋值的时候也会修改原始ndarray
索引：通过布尔索引/数组索引取数，不改变原始ndarray
'''
# 切片
s = np.arange(12)
slice_ = slice(2, 8, 3)

# 下标
print(s[slice_])
print(s[2:8:3])

# 数组索引, 形状会跟索引数组走
s_idx = np.arange(0, 10, 2)
print(s[s_idx])
s_idx = np.arange(0, 12, 2).reshape(2, -1)
print(s[s_idx])

# 布尔索引，形状会跟原始数据走
s = np.arange(35).reshape(5,7)
b = s > 21
b = b[:,3]
s[b]

# 花式索引

'''
numpy 添加数据或改变维度
- np.ndarray.flatten：摊平
- np.expand_dims: 只增加维度
- np.concatenate：不改变维度
- np.stack：维度+1，根据提供的axis进行堆叠
- np.append：不改变维度，沿给定轴append，默认摊平后水平增加
<-- 引用： https://www.lintcode.com/learn/123/343 -->

'''

# append
np.append(new_arr, [1, 1]) # 不添加axis时，默认展开水平增加
np.append(new_arr, np.expand_dims(np.array([1, 1]), axis= 0), axis = 0) # 制定axis时，append的array的其他axis必须有相同长度


'''
numpy 计算
- 数组与数组大小一致时：两两对应进行计算
- 数组与数组大小一致时：广播，“如果两个数组的后缘维度（trailing dimension，即从末尾开始算起的维度）的轴长度相符，或其中的一方的长度为1，则认为它们是广播兼容的”
    - 
'''

x = np.ones((4,3,5)) # 这里5为后缘维度
y = np.ones((4,1,3))
y1 = np.ones((4,1,1))
y2 = np.ones((1,1,5))
y3 = np.ones(1)
y4 = np.ones((1,1,3)) # x+y4会报错


'''
numpy random

random可以生成四种数据类型：
- 简单随机数
- 排列
- 分布
    - random.uniform: 均匀分布
    - random.normal：正态分布， 注意正态分布输入的参数是mean和std，之前误当成uniform了，做出来非常奇怪的数字
- 生成器
    - 生成器的随机由种子而定，默认根据系统时间，然而Windows和Linux系统的种子不一样（之前在项目里碰到过这种坑爹问题）

'''

from numpy import random
random.normal
random.uniform


