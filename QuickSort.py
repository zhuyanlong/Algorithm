def partition(nums,p,q):
    tar=nums[p]
    i=p
    for j in range(p+1,q):
        if nums[j]<tar:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
    nums[i],nums[p]=nums[p],nums[i]
    return i

def quickSort(nums,p,q):
    if p<q:
        i=partition(nums,p,q)
        quickSort(nums,p,i)
        quickSort(nums,i+1,q)

def main():
    nums=[28,342,418,485,719,670,878,752,662,994,654,504,929,660,424,855,922,744,600,229,728,33,371,863,561,772,271,178,455,449,426]
    quickSort(nums,0,len(nums))
    print(nums)

main()
