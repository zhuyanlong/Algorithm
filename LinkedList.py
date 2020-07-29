class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def addNode(self,x):
        l=ListNode(x)
        tmp=self
        while tmp.next!=None:
            tmp=tmp.next
        tmp.next=l

    def printNode(self):
        tmp=self
        res=[]
        while tmp.next!=None:
            res.append(tmp.val)
            tmp=tmp.next
        res.append(tmp.val)
        print(res)

def main():
    l=ListNode(1)
    l.addNode(1)
    l.addNode(2)
    l.addNode(2)
    l.addNode(3)
    l.addNode(3)
    l.printNode()

main