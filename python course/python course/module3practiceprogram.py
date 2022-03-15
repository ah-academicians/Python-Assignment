"""
Student: Bander Alqahtani
Program: Bander_module3practiceprogram.py
Course: CSIT 512-01
Assignment: practice program
Description: temprature convertor.
Sources: The textbook and course notes.
"""
print("enter Temprature: ")
temp = int(input())
print("Enter a sclae, F for Fahrenheit, C for Celsius: ")
scale = input()
if scale == "F":
    celsius = (5/9)*(temp-32)
    print(temp,"F = ",celsius,"C")
elif scale == "C":
    Fahrenheit = (9/5)*temp+32
    print(temp,"C = ",Fahrenheit,"F")
