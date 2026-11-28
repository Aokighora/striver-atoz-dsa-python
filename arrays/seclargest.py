import numpy as np
def main():
    print(secl())
    print(sll())

def secl():
    d=np.array([-1,-5,9,0,7,-3])
    l=float('-inf')
    for i in range(1,len(d)):
        if d[i]>l:
            l=d[i]
#O(2N)
        
    sl=float('-inf')
    for i in range(len(d)):
        if d[i]>sl and d[i]!=l:
            sl=d[i]
    return sl

#O(N)
def sll():
    d=np.array([-1,-5,9,0,7,-3])
    l=float('-inf')
    sl=float('-inf')
    for i in range(len(d)):
        if d[i]>l:
            sl=l
            l=d[i]
        elif d[i]>sl and d[i]!=l:
            sl=d[i]
    return sl if sl!=float('-inf') else -1

main()