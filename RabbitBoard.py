#动态规划法
#用字典来存储每一个坐标，实际上消耗应该和二维list是差不多的
def main():
    a=[]
    #可以用这种方式来处理循环输入
    while(True):
        n=int(input())
        if n==-1:
            break
        a.append(n)
    # print(a)
    a.sort()
    n=a[-1]
    result={}
    for i in range(n+1):
        result[(0,i)]=1
    for i in range(1,n+1):
        for j in range(i,n+1):
            if i==j:
                result[(i,j)]=result[(i-1,j)]
            else:
                result[(i,j)]=result[(i-1,j)]+result[(i,j-1)]
    for i in range(len(a)):
        print(i+1,a[i],result[(a[i],a[i])]*2)

main()