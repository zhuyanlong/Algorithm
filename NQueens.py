#参考The maze程序，The Maze使用BFS
#现在简化了问题，我只需要寻找N皇后问题的一个解
#目前做出改变，假设是stack和board始终保持同层
class Solution:
    def solveNQueens(self, n):
        res=[]
        for i in range(n):
            #候选节点集
            #这个题解的一个关键就在于要去记录stack中节点的层次，因为我要回溯，所以必须记录stack的层次
            #另一个成功的关键就是，当我们在找到一个解以后，我最初的做法是把board清空，然后改成将board恢复初始值，但这样其实都不对
            #因为这样做实际上相当于把board和stack没能保持同层，带来的结果就是，会遗漏有些解
            stack=[(0,i)]
            board=[]
            while stack:
                top=stack.pop()
                while len(board)!=top[0]:
                    board.pop()
                board.append(top[1])
                position=list(range(n-1,-1,-1))
                for i in position:
                    if self.check(board,i):
                        stack.append((len(board),i))
                if len(board)==n:
                    #这个地方要注意，不能直接res.append(board)，因为实际上只是存了指针，数据会变
                    res.append(board.copy())
        print(res)
        # output=self.printNQueens(res)
        return res

    def check(self,board,j):
        k=len(board)
        for i in range(k):
            if board[i]==j:
                return False
            if j==board[i]+k-i or j==board[i]-(k-i):
                return False
        return True

    # def printNQueens(self,res):
    #     output=[]
    #     for i in range(len(res)):
    #         tmp=['.'*len(res[i])]*len(res[i])
    #         for j in range(len(res[i])):
    #             tmp[j][res[i]]='Q'
    #         output.append(tmp)
    #     return output


def main():
    s=Solution()
    output=s.solveNQueens(4)
    # print(output)

main()
