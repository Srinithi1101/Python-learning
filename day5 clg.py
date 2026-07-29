#(1 to 10)
for i in range(1, 11):
    print(i)
print()
#(10 to 1)
i = 10
while i >= 1:
    print(i)
    i -= 1
print()
#(odd numbers(1 tO 20))
for i in range(1, 21):
    if i % 2 != 0:
        print(i)
print()
#(even number(1 to 20))
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print()
#(1 to 10(6 break))
for i in range(1,11):
    if i==6:
        break
    print(i)

#(1 to 10(5 continue))
for i in range(1,11):
    if 1==5:
        continue
    print(i)

    
