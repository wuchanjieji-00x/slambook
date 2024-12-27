"""
演示特殊字面量：None
"""
# 无return语句的函数返回值
# def say_hi():
#     print('hi')
#
# result = say_hi()
# print(f'无返回值函数，返回的内容是：{result}')
# print(f'无返回值函数，返回的内容类型是: {type(result)}')  # <class 'NoneType'>

# 主动返回None的函数
# def say_hi2():
#     print('hi')
#     return None
#
# result = say_hi2()
# print(f'无返回值函数，返回的内容是：{result}')
# print(f'无返回值函数，返回的内容类型是: {type(result)}')  # <class 'NoneType'>


# None用于if判断
def check_age(age):
    if age > 18:
        return 'success'
    # else:
    #     return None  # None =False，，这两行也可以省略不写

result = check_age(16)
if not result:
    # 进入if，表示result是None值，也就是False
    print('未成年，不可以进入')



# None用于声明无初始内容的变量
name = None
