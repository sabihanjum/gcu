#if condition
if 5 > 3:
    print("hello")
    print("bye")

# if-else condition
x = 10
if x > 0:
    print("Positive")
else:
    print("Negative")


# if-elif-else condition
dayNo = 3
if dayNo == 1:
    print("Monday")
elif dayNo == 2:
    print("Tuesday")
elif dayNo == 3:
    print("Wednesday")
elif dayNo == 4:
    print("Thursday")
elif dayNo == 5:
    print("Friday")
elif dayNo == 6:
    print("Saturday")
elif dayNo == 7:
    print("Sunday")
else:
    print("Invalid day")


# nested if condition
nat = "Indian"
age = 20
if nat=="Indian":
    if age>=18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote, age is less than 18")
else:
    print("Not eligible to vote, not an Indian citizen")


#take random num, check if it is multiple of 5 print "fizz", if multiple of 3 print "buzz", if multiple of both print "fizzbuzz", else print the number itself by using nested if

num = 25
if num % 5 == 0:
    if num % 3 == 0:
        print("fizzbuzz")
    else:
        print("fizz")
elif num % 3 == 0:
    print("buzz")
else:
    print(num)
