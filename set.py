set={10,20,30,40}
set.add(50)
set.update([60])
print(set)
for i in set:
     print(i)
wet={10,20,30,40,56,46}
wet.remove(20)
wet.discard(40) 
wet.difference_update({30,46,56}) 
wet.pop()
print(wet)
for i in wet:
     print(i)


