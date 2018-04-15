list=[4,5,6,1,6,78,3]
n=3
temp=[]
for i in list:
	if(len(temp)<3):
		temp.append(i)
	else:
		for j in temp:
			if(j>i):
				print(j)
				j=i
				break

print(temp)