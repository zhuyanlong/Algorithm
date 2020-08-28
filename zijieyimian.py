#删除链表中的重复数字
#比如1-2-2-3-3，删除之后就变成了1
#链表头节点的重要性就在这了，对链表做操作，最好加一个头结点
class Node:
    def __init__(self,x=0):
        self.next=None
        self.val=x

def Delete(l):
    if l==None:
        return
    i=Node(float('inf'))
    i.next=l
    j=l.next
    k=i
    while j!=None:
        if j.val==l.val:
            while j!=None and j.val==l.val:
                l.next=j.next
                j=j.next
            k.next=j
            l=j
            if j!=None:
                j=j.next
            else:
                break
        else:
            k=k.next
            l=l.next
            j=l.next
    Print(i)
    return i.next

def Print(l):
    tmp=l
    while tmp!=None:
        print(tmp.val)
        tmp=tmp.next

def main():
    l=Node(1)
    l.next=Node(2)
    l.next.next=Node(2)
    l.next.next.next=Node(3)
    l.next.next.next.next=Node(4)
    l=Delete(l)

main()