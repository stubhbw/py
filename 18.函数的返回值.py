# encoding:utf-8
# 函数的返回值 利用关键字 return

# 函数被调用后默认返回 NONE NONE在逻辑值中代表FALSE
# 函数中return 触发后函数也终止了


def fun(c, b):
    return c + b


def fun():
    print "123"


print(fun())

a = sum([1, 2, 3, 4, 5])
print(a)
