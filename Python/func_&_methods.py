#function and methods in python
#Function: block of code which is used to perform a specific task, it can take inputs and return output
def function(num1, num2):
    num3 = num1 + num2
    return num3
result = function(5, 10)
print("Sum is:", result)

#create a function in python which will take 3 patamters as n1, n2 and operator, display result based on operator
#ex m1(10, 20, '+') => 30, create a calculator function
def calculator(n1, n2, operator):
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '*':
        return n1 * n2
    elif operator == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
    
print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))

print("---------------------------------------------------------")

#Class --- class can be created by using variable or methods
#class by using variables
class Student:
    name = "Saba"
    age = 21

s = Student()
print("Name:", s.name)
print("Age:", s.age)

#Methods

class Student1:
    name = "Saba"
    age = 21

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student1()
s1.display()