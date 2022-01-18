# encoding: utf-8

lista = ['hello', 'there', 'my ', 'name', ' is', 'Willa']


def decorator_maker(dec1):
    def stripwhite(func):
        def wrapper(given_str):
            print(f'This is my decoration ~ {dec1}')
            res = given_str.strip()  # 定义一个会去除字符串头尾空格的decorator
            return(func(res))
        return wrapper
    return stripwhite


@decorator_maker('Willa')
def print_str(given_str):
    return(given_str + '!')


for i in lista:
    print_str(i)
