#阿里巴巴笔试
#有一种操作，把任何位置的字符移到字符串末端
#给定两个长度相同的小写字符串S和T，请你计算出小强至少需要多少次将S变成T
#如果没法成功，则返回－1

def main():
    s=input()
    t=input()
    n=len(s)
    k=0
    
    for i in range(len(s)):
        if s[i]==t[k]:
            k+=1
    if k==0:
        return -1
    lst1=list(s)
    lst2=list(t)
    lst1.sort()
    lst2.sort()
    for i in range(len(lst1)):
        if  lst2[i]!=lst1[i]:
            return -1
    return n-k

print(main())