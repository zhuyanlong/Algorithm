import sys

def main():
    ipt = sys.stdin.readline().strip().split()
    for item in ipt:
        #数字
        judge0=0
        #小写字母
        judge1=0
        #大写字母
        judge2=0
        #符号
        judge3=0
        if len(item)<8 or len(item)>120:
            print(1)
            continue
        for it in item:
            if it>='a' and it<='z':
                judge1=1
            elif it>='A' and it<='Z':
                judge2=1
            elif it>='0' and it<='9':
                judge0=1
            else:
                judge3=1
        if not judge1 or not judge2 or not judge3 or not judge0:
            print(2)
            continue
        print(0)

main()