name = input("what is your name?: ")
age = input("how old are you?: ")
surname = input("what is your surname?: ")
live = input("where do you live?: ")

new_age = int(age) + 20
print("hi " + name + " " + surname + ", " + "you live in " + live + ", " + "you are " + age + " years old. " + "after 20 year you will be " + str(new_age) + "." )