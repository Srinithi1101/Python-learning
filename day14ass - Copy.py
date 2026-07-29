#Divide two number
try:
    num1=float(input("Enter  the  first number:"))
    num2=float(input("Enter the second number:"))
    result=num1/num2
    print("Result:",result)
except ZeroDivisionError:
    print("Cannot divide by zero")
print()
#Integer Input
try:
    age=int(input("Enter your age:"))
    print("Age:",age)
except ValueError:
    print("Please enter a valid number")
print()    

#List index
fruits=["Apple","Banana","Mango"]
try:
    index=int(input("Enter index:"))
    print("Fruit:",fruits[index])
except IndexError:
    print("Invalid index.")
print()    
#Age validation
class InvalidAgeError(Exception):
    pass
try:
    age=int(input("Enter age:"))
    if age<18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Valid age.")
except InvalidAgeError as e:
    print(e)
print()

#Password length
class WeakPasswordError(Exception):
    pass
try:
    password=input("Enter password:")
    if len(password)<8:
        raise WeakPasswordError("Password must be at least 8 characters long.")
    print("Strong password.")
except WeakPasswordError as e:
    print(e)
print()    

               
