# 基础版本

[Datamap教程](https://www.datacamp.com/community/tutorials/decorators-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=aud-392016246653:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9040307&gclid=EAIaIQobChMI2LzVjbWS9AIV-JNmAh0huAGfEAAYASAAEgIfRvD_BwE)

```python
def decorator_maker_with_arguments(decarg1, decarg2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(funcarg1, funcarg2):
            print('decorator args:' , decarg1, decarg2)
            return func(funcarg1, funcarg2)
        return wrapper
    return decorator


@decorator_maker_with_arguments(decarg1, decarg2)
def func(funcarg1, funcarg2):
    return 
```



**解释：**

可以wrap几层：

1. decorator_maker: decorator需要的parameter --> decorator
2. decorator: 需要被decorate的function --> wrapper
3. wrapper: function需要的parameter --> function
4. function_to_be_decorated  -- function return

另外：

1. function_to_be_decorated被定义的地方@的是decorator_maker, 那么decorator的parameter并不能灵活更改？；
2. 所有跟function执行有关的语句都要放在wrapper里；
3. @functools.wraps(func)放在wrapper外



# 进阶版本

1. **[dispatch](http://hackwrite.com/posts/learn-about-python-decorators-by-writing-a-function-dispatcher/)**
   - 通过dispatch相关装饰器如 *@functools.singledispatch*，将@patcher.register(param) 作为装饰器装饰对应func，并call func: patcher(param)运行其对应代码
   - 高级if_else
   - 本质还是可以用decorator外的decorator取参函数 + ifelse 实现，就是写起来很重

