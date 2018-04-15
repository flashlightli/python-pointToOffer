#最长不含重复祖父的子字符串
s='arabcacfrga'
arr=[]
length=0
result=[]
for i in s:
	arr.append(i)
	qwer={}.fromkeys(arr).keys()
	if(len(arr)!=len(list(qwer))):
		if(len(list(qwer))>length):
			legnth=len(list(qwer))
			result=arr[:len(arr)-1]
			arr = []
			arr.append(i)
		else:
			arr=[]
			arr.append(i)

print(result)