"""
Student: Bander Alqahtani
Program: Bander_module3program.py
Course: CSIT 512-01
Assignment: Module 3 Graded Program
Description: Ticketing System using If Else Statements
Sources: The textbook and course notes
"""
basePrice = 40
seniorCitizenDiscount = 50
SeniorCitizenAge = 65
FrederickCitizensBasicPrice = 35
TicketPriceForUnderAgeChildren = 0
UnderAge = 6
age = int(input("Enter age: "))
if age<110 and age>0:
    country = input("Enter Country name: ")
    
    if country == "frederick" or country == "Frederick" or country == "FREDERICK":
        if age<UnderAge:
            print("Ticket price is :$",TicketPriceForUnderAgeChildren)
        elif age>65:
            print("Ticket price is :$",format(FrederickCitizensBasicPrice*(seniorCitizenDiscount/100),".1f"))
        else:
            print("Ticket price is :$",FrederickCitizensBasicPrice)
    else:
        if age<UnderAge:
            print("Ticket price is :$",TicketPriceForUnderAgeChildren)
        elif age>65:
            print("Ticket price is :$",format(basePrice*(seniorCitizenDiscount/100),".1f"))
        else:
            print("Ticket price is :$",basePrice)
else:
    print("invalid Age")