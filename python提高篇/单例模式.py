﻿# 单例模式测试 , 该文件只能被其他文件导入

class 单例类(object):
    def 单例功能测试(self):
        print("单例测试")

#其他文件导入 此对象 , 由于防止重复导入 ,
# 所以此代码只会执行一次 ;
单例对象 = 单例类()