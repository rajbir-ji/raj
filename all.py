# 1.Using only stop
for i in range(5):
    print(i)
# 2.Using both start and stop
for j in range(2,7):
    print(j)
# 3.Using only start,stop,step
for k in range(1,10,2):
    print(k)
# 4.Using negative step
for l in range(10,0,-1):
    print(l)
# simple for loop questions
# 1.write a program to print numbers from 1 to 10
for m in range(1,11):
    print(m)
    print()
# 2.write a program to print  even numbers from 2 to 20
for n in range(2,21,2):
    print(n)
    print()
# 3.write a program to print multiplication table of 5
for p in range(5,51,5):
    print(p)
    print()
# 4.write a program to calculate the sum of numbers from 1 to 50
sum=0
for q in range(1,51):
    sum=sum+q
print(sum)
print()
# 5.write a program to print squares of numbers from 1 to 10
for r in range(1,11):
    print(r*r)
    print()
# nested loop patterns
# 6. write a program to print a square pattern of size 5
n=5
for i in range(n,0,-1):
        for j in range(n):
            print("*", end=" ")
        print()
# 7. write a program to print a right angled triangle pattern of *
for i in range (5,0,-1):
    for j in range(i):
      print("*",end=" ")
    print( )
# 8. write a program to print a number in a triangle pattern
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
# 9. write a program to print a reverse triangle pattern
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
# 10. write a program to print a pyramid pattern
for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
# 11.write a program to print multiplication table of any number
num=(input("Enter a number: "))  
for i in range(1,11):
    print(num,"*",i,"=",num*i)
# 12.write a program to print multiplication table of 2 to 5
for i in range(2,11):
    print("Multiplication table of",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print()
# 3.write a program to print multiplication table of 10 in reverse order
n=int(input("Enter a number: "))
for i in range(n,0,-1):
    print("10 *",i,"=",n*i)

