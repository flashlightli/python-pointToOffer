name='123'
sex='boy'
print("{name}是一个{sex}".format(name=name,sex=sex))#format用法

#装饰器
import time
print("-----------------以下是常规装饰器---------------")
#常规装饰器
def getTimes(func):
    def getTime():
        start_time=time.time()
        func()
        end_time=time.time()
        print("the time is %s"%(end_time-start_time))
    return getTime

@getTimes
def test1():
    time.sleep(3)
    print("in the test1")

test1()
print("-----------------以下是带参数的装饰器---------------")
#带参数装饰器
def getTimes2(func):
    def getTime2(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print("the time is %s"%(end_time-start_time))
    return getTime2


@getTimes2
def test22(name,age):
    time.sleep(5)
    print("in the test2",name,age)
test22('lyz',22)