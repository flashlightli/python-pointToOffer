def Fun():
	temp=[lambda x : x*i for i in range(4)]
	return temp

for everyLambda in Fun():
	print(everyLambda(2))

'''
输出 6 6 6 6
解决方案
'''
def Fun():
	temp=[lambda x, i=i: x*i for i in range(4)]
	return temp

for everyLambda in Fun():
	print(everyLambda(2))

# yield惰性求值
def Fun():
	for i in range(4):
		yield lambda x :i*x

for qwe in Fun():
	print(qwe(2))

# 生成器  把[] 变成（）就好了 一般通过for迭代
'''
1.print并不会阻断程序的执行，就不用多说了。

2.func2()方法中的循环执行第一次就被return结束掉了。（后面的2、3、4就不会有返回的机会了）

3.yield你可以通俗的叫它"轮转容器"，可用现实的一种实物来理解：水车，先yield来装入数据、产出generator object、使用next()来释放；好比水车转动后，车轮上的水槽装入水，随着轮子转动，被转到下面的水槽就能将水送入水道中流入田里。
个人理解，yield在python内部是当作list处理的：
'''
#yield返回执行结果并不中断程序执行，return在返回执行结果的同时中断程序执行。
print("================")
def Fun():
	return (lambda x :i*x for i in range(4))

for qwe in Fun():
	print(qwe(2))