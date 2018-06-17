def calbin(num):
    res=0
    while num:
        num=num/2
        res+=1
    return res
def mixcolor(n,A):
    for i in xrange(n-1):
        A[i:n]=sorted(A[i:n],reverse=True)
        tmp1=calbin(A[i])
        for j in xrange(i+1,n):
            tmp2=calbin(A[j])
            if tmp1==tmp2:
                A[j]=A[i]^A[j]
    res=[i for i in A if i!=0]
    return len(res)
'''
for example:
    1 3 7
    transform to bin(x):
        001
        011
        111
    cal the matirx of whatever(i don`t konw how to write in eng of the tr(M))
    turn out the tr(M)=3
    
    to return 3


'''
    
     
if __name__=='__main__':
    n=int(raw_input())
    A=[int(i) for i in raw_input().strip().split(' ')]
    print mixcolor(n,A)