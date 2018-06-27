def repaa(A,B):
    res=0
    for i in xrange(len(A)+1):

        if helper(A[:i]+B+A[i:]):
            res+=1
    return res

def helper(strings):
    n=len(strings)
    i,j=0,n-1
    while i<j:
        if strings[i]==strings[j]:
            i+=1
            j-=1
        else:
            return False
    return True   
    
if __name__=='__main__':
    A=raw_input().strip()
    B=raw_input().strip()
    print repaa(A,B)