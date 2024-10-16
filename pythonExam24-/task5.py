positive_numbers = []
zero_numbers = []
negative_numbers = []


while True:
    number = input("Enter an integer (blank to quit): ")
    if number == "":
        break
    number = int(number)
    if number > 0:
        positive_numbers.append(number)
    elif number == 0:
        zero_numbers.append(number)
    else:
        negative_numbers.append(number)

print("The numbers were:")
print(*positive_numbers, *zero_numbers, *negative_numbers)
