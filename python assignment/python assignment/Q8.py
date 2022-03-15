def print_average():
    numbers = []
    while True:
        number = int(input("Type a number: "))
        if number < 0:
            if len(numbers) == 0:
                print("Average of numbers is 0.")
                break
            else:
                avg = sum(numbers)/len(numbers)
                print("Avewrage of numbers is ",round(avg,2))
                break
        else:
            numbers.append(number)
print_average()