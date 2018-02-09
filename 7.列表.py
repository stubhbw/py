# encoding:utf-8
# 列表
# ----------------------------------------列表
print("----------------------------------------列表")
# ----列表 通过中括号,中间用逗号分隔元素定义,列表中的值是可变的
# ----定义一个列表,可以存储一系列的值
list1 = ['Simon', 30, 'male']
# ----定义一个空列表
list2 = []
# ----定义一个元素的列表
list3 = [1]
print(type(list1))
print(type(list2))
print(type(list3))
# ----列表的操作方法
# ----切片和索引
print(list1[0])
print(list1[:])
# ----添加一个值到列表中
list = [1, 2, 3]
list.append(4)
print(list)
# ----删除 删除第一个出现的元素,其他元素不会删除
list3 = [1, 2, 3, 4, 1]
# 按照元素删除
# list3.remove(1)
# list3.remove(2)
# list3.remove('1')
# 按照索引删除
# del (list3[0])
# print(list3)
# ----修改
list3[0] = 123456
print(list3)
# ----查找
print(1 in list3)
