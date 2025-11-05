#zero division exception handling
a =5
b =0
try:
    print(a/b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")


#x=[10,20,30,45]
#print(x[5])  --index error exception
x = [10, 20, 30, 40]

try:
    print(x[5])
except IndexError:
    print("IndexError: list index out of range")


#value error exception handling
try:
    int("abc")
except ValueError:
    print("ValueError: invalid literal for int()")


#key error exception handling
my_dict = {'a': 1, 'b': 2}
try:
    print(my_dict['c'])
except KeyError:
    print("KeyError: 'c' not found in dictionary")

#type error exception handling
try:
    print("hello" + 5)
except TypeError:
    print("TypeError: can only concatenate str (not 'int') to str")

#attribute error exception handling
try:
    num = 10
    num.append(5)
except AttributeError:
    print("AttributeError: 'int' object has no attribute 'append'")

#import error exception handling
try:
    import non_existent_module
except ImportError:
    print("ImportError: No module named 'non_existent_module'")

#file not found error exception handling
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("FileNotFoundError: 'non_existent_file.txt' not found")

#overflow error exception handling
import math
try:
    math.exp(1000)
except OverflowError:
    print("OverflowError: result too large to be expressed within range")

#memory error exception handling
try:
    a = 'a' * (10**10)
except MemoryError:
    print("MemoryError: Unable to allocate memory")

#stop iteration exception handling
my_iter = iter([1, 2, 3])
try:
    while True:
        print(next(my_iter))
except StopIteration:
    print("StopIteration: No more items in iterator")

#syntax error exception handling
try:
    eval('x === x')
except SyntaxError:
    print("SyntaxError: invalid syntax")

#indentation error exception handling
try:
    exec('def func():\n    print("Hello")')
except IndentationError:
    print("IndentationError: unexpected indent")

#tab error exception handling
try:
    exec('def func():\n\tprint("Hello")\n    print("World")')
except TabError:
    print("TabError: inconsistent use of tabs and spaces in indentation")

#runtime error exception handling
try:
    raise RuntimeError("This is a runtime error")
except RuntimeError as e:
    print(f"RuntimeError: {e}")

#not implemented error exception handling
try:
    raise NotImplementedError("This feature is not implemented yet")
except NotImplementedError as e:
    print(f"NotImplementedError: {e}")
