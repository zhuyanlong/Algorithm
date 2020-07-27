class HeapSort:
    def __init__(self,nums):
        self.nums=nums
    #k为当前需要置换的元素下标
    def swim(self,k):
        while k>1 and self.nums[k]>self.nums[k//2]:
            self.nums[k],self.nums[k//2]=self.nums[k//2],self.nums[k]
            k=k//2
    #k为当前需要置换的元素下标
    def sink(self,k,n):
        while 2*k<=n:
            j=2*k
            if j<n:
                if self.nums[j+1]>self.nums[j]:
                    j+=1
            if self.nums[k]>=self.nums[j]:
                break
            self.nums[k],self.nums[j]=self.nums[j],self.nums[k]
            k=j

    #假定初始序列无序
    #n是实际元素个数
    def sort(self):
        n=len(self.nums)
        for i in range(2,n):
            self.swim(i)
        while n>1:
            self.nums[1],self.nums[n-1]=self.nums[n-1],self.nums[1]
            # print(self.nums[n-1])
            n-=1
            self.sink(1,n-1)

def main():
    nums=[0,84, 10, 11, 78, 51, 30, 31, 5, 91, 83]
    h=HeapSort(nums)
    h.sort()
    print(h.nums)

main()