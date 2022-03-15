"""
Student: Bander Alqahtani
Program: Bander_module4rpracticeprogram.py
Course: CSIT 512-01
Assignment: Module 4 practice Program
Description: printing numbers and statements using conditions and loops.
Sources: The textbook and course notes
"""
number = 1
while(number<=100):
    if number%15 == 0:
        print(" In the future, everyone will be world famous for 15 minutes.")
    elif number % 5 == 0:
        print("Where do you see yourself in five years?")
    elif number % 3 == 0:
        print("Better three hours too soon than a minute too late.")
    else:
        print(number)
    number  = number + 1