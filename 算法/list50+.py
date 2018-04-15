list=[2,3,6,3,2,5,5,2,5,3]
total=0
for i in list:
	total=total+int(bin(i)[2:])

total=str(total)
arr=[]
for i in total:
	if(int(i)%3==1):
		arr.append(len(total)-total.index(i))
ss=0
print(arr)

for i in arr:
	ss=ss+2**(i-1)
print(int(ss))