"""
Student: Bander Alqahtani
Program: bander_module2Assignment.py
Course: CSIT 512-01
Assignment: Assignment 2
Description: Computes the average of three input values.
Sources: The textbook and course notes
"""
course_name = input(print("Enter course name: "))
test1_score = int(input(print("Enter test1 score: ")))
test2_score = int(input(print("Enter test2 score: ")))
test3_score = int(input(print("Enter test3 score: ")))
avg = (test1_score + test2_score + test3_score)/3

string = """Scores Report For: {course}
Test #1: {test1}
Test #2: {test2}
Test #3: {test3}
Average score: {average:.2f}"""
print(string.format(course=course_name, test1=test1_score, 
        test2=test2_score, test3=test3_score,average=avg))