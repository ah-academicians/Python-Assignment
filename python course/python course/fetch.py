"""Student: Rasha Alqahtani
Program: Rasha_fetch.py 
Course: CSIT 512-01
Assignment:Assignment 5, oct 12, 2021
Description:getting inputs to calculate total cost of paint
Sources:The textbook and course notes"""
def get_dimension(dimension):
    if dimension=="length" or dimension=="width" or dimension=="Length" or dimension=="Widthth": ##user may enter with capital letters
        while(True):
            dim=int(input(print("enter "+dimension+":")))
            if dim>4.5 and dim<30:
                return dim
            else:
                print("Incorrect dimensions for "+ dimension+" it should be between 4.5 and 30")
    elif dimension=="height":
        while(True):
            dim=int(input(print("enter "+dimension+":")))
            if dim>6.5 and dim<16:
                return dim
            else:
                print("Incorrect dimensions for "+ dimension+" it should be between 6.5 and 16")
def get_color():
    while(True):
        print("Choose color from following by entering Abbreviations mentioned in brackets infromnt of color names.\n Greeen(G)\n Blue(B)\n Red(R)\n Eggshell(E)\n White(W)\n Custom(C)")
        clr=str(input())
        if clr=='G' or clr=='B' or clr=='R' or clr=='E' or clr=='W' or clr=='C':
            return clr
        else:
            print("incorrect Input, Please Enter in Capital and correct Letter i.e in () brackets infront of color name")
    