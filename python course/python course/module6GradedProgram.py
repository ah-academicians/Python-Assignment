"""
Student: Bander Alqahtani
Program: Bander_module6GradedProgram.py
Course: CSIT 512-01
Assignment: Module 6 graded Program
Description: reading data from a file and saving to other file after processing.
Sources: The textbook and course notes
"""
import math
typeError = 0
zeroDivisionError = 0
valueError = 0
try:
    file1 = open('module6data.txt', 'r')
except:
    print("file name is incorrect or not present.")
processedData = open("processedData.txt","w")
 
while True:
    # Get next line from file
    line = file1.readline()
    # if line is empty end of file is reached
    if not line:
        break
    try:
        number = int(line)
        processedData.write("square of {} is {}\n".format(number, number*number))
    except ValueError:
        if type(line) == str:
            typeError += 1
        else:
            valueError += 1
    try:
        reciprocal = 1/number
        processedData.write("reciprocal of {} is {}\n".format(number,reciprocal))
    except ZeroDivisionError:
        zeroDivisionError += 1
    try:
        sqrt = math.sqrt(number)
        processedData.write("square root of {} is {}\n".format(number,sqrt))
    except ValueError:
        valueError += 1
file1.close()

print("ValueError exception occured {} times.".format(valueError))
print("zeroDivisionError exception occured {} times.".format(zeroDivisionError))
print("TypeError exception occured {} times.".format(typeError))
    