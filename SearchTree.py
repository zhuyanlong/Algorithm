#二叉搜索树，普通二叉树插着没意义
#不知为何它的后序遍历和我理论得出的后序遍历是不一样的
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BTree:
    def __init__(self):
        self.root=None
    def treeInsert(self,value):
        #用来定位待插入节点的父节点
        y=None
        x=self.root
        t=TreeNode(value)
        while x!=None:
            y=x
            if t.val<x.val:
                x=x.left
            else:
                x=x.right
        if y==None:
            self.root=t
        else:
            if t.val<y.val:
                y.left=t
            else:
                y.right=t
    def inorderTravel(self,x):
        if x!=None:
            self.inorderTravel(x.left)
            print(x.val)
            self.inorderTravel(x.right)
        else:
            return

    def preorderTravel(self,x):
        if x!=None:
            print(x.val)
            self.preorderTravel(x.left)
            self.preorderTravel(x.right)
        else:
            return
    def postorderTravel(self,x):
        if x!=None:
            self.preorderTravel(x.left)
            self.preorderTravel(x.right)
            print(x.val)
        else:
            return

def main():
    t=BTree()
    
    t.treeInsert(1)
    t.treeInsert(2)
    t.treeInsert(3)
    
    t.treeInsert(4)
    t.treeInsert(5)
    t.inorderTravel(t.root)
    print()
    print("a",a)
    t.preorderTravel(t.root)
    print()
    t.postorderTravel(t.root)

main()
