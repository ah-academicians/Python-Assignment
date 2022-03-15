while True:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print("The sum of two numbers you entered is "+str(float(num1+num2)))
    repetition = input("Do you want to do that again? (y/n) : ")
    if repetition == "y":
        continue
    else:
        break