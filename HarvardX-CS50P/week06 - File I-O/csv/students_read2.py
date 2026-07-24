import csv

students = []

with open('students.csv') as file:
    reader = csv.reader(file)

    #for row in reader:
    #    students.append({"name": row[0], "home": row[1]})
        
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student['name']):  # key=get_name
    print(f"{student['name']} is from {student['home']}")

