import os

#展示3个基础方法
#1 列出文件夹内所有内容
print(os.listdir("E:\Games"))

#2 判断一个文件是否为 文件夹
print(os.path.isdir("E:\Games\八方旅人"))

#3 判断路径是否存在
print(os.path.exists("E:\Games"))

# 定义递归函数 输出所有文件
def 递归列出文件(文件路径):
	if os.path.exists(文件路径):
		文件列表 = os.listdir(文件路径)
		for x in 文件列表:
			if os.path.isdir(文件路径+"\\" +x):
				递归列出文件(文件路径+"\\" +x)
			print(x)


文件路径 = "E:\Games"
递归列出文件(文件路径)