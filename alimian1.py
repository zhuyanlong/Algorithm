#输入一个字符串，判断是否符合员工生命周期（需要满足，先入职，再离职，
#并且晋升/转岗行为只能发生在在职状态)
#1. String str="入职"                                   返回true
# 2. String str="入职 晋升 转岗"                          返回 true
# 3. String str="入职 晋升 转岗 离职"                      返回true
# 4. String str="入职 晋升 离职 入职 离职"                  返回true
# 5. String str="入职 转岗 入职"                           返回false
# 6. String str="入职 转岗 离职 晋升 入职"                  返回false
# 7. String str="入职 离职 离职"                           返回fasle
# 8. String str="晋升 转岗 离职"                           返回false

def lifeCycle(str):
    life=str.split()
    count=0
    for i in range(len(life)):
        if life[i]=="入职":
            if count!=0:
                return False
            count+=1
        if life[i]=="离职":
            if count!=1:
                return False
            else:
                count=0
        if life[i]=="晋升" or life[i]=="转岗":
            if count!=1:
                return False
    return True

def main():
    s="晋升 转岗 离职"
    print(lifeCycle(s))

main()