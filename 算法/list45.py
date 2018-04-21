#数组排成最小的数
#nlgn用快排也可以实现
list45=[3,32,321,123]
for i in range(0,len(list45)):
	for j in range(i,len(list45)):
		s=str(list45[i])+str(list45[j])
		t=str(list45[j])+str(list45[i])
		if(s>t):
			list45[i],list45[j]=list45[j],list45[i]

print(list45)
ss=""
for i in list45:
	ss=ss+str(i)
print(ss)
#[123, 321, 32, 3]
#123321323