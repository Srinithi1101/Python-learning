#create a text file
file = open("message.txt", "w")
file.write("Welcome to Python File Handling.")
file.close()
file = open("message.txt", "r")
print(file.read())
file.close()
print()

#Append to a text file
file = open("notes.txt","w")
file.write("Python is easy.\n")
file.close()
file = open("notes.txt","a")
file.write("I am learning File Handling.")
file.close()
file = open("notes.txt","r")
print(file.read())
file.close()
print()

#create a csv file
import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Rahul", 20])
    writer.writerow(["Priya", 21])
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print()

#create a json file
import json
employee = {"name": "Rahul","age": 25,"city": "Chennai"}

with open("employee.json", "w") as file:
    json.dump(employee, file)

with open("employee.json", "r") as file:
    data = json.load(file)
    print(data)
print()

#Append Data to a CSV file
import csv
with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price"])
    writer.writerow(["Pen", 20])
with open("products.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Pencil", 10])
with open("products.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print()    
