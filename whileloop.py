# 1.while loop 
cnt=0
while(cnt<5):
    print("Hello World")
    cnt=cnt+1
print()
# 2.
cnt=0
while(cnt<=10):
    print(cnt)
    cnt=cnt+1
    print("Hello World")
else:
    print("Loop ended")
print()
# 3.break statement
for i in "geeksforGeeks":
    if i=="e":
     break
print("Current Iteration:",i)
print()
# 4.continue statement
for i in "geeksforGeeks":
    if i=="ge":
     continue
    print("Current Iteration:",i)
print()
# 5.pass statement
for i in "geeksforGeeks":
    if i=="e":
     pass
    print("Current Iteration:",i)
