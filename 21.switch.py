# encoding:utf-8
# switch
# Python 通过字典解决switch相同的功能

# 这个导入后可以自动转化数据带小数点
from __future__ import division


# print(6 / 2)
# print(5 / 2)
# print(5.0 / 2)


# 计算器
def add(x, y):
    return x + y


def jian(x, y):
    return x - y


def cheng(x, y):
    return x * y


def chu(x, y):
    return x / y


# 用if 和 else 写的代码
def operator(x, o, y):
    if o == "+":
        return add(x, y)
    elif o == '-':
        return jian(x, y)
    elif o == '*':
        return cheng(x, y)
    elif o == '/':
        return chu(x, y)
    else:
        pass


print(operator(6, '+', 6))


# 用字典的方法
oper = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y,
        '/': lambda x, y: x / y}


def fc(x, o, y):
    print(oper.get(o)(x, y))


fc(12, '/', 2)

# 总结
# {}.get('o')('1', '2')
