# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
l=[]
flag=[]
for i in range(0,int(n)):
    word=input()
    l.append(str(word))
    flag.append(0)
res=[]
for i in range(0,int(n)):
    count=1
    for j in range(i+1,int(n)):
        if(l[i]==l[j] and flag[j]==0):
            count=count+1
            flag[j]=1
    res.append(count)
c=0
for i in range(0,int(n)):
    if(flag[i]==0):
        c=c+1
print(c)
for j in range(0,int(n)):
    if(flag[j]==0):
        print(res[j])

