"""
Student: Bander Alqahtani
Program: Bander_module5rpracticeprogram.py
Course: CSIT 512-01
Assignment: Module 4 practice Program
Description: printing nlines using functions.
Sources: The textbook and course notes
"""
def horizontal_line(length):
    for i in range(length):
        if i <length-1:
            print("*", end = "")
        else:
    	    print("*")

def vertical_line(shift, height):
    for i in range(height):
        for i in range(shift):
            print(" ", end="")
        print("*")

def two_vertical_lines(height, width):
    for i in range(height):
        print("*", end="")
        for j in range(width):
            print(" ", end = "")
        print("*")

def number_0(width):
    horizontal_line(width)
    two_vertical_lines(3,width-2)
    horizontal_line(width)
def number_1(width):
    vertical_line(width-1,width)

def number_2(width):
    horizontal_line(width)
    vertical_line(width-1,1)
    horizontal_line(width)
    vertical_line(0,1)
    horizontal_line(width)

def main():
    number1 = int(input("enter number 1: "))
    number2 = int(input("enter number 2: "))
    number3 = int(input("enter number 3: "))
    if number1 == 1:
        number_1(5)
    elif number1 == 0:
        number_0(5)
    elif number1 == 2:
        number_2(5)
    if number2 == 1:
        number_1(5)
    elif number2 == 0:
        number_0(5)
    elif number2 == 2:
        number_2(5)
    if number3 == 1:
        number_1(5)
    elif number3 == 0:
        number_0(5)
    elif number3 == 2:
        number_2(5)
main()