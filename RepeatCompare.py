#https://www.nowcoder.com/practice/24575008c6134b6fa4fab8ea0ea82a99?tpId=140&&tqId=33902&rp=1&ru=/ta/exam-iqiyi&qru=/ta/exam-iqiyi/question-ranking
import sys

def Repeat(x,k):
    x=str(x)
    res=""
    for i in range(k):
        res+=x
    res=int(res)
    return res

def main():
    n = sys.stdin.readline().strip().split()
    for i in range(len(n)):
        n[i]=int(n[i])
    v1=Repeat(n[0],n[1])
    v2=Repeat(n[2],n[3])
    if v1>v2:
        print("Greater")
    elif v1==v2:
        print("Equal")
    else:
        print("Less")

main()