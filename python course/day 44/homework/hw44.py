# For Loop:

#1) Print all integers from 0 to 20 inclusive.

for i in range (0,21):
    print(i)

#2) Print the first 10 natural numbers.

for i in range (0,10):
    print(i)

#3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive.

for i in rage (0,100):
    if i % 2 == 0:
        print("the even is" + str(i))
    else:
        print("the even is" + str(i))

#4) Enter a number to the user and then using a for loop output the sum for all the numbers up to this number

for i in range(10):
    number = int(input("შემოიყვანეტ რიცხვი: "))

sum_of_number = 0
for i in range(1, number + 1):
    sum_of_number += i

print("რიცხვის ჯამი: " + str(sum_of_number))

#5) Write an algorithm that prints multiples of 5 (numbers divisible by 5) from 1 to 50

for i in range(1,51):
    if i % 5 == 0:
        print(i)

# While Loop:

#1) Print even numbers up to 20

num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1 

#2) calculate the sum of numbers from 1 to 10.

num = 1
total_sum = 0 

while num <= 10:
    total_sum += num
    num += 1

print("the sum of numbers from 1 to 10 is:" + srt(total_sum))

#3) Write a while loopthat ask the user to guess a number between 1 and 10 until they ger it right.The corect number is 7

correct_answer = 7 
question = int(input("enter number from 1 to 10:  "))
while question != correct_answer:
    print("try again")
    question = int(input("enter number from 1 to 10:  "))
else:
    print("you gess the number")


#1:03