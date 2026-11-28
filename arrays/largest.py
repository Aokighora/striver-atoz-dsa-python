#O(N)
import numpy as np
def main():
    print(largest())

def largest():
    d=np.array([-1,3,-5,6,8,9,-5,0,7,-3])
    l=d[0]
    for i in range(1,len(d)):
        if d[i]>l:
            l=d[i]
    return l

main()
        