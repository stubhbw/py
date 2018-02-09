# encoding:utf-8
import re

# 文件对象方法

# f = open('test.txt', 'r')
# print(f.read())
# f.close()

# 循环依次打印每一行
# for i in open('test.txt'):
#     print(i)

# readline 每次读取一行 超出范围后返回None
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# readlines
# print(f.readlines())

# next 每次读取一行 超出返回则报错StopIteration
# print(f.next())
# print(f.next())
# print(f.next())
# print(f.next())
# print(f.next())
# print(f.next())

# write 每次写一个字符串
# writelines 实现多行写入,效率比write更高,少量写入用write
# l = ['one\n', 'two\n', 'three\n']
# f.writelines(l)

# read其实是将文件的指针跳到最后
# print('第一次读取' + f.read())
# seek可以将指针设置到指定的位置
# seek(x,y)
#  x 表示偏移量,可以为负数.正向右偏移,负向左偏移
#  y 表示选项
#       0 表示将指针从文件开头到偏移量字节处
#       1 表示将指针从文件当前位置到偏移量字节处
#       2 表示将指针从文件末尾到偏移量字节处
# f.seek(-3, 2)
# print('第二次读取' + f.read())

# flush 提交更新,将缓存区内的数据及时提交到文件当中
# f.flush()

# f.close()

# 举例:统计文件中Hello的个数
# content = f.read()
# f.close()
# hiReg = r'hello'
# helloReg = re.compile(hiReg, re.I)
# hiList = helloReg.findall(content)
# print(len(hiList))

# 举例:替换文件中的hello并另存为其他文件
# content = f.read()
# f2 = file('new.txt','w')
# content2 = re.sub(r'(?i)hello', 'csvt', content)
# f2.write(content2)
# f2.close()
# f.close()
