#礼物最大价值
class Solution:
    def getmaxValue(self, values, rows, cols):
        if not values or rows<=0 or cols <=0:
            return 0
        # 用于存放中间数值的临时数组
        temp = [0] * cols

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0

                if i > 0:
                    up = temp[j]
                if j > 0:
                    left = temp[j-1]
                temp[j] = max(up,left) + values[i*rows+j]
            print(temp)
        return temp[-1]
s = Solution()
a = s.getmaxValue([1,13,3,8,12,2,9,6,5,7,4,11,3,7,16,5],4,4)
print(a)