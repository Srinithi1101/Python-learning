#Return (factorial)
# def square(x):
#     return x**2
# print(square(5)+5)

# def square(x):
#     return x**2
# print(square(5))

# recursion

# def onetoten(n):
#     if n==0:
#         return 0
#     print(n)
#     return onetoten(n-1)
# onetoten(10)

#sum
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# print(sum(5))   


#list comparehensoin
# square =[i**2 for i in range(1,11)]
# print(square)

# square =[i+2 for i in range(1,11)]
# print(square)

#cube
# cube =[i**3 for i in range(1,11)]
# print(cube)

#task
# list=["apple","orange","banana"]
# for list in list:
#     print(list.upper())

# even=[i for i in range (1,11) if i %2 ==0]
# print(even)

# odd=[i for i in range (1,15) if i %3 ==0]
# print(odd)

#lambda function
# square=lambda x:x**2
# print(square(5))

# #Add
# add=lambda x,y:x+y
# print(add(5,10))

#multiple by 3 value
# multiple=lambda x,y:x*y
# print(multiple(3,5))

# biggest=lambda x,y:x if x>y else y
# print(biggest(5,6))

# n=lambda x: "Even" if x%2==0 else "odd"
# print(n(6))
# print(n(7))


# def fh(temp):
#     return(temp*9/5)+32
# c=[10,30,50,80]
# ctof=list(map(fh,c))
# print(ctof)

# def even_odd(n):
#     return("Even","odd")[n%2]
# a=[1,2,3,4,5]    
# result=list(map(even_odd,a))
# print(result)

#age vote
# def year (age):
#     return("Eligible","not eligible")[age<=18]
# a=[16,23,15,25]
# n=list(map(year,a))
# print(n)   

# #if else same line(even or odd)
# num=[15,25,30,40]
# oe=list(map(lambda x:"even" if x%2==0 else "odd",num))
# print(oe)
   
#filter
# def ispass(marks):
#     return marks >=35
# marks=[20,35,22,78]
# grade=list(filter (ispass,marks))
# print(grade)
