import threading

#创建锁
资源锁 = threading.Lock()

#上锁 
资源锁.acquire()

#解锁
资源锁.release()

