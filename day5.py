#LOOP
i=1
while i<10:
    print("Hello")
    i+=1

i=True
while i:
    password=input("Enter the password:")
    if password=="1234":
        print("login successfull")
        i=False

i=1
while i<=10:
    print(i)
    i+=1

i=1
while i<=10:
    print(i)
    if i==5:
        break
    i+=1

i=1
while i<=10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1   

#for loop
name="deva"
for letter in name:
    print(letter)

floders=["floder1","floder2","floder3"]
target=input("Enter the floder name:")
found=True
for floder in floders:
    if floder ==target:
        print("floder found")
        found=True
    if not found:
        print("no match found")

for i in range (1,5):
    print(i)

for i in range (2,20,2):
    print(i)  

for i in range(5,100,5):
    print(i)


#start,stop,step
for i in range(5,100,5):
    print(i)
print()

for i in range(100,1,-5):
  print(i)
print()

for i in range(2,21):
    if i%2==0:
        print(i)
print()    
for i in range(1,11):
    if i==5:
        continue
    print(i)
print()    
n=int (input("Enter N:"))
for i in range(2,n+1,2):
    print(i)
