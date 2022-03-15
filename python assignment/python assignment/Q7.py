import random
def dice_sum(desiredSum):
    while True:
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        print(num1," and ",num2, " = ",num1+num2)
        if int(desiredSum) == num1+num2:
            break
        else:
            continue
desiredSum = input("enter desire sum: ")
dice_sum(desiredSum)