#快手一面，最长回文字符串
#可以直接遍历，利用前后拓展，寻找最长的回文字符串
#回文字符串包括两种情况，一个是aba，另一个是abba，所以要匹配这两种不同的字符串
class Solution:
    def longestPalindrome(self, s):
        #用来储存最终的结果
        start=0
        end=0
        for i in range(len(s)):
            l1=self.expand(s,i,i)
            l2=self.expand(s,i,i+1)
            #还原坐标
            if l1>l2:
                tmp1=int(i-l1//2)
                tmp2=tmp1+l1
            else:
                tmp1=int(i-l2//2)+1
                tmp2=tmp1+l2
            if (tmp2-tmp1)>(end-start):
                start=tmp1
                end=tmp2
        # print(start,end)
        return s[start:end]

    def expand(self,s,left,right):
        #判断是否是回文串，从一个中信位置向外扩展
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        #多计算的部分减掉
        left+=1
        right-=1
        return right-left+1

def main():
    s="ababab"
    sol=Solution()
    print(sol.longestPalindrome(s))

main()