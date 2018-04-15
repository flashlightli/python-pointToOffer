#丑数的计算
list=[1]
start=1
M2, M3, M5 = 2, 3, 5
index2,index3,index5=0,0,0

while len(list) < 1500:

	while M2 <= list[-1]:
		index2 += 1
		M2 = list[index2] * 2
	while M3 <= list[-1]:
		index3 += 1
		M3 = list[index3] * 3
	while M5 <= list[-1]:
		index5 += 1
		M5 = list[index5] * 5

	list.append(min(M2, M3, M5))
print(list[1499])