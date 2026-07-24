"""
with open('students.csv') as file:
    for line in file:
        # row = line.rstrip().split(',') 
        name, house = line.rstrip().split(',') 
        #print(f'{row[0]} is in {row[1]}')
        print(f'{name} is in {house}')
        

#   SORTED   SORTED   SORTED   SORTED   SORTED   SORTED   SORTED   SORTED   SORTED   
students = []

with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        students.append(f'{name} is in {house}')

for student in sorted(students):
    print(student)


"""
students = []

with open('students.csv') as file:
    for line in file:
        name, home = line.rstrip().split(',')
        """
        student = {}
        student["name"]=name        
        student["house"]=house
        students.append(student)
        """
        
        student = {'name':name, 'home':home}
        students.append(student)

#def get_name(student):
#    return student['name']


for student in sorted(students, key=lambda student: student['name']):  # key=get_name
    print(f'{student['name']} is from {student['home']}')

