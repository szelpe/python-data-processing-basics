

file = open('names.txt', mode='r', encoding='utf-8')

lines = file.readlines()

people = []

for line in lines:
    parts = line.strip().split(',')
    name = parts[0]
    age = parts[1]
    height = parts[2]
    person = {
        'Name': name,
        'Age': age,
        'Height': height
    }
    people.append(person)



people2 = [
    {'Name': 'Peti', 'Age': '25', 'Height': '170'},
    {'Name': 'Laci', 'Age': '20', 'Height': '180'},
    {'Name': 'Mari', 'Age': '10', 'Height': '140'}
]

file_to_write = open('people.csv', mode='w', encoding='utf-8')

lines_to_write = []

for person in people2:
    line = ''
    for item in person.values():
        line += item + ','
    line += '\n'
    lines_to_write.append(line)

file_to_write.writelines(lines_to_write)
