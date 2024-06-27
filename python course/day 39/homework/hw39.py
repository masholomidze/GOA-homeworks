nubers = []

for i range(10)
    number = int(input("შემოიტანეთ რიცხვი: "))
    numbers.append(number)


greater_then_100 = []
less_than_100 = []


for number in numbers:
    if number > 100:
        greater_then_100.append(number)
    else:
        less_than_100.append(number)


print("100-ზე მეტი რიცხვები: ",greater_then_100)
print("100-ზე ნაკლები რიცხვები: ",less_than_100)