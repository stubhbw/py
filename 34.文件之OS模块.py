# encoding:utf-8
import os


# os模块

# ----------------------------------------------创建一个目录(文件夹)
# os.mkdir("test")
# ----------------------------------------------创建一个目录(文件夹),可以嵌套
# os.makedirs("a/b/c")
# ----------------------------------------------删除一个(文件夹),例如:a/b/c,只删除c
# os.rmdir("a/b/c")
# ----------------------------------------------删除一个(文件夹),可以嵌套删除,例如:a/b/c,全部删除
# os.removedirs("a/b/c")
# ----------------------------------------------返回一个列表,包含文件夹中的所有文件和目录,不包含子目录
# list = os.listdir("C:/Users/A13201/Desktop/pythonStudy")
# 返回根目录的列表 比如 c盘
# list = os.listdir("/")
# 返回当前目录文件文件夹列表
# list = os.listdir(".")
# print(list)
# ----------------------------------------------获取当前路径
# cwd = os.getcwd()
# print(cwd)
# ----------------------------------------------切换目录
# 切换到根目录
# os.chdir("/")
# os.chdir("C:/Users/A13201/Desktop")
# print(os.getcwd())


# 小程序: 遍历一个目录,返回包括子目录的文件绝对路径

def getFileList(path):
    # 遍历得到路径下的文件列表
    fileList = os.listdir(path)
    # 得到当前的全路径,用来拼接
    filepath = os.getcwd()
    # 空列表作为保存文件路径的容器
    allfileList = []
    for fileName in fileList:
        # 拼接路径

        allfileList.append(os.path.join(filepath, fileName))

    print(allfileList)


getFileList('C:\Users\A13201\Desktop\pythonStudy\\test')
