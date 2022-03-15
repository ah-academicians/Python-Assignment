import random
filename = input("enter name of file to which to which results should be written: ")
Numbers = int(input("Enter number of random numbersd to be written in file: "))

file = open(filename,"w")
for i in range(Numbers):
    file.write(str(random.randint(1,100))+"\n")