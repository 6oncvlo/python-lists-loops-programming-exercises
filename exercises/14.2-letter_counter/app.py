
par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"
par=par.lower()
counts = {}
#your code go here:
for k in par:
    if k!=" " and k in counts:
        counts[k]=counts[k]+1
    elif k!=" " and not k in counts:
        counts[k]=1
print(counts)

