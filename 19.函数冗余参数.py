# encoding:utf-8

# 函数冗余参数

# 接受的参数类似于一个元组

def f(x, y):
    print x, y


# 这里有一个元组,如何把元组直接传入方法内.分别当做x,y
t = (1, 2)

# 这里使用这个方法来直接传入一个元组 利用一个*号
# 传递字典则使用**号
f(*t)


# 占位符的作用
def p(x, y):
    print("%s : %s" % (x, y))


p(1, 2)
p(*t)


def fa(name="hebw", age=0):
    print('name:%s' % name + '  age:%s' % age)


fa(**{'age': 123, 'name': 'hbwwww'})

# fa('hbw', '26')
# fa(*('hb', 23))
# fa()

# 函数冗余参数
# 实际上这个args是一个元组
print('----------------------函数冗余参数,用元组接收')


def f2(x, *args):
    print(x)
    print(args)


f2(2, 1)

print('----------------------函数冗余参数,用字典接收')


def f3(x, **args):
    print(x)
    print(args)


f3(1)
f3(1, y=1)
