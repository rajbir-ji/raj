# 1. EVEN OR ODD 
a=int(input("Enter a number:"))
if a%2==0:
  print("Number is Even")
else:
  print("Number is Odd")
# 2. Positive , Negative or Zero
a=int(input("Enter a number:"))
if a>0:
  print("Number is Positive")
elif a<0:
  print("Number is Negative")
else :
  print("Number is Zero")
# 3.Greatest of two numbers
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
if x>y:
  print("x is greater")
else:
  print("y is greater")
#  4.Pass or Fail
print("------RESULT------")
Marks=float(input("Enter the Marks:"))
if Marks>=33:
  print("PASS")
else:
  print("FAIL")