'''
-----------------
Name: problem2.py
Purpose: Calculates the number of chickens shared between students and Mr. Fabroa

Author: Rishi K

Created: date 07/12/2020
----------------
'''
#create an input for the user to type the amount of students and chicken there are
students = int(input("How many students are in the class?: "))
chicken = int(input("How many pieces of chicken are there?: "))
#print the amount of chicken that the children will get as well as Mr. Fabroa
print("Each student will get",chicken // students, "pieces of chicken")
print("Mr. Fabroa gets",chicken % students,"pieces of chicken")