import time
import threading
from 多线程封装 import 测试线程

全局变量 = 0
代码开始时间 = time.perf_counter()

def 线程函数1(互斥锁):
    global 全局变量
    global 代码开始时间
    t=0
    while True:
        互斥锁.acquire()
        全局变量+=1
        互斥锁.release()
        t+=1
        if t>= 1000000:
            t = 0
            print(f"线程1全局变量 = {全局变量}")
            break
    代码结束时间 = time.perf_counter()
    print(f"运行时间 = {代码结束时间 - 代码开始时间}秒")

def 线程函数2(互斥锁):
    global 全局变量
    global 代码开始时间
    t=0
    while True:
        互斥锁.acquire()
        全局变量+=1
        互斥锁.release()
        t+=1
        if t>= 1000000:
            t = 0
            print(f"线程2全局变量 = {全局变量}")
            break
    代码结束时间 = time.perf_counter()
    print(f"运行时间 = {代码结束时间 - 代码开始时间}秒")


if __name__ == "__main__":
    #创建互斥锁
    互斥锁 = threading.Lock()

    #创建两个线程
    线程1 = threading.Thread(target=线程函数1,args=(互斥锁,))
    线程2 = threading.Thread(target=线程函数2,args=(互斥锁,))
    线程1.start()
    线程2.start()
    print(threading.enumerate())
    while True:
        pass