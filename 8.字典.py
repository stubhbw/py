# encoding:utf-8
# 字典
# ----------------------------------------字典
print("----------------------------------------字典")
# 字典是Python中唯一的映射类型 无序性
# ----字典 通过花括号,中间用逗号分隔元素定义
# ----{} 创建字典
dic = {0: 0, 1: 1, 2: 2}
# 根据key取值
print(dic[0])
print(dic[1])
print(dic[2])
dic1 = {'name': 'hebw', 'age': 13, 'gender': 'male'}
print(dic1["name"])
print(dic1["age"])
print(dic1["gender"])
name = 666
dic2 = {1: '111', name: 'hebw_name', 'x': 'male'}
print(dic2[name])
print(dic2)
# ----工厂方法dict()生成字典 比用花括号生产的效率要低
# fdict = dict(['x', 1], ['y', 2])
# print(fdict)
# ----内建方法:fromkeys(),字典中的元素具有相同的值,默认为None,主要用于值一致的情况下
ddict = {}.fromkeys(('x', 'y'), -1)
ddict2 = {}.fromkeys(('x', 'y'))
print(ddict)
print(ddict2)
# ----访问字典的值
dic5 = {'name': 'hebw', 'age': 13, 'gender': 'male'}
for key in dic5:
    print(key)
for key in dic5:
    print(dic1[key])
# ----添加一个值
dic5['tel'] = '13128965301'
print(dic5)
# ----删除一个值
# 删除字典中键为tel的键值对
# del (dic5['tel'])
# ----删除一个值并且返回键对应的元素
tel = dic5.pop("tel")
print(dic5)
print(tel)
# ----修改一个值
dic5['name'] = 'HEBW'
print(dic5)
# ----清空字典
# dic5.clear()
# print(dic5)
# ----判断是否存在
print("HEBW" in dic5)
print("age" in dic5)
# ----删除整个字典
# del (dic5)
# print(dic5)
# ----根据字典的key取得value,如果存在则返回,不存在返回指定的值或none
print(dic.get(13))
print(dic.get(1, "error"))
# ----返回字典中键的列表
print(dic.keys())
# ----返回字典中值的列表
print(dic.values())
# ----items() 返回键值对元组的列表
print(dic.items())
