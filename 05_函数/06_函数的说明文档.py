"""
演示对函数进行文档说明
"""

# 定义函数，进行文档说明
def add(x, y):
    """
    add函数可以接收两个参数，计算相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是两数相加的结果
    """

    result = x + y
    print(f'{x} + {y} 的结果是: {x + y}')
    return result

r = add(5, 6)