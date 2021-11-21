# 基础版本

**测试思想：**

针对一个function的不同功能/不同情景进行测试，如不同的input type；

在test里面设计输入



**pytest版本**

Basically, 会运行一切test_开头的脚本，包括class与test。有时候同一个模块的不同功能/不同情景的实现会放进一个TestClassName的class里，全部通过才可以。

**unittest版本**

Class不需要以Test开头但需要包含test在里面，所有test class都需要继承unittest.TestCase

