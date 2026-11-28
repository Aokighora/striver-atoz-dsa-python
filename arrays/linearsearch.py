import numpy as np
d=np.array([1,3,5,6,8,9])
num=int(input("num: "))
index=-1
for i in range(len(d)):
    if d[i]==num:
        index= i 
print(index)
    


