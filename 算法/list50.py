#第一个出现一次的字符
s = 'hellobaby'
def findchar(s):
    for i in s:
        if s.count(i)==1:
            return i, s.index(i)
m,n=findchar(s)
print('第一个出现一次的字符是{}，位置是{}'.format(m,n))