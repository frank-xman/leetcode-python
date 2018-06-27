import sys
def notwo(w,h): 
    if w % 4 == 0 or h % 4 == 0:
        result = w * h / 2
    elif w % 2 == 0 and h % 2 == 0:
        result = w * h / 2 + 2
    else:
        result = w * h / 2 + 1
    return result
    
if __name__=='__main__':
    M=[int(i) for i in raw_input().split()]
    print notwo(M[0],M[1])