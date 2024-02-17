

peti = {
    'Name': 'Peti',
    'Age': 25
}

peti['Height'] = 170
peti['Age'] = 26

# for key in peti.keys():
#     print(key + " " + str(peti[key]))

for (key, value) in peti.items():
    print(key + ' -> ' + str(value))

laci = {
    'Name': 'Laci',
    'Age': 20
}

mari = {
    'Name': 'Mari',
    'Age': 13
}

people = [ peti, laci, mari ]

# print(people)

people2 = [
    {'Name': 'Peti', 'Age': 26, 'Height': 170},
    {'Name': 'Laci', 'Age': 20},
    {'Name': 'Mari', 'Age': 13}
]

# for person in people2:
#     print("Name: " + person['Name'])
#     print("Age: " + str(person['Age']))

for person in people2:
    for (key, value) in person.items():
        print(key + ' -> ' + str(value))
