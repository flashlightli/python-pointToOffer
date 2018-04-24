#数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。请写一个函数，求任意第n位对应的数字。

def num1(n):
    if n<= 9:
        return n
    count = 10
    i = 1
    while(n> count):
        count += 9*(10**i)
        i += 1
    temp = (n-count/10)//(i-1)
    temp1 = (n-count/10)%(i-1)
    print(str(10**(i-1)+temp+temp1))
    return str(10**(i-1)+temp+temp1)[:1]

print(num1(199))