"""
演示嵌套调用函数
"""

# 定义函数b
def func_b():
    print('--2--')

# 定义函数a，并在内部调用fun_b
def func_a():
    print('--1--')

    # 嵌套调用fun_b
    func_b()

    print('--3--')

# 调用func_a
func_a()