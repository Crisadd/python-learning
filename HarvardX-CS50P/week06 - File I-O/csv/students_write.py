import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    #writer = csv.writer(file)
    #writer.writerow([name, home])
    
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})
<<<<<<< HEAD
    
=======
    
>>>>>>> c46cbde77d381346456d45c4bc20f3c615c6e9a7
