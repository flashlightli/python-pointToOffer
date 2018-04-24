#整数中1出现的次数（从1到n整数中1出现的次数）
def NumberOf1Between1AndN_Solution(n):
    # write code here
    sum = 0
    for item in range(n + 1):
        for i in str(item):
            if i == '1':
                sum += 1
    return sum

print(NumberOf1Between1AndN_Solution(299))