# https://www.nowcoder.com/practice/ce5b35929ab84e3a806886d9667be00a?tpId=140&tqId=33903&rp=1&ru=%2Fta%2Fexam-iqiyi&qru=%2Fta%2Fexam-iqiyi%2Fquestion-ranking
import sys

def main():
    n = sys.stdin.readline().strip().split()
    n=[int(n[i]) for i in range(len(n))]
    t=(n[1],n[0]-n[1])
    a=(n[2],n[0]-n[2])
    res=min(t[0],a[0])+min(t[1],a[1])
    print(res)

main()