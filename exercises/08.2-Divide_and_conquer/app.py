list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(l):
    odd=[]
    even=[]
    for k in l:
        if k%2==1:
            odd.append(k)
        else:
            even.append(k)
    return [odd,even]
print(merge_two_list(list_of_numbers))

