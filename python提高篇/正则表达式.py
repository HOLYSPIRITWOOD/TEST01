# 演示正则表达式 re模块的三个基础用法;
import re

def 正则匹配(匹配函数,字符串a,字符串b):
    匹配结果 = 匹配函数(字符串a,字符串b)
    #print(type(匹配结果))
    if type(匹配结果) == re.Match:
        print(匹配结果.span())
        print(匹配结果.group())
    elif type(匹配结果) == list:
        print(匹配结果)
    else:
        print("不匹配")

#字符串 = "abdbabddaadf"
## match 从头匹配 , 成功返回匹配对象 ,失败返回 None
## match 只能从头匹配 , 
#正则匹配(re.match,"abd",字符串)

##search 收索整个字符串 , 找到一个匹配的
#字符串1 = " 赵灵儿 李逍遥 林月如"
#正则匹配(re.search,"灵儿",字符串1)

##findall 收索整个字符串 , 找到所有匹配的
#字符串2 = "赵灵儿  李逍遥 灵儿 小灵儿 林月如"
#正则匹配(re.findall,"灵儿",字符串2)