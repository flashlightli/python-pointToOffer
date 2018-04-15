import json

str1='hello world'
print(str1[::-1])#反转

arr=[1,2,3,'abc']
print(arr[::-1]) #支持数组的反转

#SQL  数组变成字符串

sarr=','.join(map(str,arr))
print(sarr)

#sql 字符串变成数组
sstr='1,2,3,ab'
print(sstr.split(','))

#json 转字符串
obj={
	"ss":"123",
	"time":111
}
print(json.dumps(obj))
print(type(json.dumps(obj)))

#字符串转json

objStr='{"ss": "123", "time": 111}'
print(json.loads(objStr))
print(type(json.loads(objStr)))