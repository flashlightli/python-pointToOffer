from datetime import datetime
now = datetime.now()
def fun(date=datetime.now()):
    arr=["1","2"]
    brr=["3"]
    arr.extend(brr)  #连接两个数组
    print("=========",":".join(arr),str(date))  #join方法以一个分隔符 就是前面那个参数 把join内的参数分割开来

