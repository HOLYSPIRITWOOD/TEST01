#工厂模式 适用于 按照一定的逻辑来创建对象
#或者大批量 创建 不同的类对象

class 人类(object):
    pass

class 学生(人类):
    pass

class 老师(人类):
    pass

class 学者(人类):
    pass

class 人类工厂(object):
    def 人类生产线(self,类型):
        if 类型 == "学生":
            return 学生()
        elif 类型 == "老师":
            return 老师()
        else:
            return 学者()

人类生产表 = ["学生","老师","学生","学者","学生","老师"]
郑州人类工厂 = 人类工厂()
新生儿表 = []
for x in 人类生产表:
    新生儿表.append(郑州人类工厂.人类生产线(x))

print(新生儿表)