# encoding:utf-8
# 深拷贝和浅拷贝

# 总结 浅拷贝和深拷贝的区别在于拷贝的新对象的内存地址和对象包含的元素的内存地址是不是都是新的一个内存地址


import copy

# b = a ,修改a会导致b也变化,因为a b都是指向同一个内存空间
a = [1, 2, 3, ['a', 'b', 'c']]
b = a
a.append(1)
print(id(a))
print(id(b))
print(b)

# 浅拷贝 c指向另一个内存空间 增删a的元素不会导致c发生改变,但是修改a的元素会导致c发生变化
c = copy.copy(a)
a.append(6)
print(id(a))
print(id(c))
print(a)
print(c)
# 浅拷贝,虽然不存在同一个内存空间,但是包含的元素还是在同一个内存空间,修改元素还是会同时改变
print(id(a[3]))
print(id(c[3]))
a[3].append('d')
print(c)

# 深拷贝 理解为将所有的数据都拷贝出来
d = copy.deepcopy(a)
print(id(a))
print(id(d))
print(id(a[3]))
print(id(d[3]))
