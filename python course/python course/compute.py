"""Student: Bander Alqahtani
Program: Bander_module5GradedProgram.py 
Course: CSIT 512-01
Assignment:Assignment 5, oct 12, 2021
Description:getting inputs to calculate total cost of paint
Sources:The textbook and course notes"""
from Bander_fetch import get_dimension, get_color
import math
def calc_cans(length, width, height):
    walls=2*(length*height)+2*(width*height)
    ceiling=length*width
    total_area_to_paint=walls+ceiling
    total_cans=math.ceil(total_area_to_paint/365)
    return total_cans
def calc_cost(cans, colorcode):
    if colorcode=="G":
        return float(cans*3.68)
    elif colorcode=="R":
        return float(cans*4.25)
    elif colorcode=="B":
        return float(cans*3.69)
    elif colorcode=="E":
        return float(cans*4.25)
    elif colorcode=="W":
        return float(cans*3.25)
    elif colorcode=="C":
        return float(cans*6)
    else:
        print("wrong Arguments")


def main():
    height=get_dimension("height")
    width=get_dimension("width")
    length=get_dimension("length")
    color=get_color()
    cans=calc_cans(length, width, height)
    print("total cost to paint will be $"+str(calc_cost(cans,color)))
    
    

main()