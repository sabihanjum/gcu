x=[10,21,17,18,24,9,12]
y = []
for i in x:
    if i%2==0:
        y.append(i)
print("Even numbers are:", y)

#list comprehension
y = [i for i in x if i%2==0]
print("Even numbers are:", y)

#double of each number in x
y = [i*2 for i in x]
print("Double of each number:", y)

#string name="program" find how many vowels are there in the string using list comprehension
name = "program"
print(len([char for char in name if char in 'aeiouAEIOU']))
