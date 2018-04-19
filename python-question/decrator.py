#1、不带括号时，调用的是这个函数本身
#2、带括号（此时必须传入需要的参数），调用的是函数的return结果
#普通装饰器
import inspect

def fun1(func):
	def add_fun():
		print("add ",)
		func()
		return func()     #后面要加括号----一定
	return add_fun

@fun1#装饰器函数相当于fun1(fun2)
def fun2():
	print("222")
fun2()
fun2()

#2.被装饰的函数带参数
def fun1(func):
	def add_fun(key):
		print("add ",key)
		if key == 4:
			func(key)
			return func(key)
		else:
			return None
	return add_fun

@fun1#装饰器函数相当于fun1(fun2)
def fun2(key):
	print("222",key)
fun2(4)
fun2(3)

#1.装饰器函数带参数
def decrator(*dargs, **dkargs):
    def wrapper(func):
        def _wrapper(*args, **kargs):
            print("decrator param:", dargs, dkargs)
            print("function param:", args, kargs)
            return func(*args, **kargs)
        return _wrapper
    return wrapper

@decrator(1, a=2)
def foo(x, y=0):
    print("foo", x, y)

foo(3, 4)