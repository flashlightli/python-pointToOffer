import functools

print(int('12345'))  # print 12345 )
print(int('11111', 8))  # print 4681
#partial 就是一个偏函数 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
foo = functools.partial(int, base=8)

print(foo('11111'))  # print 4681
#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，并且会自动放入左边
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))