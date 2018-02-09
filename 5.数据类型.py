# encoding:utf-8
# 数据类型
"""
-----------数字
-----------字符串
-----------列表
-----------元组
-----------字典
"""
# ----------------------------------------数字
print("----------------------------------------数字")
# ----整型 int
a = 123
print(type(a))
# ----长整型 long
b = 999999999999999999999
print(type(b))
c = 99L
print(type(c))
# ----浮点型 float
d = 13.0
print(type(d))
e = 5.0 / 2
print(type(e))
# ----复数类型 complex
f = 3.14j
print(type(f))
# ----------------------------------------字符串
print("----------------------------------------字符串")
# ----单引号 ''
str1 = 'hello world'
print(str1)
print(type(str1))
# ----双引号 ""
str2 = "hello world"
print(str2)
# ----注意嵌套使用,转义字符
str3 = "hello i'm hebw"
print(str3)
str4 = "hello i'm \"hebw\""
print(str4)
# ----三引号 """   """ 保存文字的格式
# ----注意换行符.缩进符
str5 = """Tom:
    i'm hebw,nice to see you
    ok , see you again."""
str6 = "Tom:\n\ti'm hebw,nice to see you\n\tok , see you again."
print(str5)
print(str6)
# ----字符串,列表,元组都被称作序列类型数据
# ----索引
str6 = 'abcde'
print(str6[0] + str6[1])
print(str6[-1] + str6[-2])
# ----切片 [开始:结束:间隔默认为1,有调整切片方向的作用] 从左向右切片
# ----切片 正索引
print(str6[0:1])
print(str6[:4])
print(str6[2:])
print(str6[2::2])
# ----切片 负索引
print(str6[-1])
print(str6[-1:])
print(str6[-1::-1])
print(str6[-4:-1])
print(str6[-1:-4:-1])
print(str6[-2:-5:-1])

