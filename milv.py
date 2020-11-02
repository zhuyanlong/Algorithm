#题目见onenote，幂律面试
#Q1
#a=[5,3,1,5,4]
#b=[5,3]
#返回b中元素在a中的位置
def findIndex(a,b):
  result=[]
  for item in b:
    judge=0
    while item in a[judge:]:
      print(item,a.index(item))
      if judge==0:
        result.append(a[judge:].index(item))
#       else:
        judge=a[judge:].index(item)
        result.append(a.index(item)+1)
#       a.remove(item)
      print("list",a)
  return result

def findIndex(a,b):
  result=[]
  for item in b:
    for i in range(len(a)):
      if item==a[i]:
        result.append(i)
  return result

def main():
  a = [5, 3, 1, 5, 4]
  b = [5, 3]
  print(findIndex(a,b))

#这是一个树状结构
nodes = [
    {
        "id": "A",
        "pid": "-1"
    },
    {
        "id": "A-1",
        "pid": "A"
    },
    {
        "id": "A-2",
        "pid": "A"
    },
    {
        "id": "A-3",
        "pid": "A"
    },
    {
        "id": "A-2-1",
        "pid": "A-2"
    },
    {
        "id": "A-2-2",
        "pid": "A-2"
    },
    {
        "id": "A-2-3",
        "pid": "A-2"
    }
]

re = [
  "/A",
  "/A/A-1"
]

def constructTree(node):
  result=[]
  for item in node:
    if item['pid']=="-1":
      result.append("/"+item['id'])
    else:
      tmp="/"+item['pid']+"/"+item["id"]
#       print(tmp)
      tmppid=item['pid']
      for i in range(len(node)):
        if node[i]['id']==tmppid:
          if node[i]['pid']=="-1":
            break
          else:
            tmp="/"+node[i]["pid"]+tmp
            tmppid=node[i]["pid"]
      result.append(tmp)
  return result

print(constructTree(nodes))

#Q3
array = [
    [1, 1, 5, 2],
    [1, 1, 7, 3],
    [30, 30, 30, 9]
]

ret = 4

def minPath(path):
  if len(path)==0:
    return
  printpath=[[0 for i in range(len(path[0]))] for i in range(len(path))]
  dp=[[0 for i in range(len(path[0]))] for i in range(len(path))]
  for i in range(len(path[0])):
    dp[0][i]=path[0][i]
  if len(path)==1:
    return min(path[0])
  for i in range(1,len(path)):
    for j in range(len(path[0])):
      tmp=[]
      if j-1>=0:
        tmp.append(dp[i-1][j-1])
      if j>=0 and j<len(path[0]):
        tmp.append(dp[i-1][j])
      if j+1<len(path[0]):
        tmp.append(dp[i-1][j+1])
      dp[i][j]=path[i][j]+min(tmp)
  return min(dp[-1])
  
print(minPath(array))


#Q4
def maxLength(words):
  maxlen=0
  for i in range(len(words)-1):
    for j in range(i,len(words)):
      if not set(words[i])&set(words[j]):
        tmp=len(words[i])*len(words[j])
        if tmp>maxlen:
          maxlen=tmp
  return maxlen

# words=["abcw","baz","foo","bar","xtfn","abcdef"]
# words=["a","ab","abc","d","cd","bcd","abcd"]
words=["a","aa","aaa","aaaa",]
print(maxLength(words))