"""
Student: Bander Alqahtani
Program: Bander_module8assignment.py
Course: CSIT 512-01
Assignment: Module 8 graded Program
Description: list methods.
Sources: The textbook and course notes
"""
#get parts function
def get_parts(string):
    line = string.strip()
    splittedLine = line.split(",")
    firstName = splittedLine[0].strip()
    sencondName = splittedLine[1].strip()
    number = splittedLine[2].strip()
    return firstName,sencondName,number
#username maker
def make_user(firstName,lastName,number):
    userName = firstName[0:2].lower()+lastName[0:2].lower()+number[2:]
    return userName
def main():
    #opening file clients.txt
    file = open("clients.txt","r")
    lines = file.readlines()
    print("""client       username
    =====================""")

    for line in lines:
        firstname,lastName,number = get_parts(line)
        userName = make_user(firstname,lastName,number)
        print(firstname+" "+lastName+"        "+userName)
main()
