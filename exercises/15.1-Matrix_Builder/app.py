#Import random
import random
#Create the function below:
def matrixBuilder(n):
    res=[]
    for k in range(n):
        l=[]
        for j in range(n):
            l.append(1)
        res.append(l)
    return res
print(matrixBuilder(3))