# encoding:utf-8
# 变量

# 变量的命名和赋值
# 变量的命名可以是数字,字母,下划线组合,不能以数字开头
a = 1
print(a)

# 查看变量在内存中的地址,变量重新赋值,相当于标签移动,指向另一个空间
# 也就是说,下面的 a 和 b 是同一个内存地址
print(id(a))
a = 2
print(id(a))
b = 2
print(id(b))
print(id(0))
