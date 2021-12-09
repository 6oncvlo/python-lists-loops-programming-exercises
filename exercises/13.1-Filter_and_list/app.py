
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def f1(x):
    return x[0]=="R"

resulting_names=list(filter(f1, all_names))
print(resulting_names)




