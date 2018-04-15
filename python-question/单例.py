#单例 一个类只能出现一个实例
#本身就是单例模式 可以在其他文件调用 from 单例.py import singleton
'''
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
'''

'''
使用__new__
class Singleton(object):
	_instance = None

	def __new__(cls, *args, **kw):
		print("aaaaaaaaaa")
		if not cls._instance:
			print("BBBBBBBBB")
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
		return cls._instance


class MyClass(Singleton):
	a = 1

a=MyClass()
b=MyClass()
print(a==b)
print(a is b)
'''

'''
装饰器 
from functools import wraps


def singleton(cls):
	instances = {}

	@wraps(cls)
	def getinstance(*args, **kw):
		if cls not in instances:
			instances[cls] = cls(*args, **kw)
		return instances[cls]

	return getinstance


@singleton
class MyClass(object):
	a = 1

a=MyClass()
b=MyClass()
print(a==b)
print(a is b)
'''

#metaclass 元类-type
class Singleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]


#Python3
class MyClass(metaclass=Singleton):
   pass

a=MyClass()
b=MyClass()
print(a==b)
print(a is b)