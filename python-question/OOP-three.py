'''
多态
同一个事物不同时刻体现出来的不同状态
前提条件：
1.继承关系
2.方法重写
3.父类引用指向子类对象
好处
 A:提高了代码的维护性(继承保证)
 B:提高了代码的扩展性(由多态保证)
'''
class f():
	def __init__(self,name,sex):
		self.name=name
		self.sex=sex
	def show(self):
		print(self.name)

class z(f):
	def __init__(self,name,sex):
		super(z,self).__init__(name,sex)
	def show(self):
		print(self.sex)

demo=z('a','boy')
demo.show()
