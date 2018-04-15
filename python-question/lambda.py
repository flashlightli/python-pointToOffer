listA=[{'name':'aa'},{'name':'cc'},{'name':'bb'}]

li = [11, 22, 33]

print(li[1])

new_list = map(lambda a: a + 100, li)

new_list1 = filter(lambda arg: arg > 22, li)

for i in listA:
	print(i)