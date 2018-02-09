# encoding:utf-8
from __future__ import division
import time

# 内建函数
# 总结 abs type max min len divmod pow round callable isinstance cmp xrange str tuple int long list float

# 返回数字的绝对值
a = abs(-10111111)
print(a)
print(type(a))
# 取最大值
l = [1, 23, 4, 5, 6, 7, 8, 9, 0, 1, 3, 23, 2, 2, 31, 5, 7, 89, 34, 23, 'sd']
l2 = {1: 1, 2: 2}
print(max(l))
print(min(l))
# 求序列的长度
print(len(l))
print(len(l2))
# 返回包含两个数字的商和魔的元组
print(divmod(2, 5))
# 这个运算有点复杂啊
print(pow(2, 3, 4))
# 四舍五入
print(round(12.4))
# 检测函数是否可以被调用
print(callable(round))
# 判断对象是否属于某类型
print(isinstance(l, tuple))
print(type(l))
# 判断两个字符串是否一样
print(cmp('1', '1'))
print(cmp('1', '2'))
print(cmp('2', '1'))
# xrange效率比range高很多,具体用处不明啊
print(xrange(12))
# 类型转换
print(type(int(123)))
print(type(long(123)))
print(type(float(123)))
print(type(tuple([1, 2])))
print(type(list((1,))))
print(type(str(1)))

# 总结 abs type max min len divmod pow round callable isinstance cmp xrange
