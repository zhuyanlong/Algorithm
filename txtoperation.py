import csv
datadict={}
stoplist=[]
picture=['Auge','Augen','Baum','Brot']

def loadData(fileName):   
    with open(fileName,encoding='utf-8') as txtData:
        lines=txtData.readlines()
        # print(lines)
        for line in lines:
            # print(line)
            lineData=line.strip().split(' ')
            # print(lineData)
            for item in lineData:
                tmp=item.strip().strip('.').strip(',').strip('"')
                if tmp!='':
                    if tmp not in datadict:
                        datadict[tmp]=1
                    else:
                        datadict[tmp]+=1
        # data=sorted(data.items(),key=lambda item:item[1])
    # print(datadict)
    # return datadict

def loadStop(filename):
    with open(filename, encoding='utf-8') as txtData:
        lines=txtData.readlines()
        # print(lines)
        for line in lines:
            lineData=line.strip().split(' ')
            # print(lineData[0])
            tmp=lineData[0].strip('\n').strip().strip('.').strip(',').strip('"')
            if tmp!='':
                if tmp[0].isupper():
                    stoplist.append(tmp)
    # print(stoplist)

def q6(N):
    result=[]
    data=list(reversed(sorted(datadict.items(),key=lambda item:item[1])))
    for item in data:
        if item[0][0].isupper():
            if item not in stoplist:
                result.append(item)
                N-=1
                if N==0:
                    break
    print(result)
    return result

def q7():
    filename="Grimm.txt"
    result=[]
    with open(filename,encoding='utf-8') as txtData:
        lines=txtData.readlines()
        # print(lines)
        for line in lines:
            lineData=line.strip().split(' ')
            # print(lineData)
            for item in picture:
                if item in lineData:
                    result.append((item,line.strip('\n').strip(),"/static/"+item+".jpg"))
    return result

def q8():
    result3 = []
    file = 'Grimm.txt'
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            row = []
            row.append(line)
            isNoun = False
            lineData=line.strip().split(' ')
            # print(lineData)
            for s in lineData:
                if s.istitle() and isNoun:
                    # print(s)
                    # print(line)
                    row.append(s)
                    isNoun = True
                    result3.append(row)
                if not s.istitle():
                    isNoun = False
                if s.istitle() and not isNoun:
                    isNoun = True
    # print(result3)
    return result3

def q9(w1,w2,n):
    data=[]
    result=[]
    i=0
    j=0
    fileName="Grimm.txt"
    with open(fileName,encoding='utf-8') as txtData:
        lines=txtData.readlines()
        # print(lines)
        for line in lines:
            # print(line)
            lineData=line.strip().split(' ')
            # print(lineData)
            for item in lineData:
                tmp=item.strip().strip('.').strip(',').strip('"')
                if tmp!='':
                    data.append(tmp)
    for k in range(len(data)):
        if data[k]==w1:
            n-=1
            if n==0:
                i=k
        if data[k]==w2:
            j=k
    # print(len(data))
    result.append(abs(i-j))
    count=10
    tmp=[]
    for k in range(j,i+1):
        tmp.append(data[k])
        count-=1
        if count==0:
            break
    tmp=" ".join(tmp)

    result.append(tmp)
    # print(result)
    return result

loadData("Grimm.txt")
loadStop("Grimm.txt")

q8()

# q7()s

# q6(5)
# q9("und","Einem",5)