#https://www.nowcoder.com/practice/ab900f183e054c6d8769f2df977223b5?tpId=140&&tqId=33903&rp=1&ru=/ta/exam-iqiyi&qru=/ta/exam-iqiyi/question-ranking
import sys

def judgeDNA(s):
    initial=['A','C','G','T']
    arr=[""]
    for i in range(len(s)):
        tmparr=[]
        for item in arr:
            for tmp in initial:
                if tmp+item not in s:
                    return i+1
                tmparr.append(tmp+item)
                # print(arr)
        arr=tmparr.copy()
    return len(s)

def main():
    s = sys.stdin.readline().strip()
    print(judgeDNA(s))

main()
