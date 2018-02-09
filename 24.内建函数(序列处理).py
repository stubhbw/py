# encoding:utf-8

# 内建函数 序列处理
# 总结 : filter zip map reduce

# ------------------------------------------------序列的处理操作
l = (1, 2, 3, 4, 5, 6, 7, 8)
print(len(l))
print(max(l))
print(min(l))


# 筛选,过滤的操作,第一个参数是函数,返回值是逻辑值 True 或 False
# 将大于5的数保留下来
def f(x):
    if x > 5:
        return True


# 返回值是元组
print(filter(lambda x: x == 5, l))
# 将能被2整除的数保留下来
h = range(10)


def ft(x):
    if x % 2 == 0:
        return True


print(filter(ft, h))

# 压缩 柔和 最后返回一个元素是元组的列表 区分zip和map 还有短板的时候各自的表现
name = ['mili', 'zou', 'yang']
age = [23, 12, 44]
male = ["male", 'female', 'male']
print(zip(name, age, male))
print(map(None, name, age, male))
# 注意这里的短板
test = [1, 2]
print(zip(name, age, male, test))
print(map(None, name, age, male, test))
# map第一个参数可以是函数,对合并的数据进行处理
a = [1, 2, 3]
b = [4, 5, 6]
print(map(lambda x, y: x * y, a, b))
# reduce 这个函数可以将序列的前两个数做第一个参数定义的函数的动作,然后将数再交给第三个数,一直这样进行下去
a = reduce(lambda x, y: x + y, xrange(1, 101))
print(a)
