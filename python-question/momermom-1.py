list1 = [{'age' : 11 ,'money': 22 },{'age' : 13 ,'money': 24} ,{'age' : 12 ,'money': 26},{'age' : 12 ,'money': 23},{'age' : 12 ,'money': 24}]
 #一行代码实现对list根据age进行排序   
list2 = sorted(list1, key=lambda d: d['age'], reverse = False)#reverse判断正序倒序
print(list2)

#求列表的差集  交集 并集
list21 = [1,2,3,4]
list22 = [3,4,5,6]
list23 = [ i for i in list21 if i not in list22 ]         #差集元素在list21而不在list22
list24 = list(set(list21) ^ set(list22))        #除去公有的元素
list25 = list(set(list21) & set(list22))        #两个都有的元素
list26 = list(set(list21).union(set(list22)))   #求并集 只要存在 即拥有
list27 = list(set(list21).difference(set(list22)))      #list21有但是list22没有的 差集
print(list23,list24,list25,list26,list27)

#求list元素的和
list31 = [1,2,3,4,5,6]
list32 = sum([2+i for i in list31 if list31.index(i) % 2 == 0])
print(list32)

 #sorted  嵌套 sorted 先根据age排序 再根据money 排序
list41 = [{'age' : 11 ,'money': 22 },{'age' : 13 ,'money': 24} ,{'age' : 12 ,'money': 26},{'age' : 12 ,'money': 23},{'age' : 12 ,'money': 24}]
list42 = sorted(list1, key=lambda d: d['age'] , reverse = False)
#
list43 = sorted(sorted(list1, key=lambda d: d['money'] , reverse = False), key=lambda d: d['age'] , reverse = False)
print(list43)
