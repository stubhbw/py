# encoding:utf-8

# lambda表达式

# 普通的表达式
def lam(x, y):
    return x + y


a = lam(x=1, y=2)
b = lam(*(3, 7))
print(a)
print(b)

# lambda表达式写法

print("----------------------lambda")


def l(x, y):
    return x * y


g = lambda x, y: x * y

print(type(g))
print(id(g))
print(g)
print(g(2, 2))

# lambda用法
print("----------------------lambda用法")
l = range(1, 6)
# l = [1]
print(l)


def fa(x, y):
    return x * y


# 注意这个reduce的作用 递减[1,2,3,4,5,6] 每次去两个值去做前面的方法
a = reduce(fa, l)
c = reduce(lambda x, y: x * y, l)
print(a)
print(c)
