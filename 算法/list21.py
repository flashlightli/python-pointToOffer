list=[1,2,3,4,5,6,7,7,8,9,8]
#奇数排在偶数前面
i,j=0,len(list)-1
while(i <= j):
	if(list[i]%2==0):
		if(list[j]%2!=0):
			list[i],list[j]=list[j],list[i]
			j = j - 1
			i = i + 1
			print(list)
		else:
			j = j - 1
	else:
		i = i + 1
	print(i,j)
print(list)