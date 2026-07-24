import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    #writer = csv.writer(file)
    #writer.writerow([name, home])
    
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})
    
    
    1.20.17     1.20.17     1.20.17     1.20.17     1.20.17     1.20.17     1.20.17     1.20.17 