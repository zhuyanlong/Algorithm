class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelTraversal(root):
    if root==None:
        return []
    res=[]
    stack=[(root,0)]
    while stack:
        tmp=stack.pop()
        if len(res)==tmp[1]:
            res.append([tmp[0].val])
        else:
            res[tmp[1]].append(tmp[0].val)
        if tmp[0].right:
            stack.append((tmp[0].right,tmp[1]+1))
        if tmp[0].left:
            stack.append((tmp[0].left,tmp[1]+1))
    return res

def main():
    t=TreeNode(1)
    t.left=TreeNode(2)
    t.right=TreeNode(3)
    t.left.left=TreeNode(4)
    t.left.right=TreeNode(5)
    t.right.left=TreeNode(6)
    t.right.right=TreeNode(7)
    print(levelTraversal(t))

main()
