list=[2,4,3,6,3,2,5,5]
n2=0
for i in list:
	n2=n2^i
s=bin(n2)[2:]

n=0

for i in s:
	if(s.index(i)==1):
		n=i
t=len(s)-int(i)
a=int('1'+'0'*(t-1))

arr1=[]
arr2=[]
for i in list:
	if(bin(i)[-t]=='1'):
		arr1.append(i)
	else:
		arr2.append(i)
print(arr1)
print(arr2)
m1,m2=0,0
for i in arr1:
	m1=m1^i
for i in arr2:
	m2=m2^i
print(m1,m2)