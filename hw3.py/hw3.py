import os

# part 1.	Write a function that takes a string as input and does the following:
# a.	Returns True if the input string has more vowels than consonants
# b.	Returns False if the input string has more consonants than vowels
# c.	Returns None (this is the Python equivalent of null) if the input string has an equal number of consonants and vowels.
#       We’ll ignore type safety for now!

def vowelsvsconsonents(string1):
    numberOfVowels = 0
    numberOfConsonents = 0
    for i in string1:
        if i != " ":
            if i.lower() in ("a","e","i","o","u"):
                numberOfVowels += 1
            else:
                numberOfConsonents += 1
    if numberOfConsonents > numberOfVowels:
        return False
    elif numberOfVowels > numberOfConsonents:
        return True
    else:
        return None

# part 2. calculate volume of cylinder
def volumeOfCylinder(radius, height):
    intRadius = int(radius)
    intHeight = int(height)
    PI = 3.14
    volume = PI * intHeight * intRadius**2
    return volume

    
# part 3.  write a function that takes a list of strings as inputs,
#  and returns a single string created by joining all the input strings together, with a comma separating them.
def csvToStrings(listofStrings):
    stringFromCsv = ""
    for i in listofStrings:
        stringFromCsv = stringFromCsv + "," + i
    return stringFromCsv.lstrip(",")

#4.	Now write another function that takes a list of lists of strings, applies the operation from question 3 to each list,
#  and writes the result as a row of an output file. The function should return the path to the file where the strings were written.

def writingCsvToFile(listoflists):
    file = open("csv.txt","w")
    for i in listoflists:
        file.write(csvToStrings(i)+"\n")
    return os.path.abspath("csv.txt")

# part 5. a function that takes in a filename (which we will assume is a CSV), 
# and returns a list of lists of strings, where one row in the file corresponds to one list in the output list 
def filetocsv(filename):
    file = open(filename, "r")
    listoflists = []
    lines = file.readlines()
    for line in lines:
        listoflists.append(line.strip("\n").split(","))
    return listoflists



##part 6. write a function that takes two numbers and divides the first one by the second.
## You should catch the error if the second number is zero and print a warning instead of crashing.


def division(numerator, denominator):
    try:
        return int(numerator)/int(denominator)
    except ZeroDivisionError:
        return "Denominator can't be zero."


# part 7. Write a function that takes a list of integers and returns the same list, but without any duplicates.

def removeDuplicates(listOfIntegers):
    nonDuplicateList = []
    for i in listOfIntegers:
        if i not in nonDuplicateList:
            nonDuplicateList.append(i)
    return nonDuplicateList

# Part 8 In Python, you can write code that interacts with other parts of your operating system.
#  Write a function that creates a new folder called “hw3-folder” inside the current directory.

def createAFolder():
    try:
        os.makedirs("hw3-folder")
    except:
        print("Folder with same already exists.")

#test data to run functions
listoflists = [["yumming","is","coder"],["yumming","is","coder"],["yumming","is","coder"]]
print(writingCsvToFile(listoflists))
print(csvToStrings(["awais","is","computer","science","student"]))
print(volumeOfCylinder(2,1))
print(filetocsv("csv.txt"))
print(division(10,5))
print(division(10,0))
createAFolder()
print(vowelsvsconsonents("wais"))
print(vowelsvsconsonents("waaais"))
print(vowelsvsconsonents("waissssss"))



