def getStep(n,x,y):
    step=[]
    for i in xrange(n):
        step.append(x[i]+y[i]-2)
    return min(step)
 
n=int(input())
x=map(int,raw_input().strip().split())
y=map(int,raw_input().strip().split())
print getStep(n,x,y)