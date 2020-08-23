# https://www.nowcoder.com/practice/c4ea1f2263434861aef111aa44a5b064?tpId=140&tqId=33903&rp=1&ru=%2Fta%2Fexam-iqiyi&qru=%2Fta%2Fexam-iqiyi%2Fquestion-ranking
import sys
def DeleteDuplicate(s):
    tmp=[]
    for item in s:
        if item not in tmp:
            tmp.append(item)
    tmp="".join(tmp)
    print(tmp)

def main():
    s = sys.stdin.readline().strip()
    DeleteDuplicate(s)

main()