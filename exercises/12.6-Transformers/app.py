incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
def my_var(x):
	j=x["name"]+" "+x["lastName"]
	return j
#print(my_var({ "name": 'Mario', "lastName": 'Montes' }))

transformedData=list(map(my_var, incomingAJAXData))
print(transformedData)
