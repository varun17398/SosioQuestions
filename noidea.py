# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
m=input()
l=[]
for i in range(0,int(n)):
    a=int(input())
    l.append(a)
l1=[]
l2=[]
for i in range(0,int(m)):
    b=int(input())
    l1.append(b)
for i in range(0,int(m)):
    c=int(input())
    l2.append(c)

happy=0
unhappy=0
for i in l:
    if(i in l1):
        happy=happy+1
    if(i in l2):
        unhappy=unhappy+1
print(happy-unhappy)


