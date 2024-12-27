


# money = 5000000
# name = input('请输入您的姓名： ')
#
# def check_money():
#     print(f'{name}，您好，您的余额剩余: {money}元')
#     menu()
#
# def putin():
#     x = int(input('请输入您存款的金额：'))
#     global money
#     money += x
#     print(f'{name}，您好，您存款{x}元成功')
#     check_money()
#     menu()
#
# def putout():
#     y = int(input('请输入您取款的金额：'))
#     global money
#     if y <= money:
#         money -= y
#         print(f'{name}，您好，您取款{y}元成功')
#         check_money()
#     else:
#         print('对不起，您的余额不足')
#     menu()
#
# def menu():
#     print('------主菜单------')
#     print(f'{name}，您好，欢迎来到黑马银行，请选择操作：')
#     print('查询余额\t[输入1]')
#     print('存款\t\t[输入2]')
#     print('取款\t\t[输入3]')
#     print('取款\t\t[输入4]')
#     num = int(input('请输入您的选择：'))
#     # for num in range(1, 5):
#     if num == 1:
#         print('------查询余额------')
#         check_money()
#     elif num == 2:
#         print('------存款------')
#         putin()
#     elif num == 3:
#         print('------取款------')
#         putout()
#     else:
#         print('------退出------')
#         return
#
# menu()


# 教程

# 定义全局变量
money = 5000000
# name = None

# 要求客户输入姓名
name = input('请输入您的姓名： ')

# 定义查询函数
def check(show_header):
    if show_header:  # 通过参数控制内容的输出
        print('----------查询余额----------')
    print(f'{name}，您好，您的余额剩余：{money}')

# 定义存款函数
def putin(num):
    global money
    money += num
    print('----------存款----------')
    print(f'{name}，您好，您存款{num}元成功')

    # 调用check函数查询余额
    check(False)  # 传入实参

# 定义取款函数
def putout(num):
    global money
    money -= num
    print('----------取款----------')
    print(f'{name}，您好，您取款{num}元成功')

    # 调用check函数查询余额
    check(False)  # 传入实参

# 定义主菜单函数
def menu():
    print('----------主菜单----------')
    print(f'{name}，您好，欢迎来到黑马银行，请选择操作：')
    print('查询余额\t[输入1]')  # 注意这里制表符的使用，可以对齐输出
    print('存款\t\t[输入2]')   # 第一行第一项较长，所以用一个\t，下面的用两个\t
    print('取款\t\t[输入3]')
    print('取款\t\t[输入4]')
    return input('请输入您的选择：')

# 设置无限循环，确保程序不退出
while True:
    keyboard_input = menu()  # 通过变量接收menu函数的返回值（即客户的选择），这里既接收了menu函数的返回值，也调用了menu函数
    if keyboard_input == '1':
        check(True)   # 注意这里通过传入实参去控制check函数的输出
        continue   # 通过continue继续下一次循环，回到主菜单
    elif keyboard_input == '2':
        num = int(input('请输入您存款的金额：'))  # 获取一个实参
        putin(num)
        continue
    elif keyboard_input == '3':
        num = int(input('请输入您取款的金额：'))  # 获取一个实参
        putout(num)
        continue
    else:
        print('程序退出')
        break


