"""
演示函数使用的过程中，变量的作用域
"""
# 局部变量
# def test_a():
#     num = 100
#     print(num)
#
# test_a()
# # 出了函数体，局部变量就无法使用了
# print(num) # 系统警告  # NameError: name 'num' is not defined.


# 全局变量
# num = 200
#
# def test_a():
#     print(f'test_a: {num}')
#
# def test_b():
#     print(f'test_b: {num}')
#
# test_a()
# test_b()
# print(num)

# 在函数内修改全局变量
# num = 200 # 全局变量
#
# def test_a():
#     print(f'test_a: {num}')
#
# def test_b():
#     num = 500  # 这里的num已经是局部变量了，和之前的num不是同一个变量
#     print(f'test_b: {num}')
#
# test_a()  # test_a: 200
# test_b()  # test_b: 500
# print(num) # 200



# global 关键字，在函数内声明变量为全局变量

num = 200 # 全局变量

def test_a():
    print(f'test_a: {num}')

def test_b():
    global num # 设置函数内部定义的变量为全局变量
    num = 500  # 这里的num，和之前的num被声明为同一个变量
    print(f'test_b: {num}')

test_a()  # test_a: 200
test_b()  # test_b: 500
print(num) # 500

