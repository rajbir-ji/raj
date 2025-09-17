n=4
for i in range(1,4):
  for j in range(1,4): 
      print(f"{i}*{j}={i*j}")
  print("--------")
# square pattern
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()