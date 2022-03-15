"""
Student: Bander Alqahtani
Program: Bander_module10program.py
Course: CSIT 512
Assignment: Module 10 graded Program
Description: classes and methods
Sources: The textbook and course notes
"""
import random
class BankAccount:
    def __init__(self):
        self.__balance = 0
        #generating random password
        self.__pin = random.randint(1000,9999)  
        
    def get_pin(self):
        return self.__pin
    def check_pin(self,pin):
        return self.__pin == pin

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        return self.__balance
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            return self.__balance
        else:
            return False
    def get_balance(self):
        return self.__balance


def main():
    while True:
        menu_input = input("choose an option: (N) Create Account,(D) Deposit, (W) Withdraw, (C) Check Balance,(S) stop: ").lower()
        if menu_input == "n":
            account = BankAccount()
            pin = account.get_pin()
            print("Your pin is " + str(pin))
        elif menu_input == "d":
            pin = int(input("Enter pin: "))
            if account.check_pin(pin):
                amount = int(input("Enter amount: "))
                newbalance = account.deposit(amount)
                print("Amount deposited successfully. your new account balance is "+ str(newbalance))
            else:
                print("Bad pin. Transaction failed.")
        elif menu_input == "w":
            pin = int(input("Enter Passowrd: "))
            actual_pin = account.get_pin()
            if pin == actual_pin:
                amount = int(input("Enter amount: "))
                returned = account.withdraw(amount)
                if returned != False:
                    print("Amount withdrawn successfully. your new account balance is "+ str(account.get_balance() ))
                else: 
                    print("You entered invalid amount.")
            else:
                print("Invalid Password.")
        elif menu_input == "c":
            pin = int(input("Enter pin: "))
            if account.check_pin(pin):
                print("Your account balance is "+ str(account.get_balance()))
            else:
                print("Incorrect pin.")
        elif menu_input == "s":
            print("Thank you for banking with us. come back again.")
            break
        else:
            print("invalid option. please choose a valid option.")
            
main()