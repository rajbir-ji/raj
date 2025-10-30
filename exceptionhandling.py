# exceptionhandling.py
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
# base exception handling example
try:
    raise BaseException("This is a base exception")
except BaseException as e:
    print("Caught BaseException:", e)
# Exception 
try:
    raise Exception("This is a generic exception")
except Exception as e:
    print("Caught Exception:", e)
# ArthmeticError
try:
    raise ArithmeticError("This is an arithmetic error")
except ArithmeticError as e:
    print("Caught ArithmeticError:", e)
# ZeroDivisionError
try:
    result=10/0
except ZeroDivisionError as e:
    print("Caught ZeroDivisionError:", e)
# OverflowError
import math
try:
    result=math.exp(1000)
except OverflowError as e:
    print("Caught OverflowError:", e)
# floating point error
import numpy as np
np.seterr(all='raise')
try:
    np.divide(1,0)
except FloatingPointError as e:
    print("Caught FloatingPointError:", e)
# AssertionError
try:
    assert 1==2, "Assertion failed"
except AssertionError as e:
    print("Caught AssertionError:", e)
# AttributeError
class MyClass:
    pass
obj=MyClass()
try:
    obj.some_attribute()
except AttributeError as e:
    print("Caught AttributeError:", e)
# index error
my_list=[1,2,3]
try:
    element=my_list[5]
except IndexError as e:
    print("Caught IndexError:", e)
# KeyError
d={"key1":"value1"}
try:
    value=d["key2"]
except KeyError as e:
    print("Caught KeyError:", e)
# memory error
try:
    li=[1]*(10**10)
except MemoryError as e:
    print("Caught MemoryError:", e)
# NameError
var=12
try:
    print(var)
except NameError as e:
    print("Caught NameError:", e)
# OSError(andrelated errors)
try:
    open("non_existent_file.txt")
except FileNotFoundError as e:
    print("FileNotFoundError caught:", e)
except OSError as e:
    print("Caught OSError:", e)


