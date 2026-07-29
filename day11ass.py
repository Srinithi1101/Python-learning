#funtion welcome name
def welcome(name):
    print("Welcome,",name+"!")
welcome("Alice")
print()

#function square(num)
def square(num):
    print(num*num)
square(6)
print()
#Largest two numbers
def largest(a,b):
    if a>b:
        print(a)
    else:
        primt(b)
largest(15,6)
print()
#count vowels
def count_vowels(word):
 count=0
 for ch in word.lower():
    if ch in "aeiou":
        count+=1
 print(count)
count_vowels("Education")
print()
#Calculate Total Price
def total_price(price,quantity):
    print(price*quantity)
total_price(120,4)    
