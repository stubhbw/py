# encoding:utf-8

# 内置函数 处理字符串的内置函数
# 总结 capitalize replace split 还有string模块 处理字符串
import string

str = 'aaabcde,fghijklmn,opqrst,uvwxyz'

# 字符串首字母大写
print(str.capitalize())
# 替换,第三个参数表示替换的次数,默认替换所有
print(str.replace('a', 'Hello_A'))
print(str.replace('a', 'Hello_A', 2))
# 按照某元素切割,返回一个列表,第三个参数表示切割的次数,默认全部
print(str.split(','))
ip = '192.168.0.1'
print(ip.split('.'))
print(ip.split('.', 1))

print(string.replace(str, 'a', 'AAA'))
