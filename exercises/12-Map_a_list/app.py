Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:
    return 9*x/5+32
   
result = list(map(fahrenheit_values, Celsius_values))
print(result)
