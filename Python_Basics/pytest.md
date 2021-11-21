# 基础版本

**测试思想：**

- 针对一个function的不同功能/不同情景进行测试，如不同的input type

- 在test里面设计输入，及输入应该对应的输出（expected），并与运行待测试脚本后的（actual）进行断言对比 assert
- **在修改函数功能前，完成测试脚本，以确保修改后的函数与修改前的函数功能兼容**



**pytest版本**

- 会运行一切test_开头的脚本，包括class与test
- 一个TestClassName的class或test_function里的test需要全部通过

**unittest版本**

- Class不需要以Test开头但需要包含test在里面
- 所有test class都需要继承unittest.TestCase
- 有六种断言function（a..Equal, a..NotEqual, a..True, a..False, a..In, a..NotIn）

