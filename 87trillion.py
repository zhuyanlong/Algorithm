#分酒问题
#有x容积的酒坛装满酒，有y容积(y>=x//2)和z容积(z>=y//2)的空酒坛，要求用y和z装x//2的酒
#换个想法思考这个问题就相当于我初始状态是(8,0,0)，最后要达到的状态是(0,4,4)，在这个过程中要判断下不要超越容积就行
def dfs(x,y,z):
    stack=[(x,y,z)]
    while stack:
        tmp=stack.pop()


        if a==0 and b==x//2 and c==x//2:
            return

    return


#检测环装链表，打破环，实现链表逆置
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Jiuding:
    #检测环,打破环
    def Cycle(self, head):
        if head == None or head.next == None:
            return head
        fast=head
        slow=head
        while fast!=None:
            fast=fast.next
            slow=slow.next
            if fast!=None:
                fast=fast.next
                if fast==slow:
                    break
        if fast==None:
            return self.reverseList(head)
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        slow=slow.next
        while slow.next!=fast:
            slow=slow.next
        slow.next=None
        return self.reverseList(head)

    #链表逆置
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        c=head.next
        p=c.next
        head.next=None
        while c.next!=None:
            c.next=head
            head=c
            c=p
            p=p.next
        c.next=head
        return c

def main():
    j=Jiuding()
    l=ListNode(1)
    l.next=ListNode(2)
    l.next.next=ListNode(3)
    l.next.next.next=ListNode(4)
    l.next.next.next.next=ListNode(5)
    l.next.next.next.next.next=ListNode(6)
    l.next.next.next.next.next.next=l.next.next.next
    t=j.Cycle(l)
    print(t.val)
    print(t.next.val)
    print(t.next.next.val)
    print(t.next.next.next.val)
    print(t.next.next.next.next.val)
    print(t.next.next.next.next.next.val)

main()