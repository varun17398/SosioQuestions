def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    s=n/k
    i=0
    l1=[]
    while(i<n):
        l=[]
        for j in range(0,k):
            l.append(string[i])
            i=i+1
        #s1=''.join(l)
        l1.append(l)
    #print(len(l1))
    for j in range(0,len(l1)):
        #print(l1[j][j])
        del l1[j][j]
    l2=[]
    for j in range(0,len(l1)):
        s1=''.join(l1[j])
        print(str(s1)+'\n')
    pass




    

merge_the_tools('AABCAAADA',3)

#if __name__ == '__main__'
