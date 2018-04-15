#逆序对
def merge_sort(data):
	if (len(data) <= 1):
		return data
	index = len(data) // 2 #返回整数部分 除去余数
	lst1 = data[:index]
	lst2 = data[index:]
	left = merge_sort(lst1)
	right = merge_sort(lst2)
	return merge(left, right)


def merge(lst1, lst2):
	"""to Merge two list together"""
	list = []
	while (len(lst1) > 0 and len(lst2) > 0):
		data1 = lst1[0]
		data2 = lst2[0]
		if (data1 <= data2):
			list.append(lst1.pop(0))
		else:
			global num
			num = num + 1
			list.append(lst2.pop(0))
	if (len(lst1) > 0):
		list.extend(lst1)
	else:
		list.extend(lst2)
	return list


num = 0
arr = [2, 1, 4, 3, 6, 5, 4]
print(merge_sort(arr))
print(num)
