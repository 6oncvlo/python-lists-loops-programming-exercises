import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

l=[]
for k in people:
	l.append((k["birthDate"]))

age_list=list(map(calculateAge, l))
print(age_list)

name_list = list(map(lambda person: person["name"] , people))
print(name_list)

res=[]
for k in range(len(name_list)):
	res.append("Hello, my name is "+name_list[k]+ " and I am "+ str(age_list[k])+" years old")
print(res)


