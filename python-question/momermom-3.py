class MyDecorator(object):
    functions = []
    messages = []
    def __init__(self,func,msg='hello'):     #msg相当于参数的默认值
        self.functions.append(func)
        self.functions.append(msg)
    def inner(self,func):
        this_class=type(self)
        return this_class(func,msg='world')
    def __call__(self, *args, **kwargs):
        for i,func in enumerate(self.functions): #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
            #enumerate(sequence, [start=0])  start 下标起始的位置
            func(self.messages[i])

@MyDecorator
def first(a):
    print('first:',a)

@first.inner
def second(a):
    print('second',a)

first()
second()
