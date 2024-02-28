# -*- coding: utf-8 -*-
#APPROVED
"""
Created on Sun Apr 11 10:21:10 2021

@author: jacob
"""

'''Define the functions for the following:
    a) To input list elements
    b) To display list elements
    c) To delete an element from the list
    
Write a menu diven program'''

def list_input(element):
    list.append(element)
    
def display():
    print(list)
    
def delete_element(element):
    if element not in list:
        print('Element does not exist.')
    else:
        list.remove(element)
        print('Element removed.')
    
list = []

while True:
    print('Please enter the appropriate choice:\n\ta) To input list elements\n\tb) To display list elements\n\tc) To delete an element from the list\n\td) To stop the program')
    choice = input()
    
    if choice =='a':
        element = input('Enter element: ')
        list_input(element)
    elif choice == 'b':
        display()
    elif choice == 'c':
        element = input('Enter element to be deleted: ')
        delete_element(element)
    elif choice == 'd':
        break
print('Thank you for using this program')