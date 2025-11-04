#for loop
for i in range(1, 11):
    print(i)


#to print all element one by one from list
x = [10, 20, 30, 40, 50]
for i in x:
    print(i)

#sum of x
total = 0
for i in x:
    total += i
print("Sum of x:", total)

#find vowels in name
name = "Saba"
vowels = "aeiouAEIOU"
for char in name:
    if char in vowels:
        print(char)

#break statement
for i in range(1, 11):
    if i == 6:
        break
    print(i)

#continue statement
for i in range(1, 11):
    if i % 3 == 0:
        # continue
        break
    print(i)

#pass
if 3>2:
    pass
print("Hello")


print("---------------------------------------------------------")

#while loop
count = 1
while count <= 10:
    print(count)
    count += 1



print("---------------------------------------------------------")
#problem
#take sentence n check if it is palindrome or not n print accordingly
sentence = "madam"
reversed_sentence = ""
for char in sentence:
    reversed_sentence = char + reversed_sentence
if sentence == reversed_sentence:
    print("Palindrome")
else:
    print("Not Palindrome")

# other method for palindrome
if sentence == sentence[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#find and display the count of student who failed the exam
marks =[50, 65, 24, 75, 18, 72]
failed_count = 0
for mark in marks:
    if mark < 30:
        failed_count += 1
print("Number of students failed:", failed_count)

#print prime numbers between 1 to 50
for num in range(1, 51):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            print(num)