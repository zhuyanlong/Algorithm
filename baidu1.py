# https://www.luogu.com.cn/problem/CF352A
#用5和0构成最大的能被90整除的数
#想法比较简单，被90整除，必须有个0，然后剩下的5构成最大的能被9整除的数
#被9整除数的特点是，各个位数之和是9的倍数，所以5出现的次数，一定是9的倍数，然后末尾由0构成就行
import sys
def main():
    n = int(sys.stdin.readline().strip())
    m=sys.stdin.readline().strip().split()
    m = list(map(int, m))
    cz=0
    cf=0
    res=""
    for i in range(len(m)):
        if m[i]==0:
            cz+=1
        else:
            cf+=1
    if cz==0:
        print(-1)
        return
    #5的个数不足9个，有0的情况下，最大就是0
    elif cf<9:
        print(0)
        return
    #每9个5构成一个数
    else:
        for i in range(cf//9):
            res+="555555555"
        while cz!=0:
            cz-=1
            res+='0'
    print(res)
    return

main()