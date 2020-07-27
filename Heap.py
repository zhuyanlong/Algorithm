#数据类型，堆
#默认0号位不存储数据，只有这样才能通过k//2定位父元素
class Heap:
    def __init__(self,nums):
        self.nums=nums
    #k为当前需要置换的元素下标
    def swim(self,k):
        while k>1 and self.nums[k]>self.nums[k//2]:
            self.nums[k],self.nums[k//2]=self.nums[k//2],self.nums[k]
            k=k//2
    #k为当前需要置换的元素下标
    def sink(self,k):
        while 2*k<=len(self.nums):
            j=2*k
            if j<len(self.nums):
                if self.nums[j+1]>self.nums[j]:
                    j+=1
            if self.nums[k]>=self.nums[j]:
                break
            self.nums[k],self.nums[j]=self.nums[j],self.nums[k]
            k=j

def main():
    nums=[0,10,9,8,7,6,5,4,3,2,1]
    h=Heap(nums)
    print(h.nums)
    h.nums[1],h.nums[-1]=h.nums[-1],h.nums[1]
    h.nums.pop()
    h.sink(1)
    print(h.nums)

main()

