import sys

def main():
    s = sys.stdin.readline().strip().split()
    s=[int(s[i]) for i in range(len(s))]
    A=s[0]
    B=s[1]
    a=s[2]
    b=s[3]
    k=fun(a,b)
    # print(k)
#a b除以公因子，化为最小的数
    b//=k
    a//=k
#x1是能整除a的最大值
    x1=A-A%a
    # print(x1)
#y1是通过x1求得的y
    y1=x1/a*b
#y2是能整除b的最大值
    y2=B-B%b
#x2是通过y2求得的
    x2=y2/b*a
    if x1>A or y1>B:
        x1=0
        y1=0
    if x2>A or y2>B:
        x2=0
        y2=0
    x=int(max(x1,x2))
    y=int(max(y1,y2))
    print(x,y)

#求a和b的公因子
def fun(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        c=a%b
        a=b
        b=c
    return a

main()