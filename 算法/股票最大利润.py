#一只股票有涨有跌 涨跌数据list所示   求这只股票利润的最大值

arr = [1, 0, 4, 6, 3, 7, 8, 9, 2, 0, 5]
sign = 0         #标记是记录最大值还是最小值
result = [1]
number = 0

for i in range(0, len(arr) - 2):
    if sign == 0:
        if arr[i] >= arr[i + 1]:
            result.pop()
            result.append(arr[i + 1])
        else:
            #result.append(arr[i])
            result.append(arr[i + 1])
            sign = 1
    elif sign == 1:
        if arr[i] > arr[i + 1]:
            result.append(arr[i + 1])
            sign = 0
        else:
            result.pop()
            result.append(arr[i + 1])

if len(result)%2 == 0:
    result.pop()

print(result)
for i in range(0,len(result)):
    if i%2 != 0:
        number += result[i] - result[i-1]
print(number)