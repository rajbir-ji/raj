try:
    a=int(input("Enter a numerator: "))
    b=int(input("Enter a denominator: "))
    result=a/b

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid value.")
else:
    print("The result is:", result)
finally:
    print("Execution completed.")