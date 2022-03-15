"""
Student: Bander Alqahtani
Program: Bander_module4gradedprogram.py
Course: CSIT 512-01
Assignment: Module 4 Graded Program
Description: printing sequence of numbers using loops
Sources: The textbook and course notes
"""
while True:
    number=int(input("How many rows?:"))
    if number>=1 and number<=25:
        for z in range(number):
            i=9
            while i!=0:
                for x in range(i):
                    print(i, end ="")
                i=i-1
                if i==0:
                    print(end="\n")
    else:
        print("out of range - must be between 1 and 25")