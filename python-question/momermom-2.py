def count_down(n):
    print("=======",n)
    while n >= 0:

        newn = yield n
        print("*********", newn)
        if newn:
            n = newn
            print("-------")
        else:
            n-=1

cd = count_down(5)           #声明一个生成器并不会导致里面的东西运行
# for i in cd:          #本质上调用for循环就是调用next方法
#     print("----/////",i)
#     if i == 5:
#         cd.send(3)          #send在生成器生成后立即执行不允许带参数

next(cd)
cd.send(3)

# def prt1(num):
#     while True:
#         print("generator()" + str(num))
#         yield num
#         num += 1
#         print(111, num)
#
#
# z = prt1(9)  # 此处不会导致prt1函数真正执行，因此第一个print语句不会执行
# print(z.send(None))  # 生成器函数开始执行，打印第二个print,到yield处，返回9
# print("========")
# print(z.send(1))  # 生成器函数从上次yiled之后继续执行，返回10,
# # 由于yiled的返回值没有任何赋值，这里的参数1并没有什么用(luan)处（yong）
# print("++++++++++++")
# print(z.next())  # next在这种情况下等同于send(xxx)