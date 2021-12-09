arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds(l):
    t=0
    for k in l:
        if k%2==1:
            t=t+k
    return t
print(sumOdds(arr))


