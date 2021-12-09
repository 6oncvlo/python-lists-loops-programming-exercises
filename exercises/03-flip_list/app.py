arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
new_list=[]
for k in range(len(arr)):
    new_list.append(arr[-1-k])
print(new_list)
