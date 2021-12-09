def lyrics_generator(l):
    m=""
    for k in range(len(l)):
        if l[k]==0:
            m=m+" Boom "
        elif k>1 and l[k]==1 and l[k-1]==1 and l[k-2]==1:
            m=m+" Drop the base !!!Break the base!!! "
        else:
            m=m+" Drop the base "
    return m



# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
