a=13
b=24
c=a | b
d=a&b
#print(c) #或
#print(d) #与
#print(~a) #非  符号位
#print(a^b) #异或
#print(a<<1) #左移1位
#print(a>>1) #右移一位
'''
不用四则运算两个数相加
1.异或运算
2.与运算
3.前两个相加
'''

def fun(a,b):
	sum=a^b
	num=(a&b)<<1
	while num!=0:
		temp=sum
		qwer=num
		sum=temp^num
		num=(temp&qwer)<<1

	return sum

print(fun(12,14))