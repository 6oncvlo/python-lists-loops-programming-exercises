
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello=[]
for k in my_list:
    if type(k)==dict or type(k)==list:
        hello.append(k)
print(hello)
