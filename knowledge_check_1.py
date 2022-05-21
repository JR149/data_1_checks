#Statement to print hello world
print('\tHello World!\n',"\tHope you're having a great day!")

#Populated list
cars = [
    {'Make' : 'Kia', 'Model' : 'Soul', 'Year' : 2022},
    {'Make' :'Kia', 'Model': 'Rio', 'Year' : 2021},
    {'Make' : 'Chevy', 'Model': 'Bolt EUV', 'Year' : 2022}
]
#Value from populated list
print(cars[1])

#Type for cars
print(type(cars[0]))

#Making a dictionary with 2 keys and values
for item in cars:
    print(item['Make'], item['Year'])
    

for item in cars:
    print(item['Make'])

#Tuple
storm = ('rain', 'thunder', 'hail', 'sleet')
print(storm[2]) 



