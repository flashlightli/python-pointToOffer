# def a(c):
# 	def rea():
# 		print("aaaaa")
# 		c()       #注释掉会只显示aaaaa
# 		print("AAAAAAAAAA")
# 	return rea
#
# def b(c):
# 	def reb():
# 		print("bbbbbbb")
# 		c()       #注释掉会只显示aaaaa bbbbb
# 		print("BBBBBBBBBB")
# 	return reb
#
# @a
# @b
# def c():
# 	print("ccccccc")
# c()


def logged(func):
	def with_logging(*args, **kwargs):
		print(func.__name__ + " was called")
		return func(*args, **kwargs)

	return with_logging


@logged
def f(x):
	"""does some math"""
	return x + x * x


def f(x):
	"""does some math"""
	return x + x * x


f = logged(f)
print(f.__name__,f.__doc__)#with_logging None 一些属性会丢失

# from functools import wraps
# def logged(func):
# 	@wraps(func)
# 	def with_logging(*args, **kwargs):
# 		print(func.__name__ + " was called")
# 		return func(*args, **kwargs)
# 	return with_logging
# #而functools.wraps 则可以将原函数对象的指定属性复制给包装函数对象, 默认有 __module__、__name__、__doc__,或者通过参数选择。代码如下：
# @logged
# def f(x):
#    """does some math"""
#    return x + x * x
#
# print(f.__name__)  # prints 'f'
# print(f.__doc__)  # prints 'does some math'