https://www.datacamp.com/community/tutorials/decorators-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034364&utm_targetid=aud-392016246653:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9040307&gclid=EAIaIQobChMI2LzVjbWS9AIV-JNmAh0huAGfEAAYASAAEgIfRvD_BwE



def decorator_maker_with_arguments(decarg1, decarg2): 
    def decorator(**func**):

​		 @functools.wraps(func)

​    	def wrapper(funcarg1, funcarg2):
​         	print('decorator args:' , decarg1, decarg2)

​         	return **func**(funcarg1, funcarg2)

​		return wrapper

​	return decorator



可以wrap几层：

1. decorator_maker: decorator需要的parameter
2. decorator: 需要被decorate的function
3. wrapper: function需要的parameter
4. function_to_be_decorated: 

另外：

​	decorator除了自身的定义以外，还需要再function_to_be_decorated被定义的地方@；

​	那么decorator的parameter并不能灵活更改