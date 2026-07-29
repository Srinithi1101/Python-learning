#ATM pin verification
card=input("ATM card is Inserted?(yes/No):")    
if card == "yes":
    pin = int(input("Enter PIN: "))
    if pin == 1234:
        print("Welcome! Transaction Successful.")
    else:
        print("Invalid PIN.")
else:
    print("Please insert your ATM card.")
print()

#positive or negative
num=int(input("Enter the number:"))
if num!= 0:
      print("The numer is not zero")
      if num>0:
          print("the number is positive")
      else:
          print("The number is negative") 
else:
    print("The number is zero")

#largest three numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b and a>c:
      print("Largest number is ",a)
elif b>a and b>c:
    print("Largest number is",b)
else:
    print("Largest number is",c)
print()

#leap year
year=int(input("Enter the Year:"))
if(year%400==0):
         print("Leap year")
else:

    print("It is not leap year")
print()

#Electricity bill
units=int(input("Enter your bill:"))
if units<=100:
          bill=units*2 
elif units <=300:

    bill=(100*2)+((units-100)*3)
else:
    bill=(100*2)+(200*3)+((units-300)*5)
    print("Electricity bill=Rs",bill)
print()

#Day of the week
day=int(input("Enter day number (1-7):"))
if day == 1:
        print("Sunday")
elif day == 2:
    print("MOnday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day== 7:
    print("Saturday")
else:
    print("Invalid")
print()

#Driving License Eligibility
age=int(input("Enter your age:"))
if age>=18:
        print("Eligible for Driving License:")
else:
    print("Not Eligible for Driving License:")
    print()

#Login System
username=input("Enter username:")
password=input("Enter password:")
if username=="kavii" and password == "1234":
    print("Login successful")
else:
    print("invalid username or password")
    print()
#Examination Eligibility
attendance=float(input("Enter attendance percentage:"))
if attendance>=75:
    print("Eligible for Examination")
else:
    print("Not eligible for Examination")
    print()
    
#Student  grade  calculator
marks=int(input("Enter the marks:"))
if marks >=90:
    print("Grade A") 
elif marks >=80:
    print("Grade B") 
elif marks >=70:
    print("Grade c")
elif marks >=60:
    print("Grade E")
else:
    print("Grade F")
print()    
     
#Online Shopping System
username=input("Enter username:")
password=input("Enter password:")
if username=="deva" and password == "4567":
    print("Login successful")
    balance =float(input("Enter account balance:"))
    amount=float(input("Enter order amount:"))
    if balance>=amount:
        print("Order Placed Successfully")
    else:
        print("Insufficienr Balance")
else:
    print("Login failed")
    


