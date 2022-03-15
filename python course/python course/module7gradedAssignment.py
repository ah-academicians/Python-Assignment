"""
Student: Bander Alqahtani
Program: Bander_module67gradedAssignment.py
Course: CSIT 512-01
Assignment: Module 6 graded Program
Description: list methods.
Sources: The textbook and course notes
"""
import random

#creating a list
myList = []
listLength = random.randint(10,20)
for i in range(listLength):
    myList.append(random.randint(0,19))
print("list is ", myList) 

copiedList = myList.copy()
print("copy is",copiedList)
copiedList.sort()
copiedList.reverse()
print("descending order ",copiedList)


"""Before continuing with the next two parts, add a function user_input(lo, hi) to your
program. It should ask the user for an integer between lo and hi and return the value."""
def user_input(lo,hi):
    while True:
        number = int(input("Enter a number between "+str(lo)+" and "+str(hi)+": "))
        if number > lo and number < hi:
            break
        else:
            print("you entered an invalid number, number should be between "+str(lo)+" and "+str(hi))
    return number



"""Write a function named how_many(a_list, a_num) that that expects a list of numbers
and a number as arguments. It returns how many times the number is found in the list.
If the number is not in the list, return 0."""
def how_many(a_list, a_num):
    try:
        return a_list.count(a_num)
    except:
        return 0



"""Ask the user for an integer between 0 and 19. If the number is in the list, 
report how many times it occurs."""
number = user_input(0,19)
print(str(number)+" occurs "+ str(how_many(myList,number)) +" times.")

"""Write a function named find_bigger(a_list, a_num) that expects as arguments a list of
numbers and a number. It should return a new list consisting of all the numbers in the list
that are greater than the number. """
def find_bigger(a_list, a_num):
    biggerList = []
    for i in a_list:
        if a_num < i:
            biggerList.append(i)
    return biggerList

"""Ask the user for an integer between 0 and 19 and then report how many of the items in the
list are greater than that number."""
number = user_input(0,19)
print("larger items are: ",find_bigger(myList, number))
