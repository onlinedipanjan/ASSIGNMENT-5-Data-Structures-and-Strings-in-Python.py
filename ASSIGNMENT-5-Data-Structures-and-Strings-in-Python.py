# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message

# Solution:
students_marks = {
        "James": 31,
        "Velma": 43,
        "Kib": 81,
        "Louis": 11,
        "Phyllis": 18,
        "Zenaida": 55,
        "Gillian": 38,
        "Constance": 16,
        "Giselle": 73,
        "Kirsten": 16,
}


student_name = input("Please enter the student's name: ")


if student_name in students_marks:
   print("Enter Student Name:", student_name) 
   print(f"{student_name}'s marks are: {students_marks[student_name]}")
else:
   print("Enter Student Name:", student_name) 
   print(student_name,"Student not found.")


# This nore for me:-  this is iferror formumal 

# -------------------------------------------------------------------------------------------------------------------------------


# Task 2: Demonstrate List Slicing 

# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

# Solution:

# input_number = input("Enter Number:- ") # this testing prupose only

# inpput_start = int(input("Enter Start Number:- ")) # this testing prupose only
# inpput_end = int(input("Enter Start Number:- ")) # this testing prupose only
# input_number = list(range(inpput_start,inpput_end)) # this testing prupose only


input_number = list(range(1,11))

# spielt = input_number.split(",")

extracted_elements = input_number[:5]

reversed_elemtns = extracted_elements[::-1]

print("Orginal List",input_number)

print("Extracted First Five Elements: ", extracted_elements)
print("Reversed Extracted Elements:", reversed_elemtns)















