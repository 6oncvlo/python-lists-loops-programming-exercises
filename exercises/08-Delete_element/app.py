people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    l=[]
    for k in people:
        if k!=person_name:
            l.append(k)
    return  l

    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))