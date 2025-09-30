ages=list(map(float,input("Enter ages: ").split()))
n=len(ages)
count=sum(1 for a in ages if 60<a<90)
print("count=",count)
