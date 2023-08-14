import threading
import time

#定义一个类 封装一个线程
class 测试线程(threading.Thread):
	def __init__(self,a,b):
		super().__init__()
		self.参数1 = a
		self.参数2 = b
	def run(self):
		while True:
			print(self.参数1+self.参数2)
			time.sleep(1)



if __name__ == "__main__":
	线程1 = 测试线程(10,30)
	线程1.start()

	while True:
		print("主线程")
		time.sleep(1)
