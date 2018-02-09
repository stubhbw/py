#!/usr/bin/python
# coding=utf-8
print "你好世界"

str = 'Hello World Python'

# Python 字符串
print "============================"
print "Python 字符串"
print str
print str[0]
print str[0:5]
print str[1:]
print str + " hebw"
print str * 3 + "==="

print str[:-1]

# Python 列表
print "============================"
print "Python 列表"
list = ['nihao', 'buhao', 'henhao']
tinylist = ['123', 'hebw']

print list
print list[0]
print list[1:3]
print list[1:]
print tinylist * 2
print list + tinylist

# Python 元组
print "============================"
print "Python 元组"

tuple = ('runoob', 789, 2.323, 'Hebw', '70.2')
tinytuple = ('123', 'Hebw')

print tuple
print tuple[0]
print tuple[1:3]
print tuple[1:]
print tuple * 2
print tuple + tinytuple
