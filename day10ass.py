#print even number (list)
n=[12,7,25,18,30,9,4]
for i in n:
    if i%2 ==0:
        print(i)
print()
#count number(list)
names=["Arun","Priya","Rahul","Meena","John"]
print("Number of names:",len(names))
print()
#print unique elements (SET)
cities={"Chennai","Madurai","Trichy","Coimbatore"}
for city in cities:
    print(city)
print()
#Find highest mark(Dictionary)
marks={
    "Asha":78,
    "Ravi":92,
    "Kumar":65,
    "Divya":88
    }
print("Highest mark:",max(marks.values()))
print()
#count passed students(dictionary)
marks={
    "Arun":45,
    "Priya":76,
    "Jojn":50,
    "MEena":38,
    "Rahul":81
    }
count=0

for mark in marks.values():
      if mark >=50:
        count+=1
print("Passed students:",count)      
      
      
    
