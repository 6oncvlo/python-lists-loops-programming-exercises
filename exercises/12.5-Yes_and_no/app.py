theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def bi(k):
    if k==0:
        return "woko"
    else:
        return  "wiki"


re=list(map(bi, theBools))
print(re)