# 导入multiprocessing 模块
import multiprocessing
import time

#定义进程的主函数
def 进程1():
    while True:
        print("我是子进程1")
        time.sleep(1)

#创建进程对象
子进程1 = multiprocessing.Process(target=进程1)


if __name__ == "__main__":
    子进程1.start()
    #主进程运行
    while True:
        print("我是主进程")
        time.sleep(1)