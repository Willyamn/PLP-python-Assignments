# PLP-python-Assignments

# Week4 Assignment.
#File name: week4Assignment.py

File Operations Program (Python)

This Python program demonstrates file handling and error handling concepts. It allows users to:

Read a file, apply modifications, and save to a new file.

Safely read a file by handling errors (missing file, permission issues, etc.).

Features

Read & Write Challenge

User chooses an input .txt file.

Multiple modification options before saving:

Convert to UPPERCASE

Convert to lowercase

Add line numbers

Reverse text

Copy content as is

Saves modified content to a new file chosen by the user.

Error Handling Lab

User enters a filename.

Handles errors gracefully if:

File does not exist 

Permission is denied 

Other unexpected issues 

Menu-driven interface to select between operations.

Example Run
Main Menu
--- File Operations Menu ---
1. File Read & Write Challenge 
2. Error Handling Lab 
3. Exit
Choose an option (1-3):

Case 1: File Read & Write
Enter the name of the file to read: notes.txt

--- Modification Options ---
1. Convert to UPPERCASE
2. Convert to lowercase
3. Add line numbers
4. Reverse text
5. No modification (copy as is)
Choose a modification (1-5): 3

Enter the name of the new file to save modified content: notes_numbered.txt
File 'notes.txt' has been modified and saved to 'notes_numbered.txt'

Case 2: Safe File Read
Enter the filename to read: missing.txt
The file 'missing.txt' was not found.

Concepts Covered

File handling (open(), read(), write())

Error handling (try-except)

Loops & menus

String manipulation (uppercase, lowercase, reverse, line numbering)

# Week 5 Assignment
# file name: Week5Assignment.py

Activity 1: Smartphone Class
- Create and manage smartphones with attributes like brand, model, storage, and battery.  
- Encapsulation is used with protected attributes.  
- Inheritance shown with a `GamingPhone` subclass that adds GPU features.  

---

Activity 2: Polymorphism Challenge
- Implemented a `Vehicle` base class with a `move()` method.  
- Subclasses `Car`, `Plane`, `Boat`, and `Bicycle` override `move()` differently.  
- Demonstrates **polymorphism**: the same method name behaves differently depending on the object.

  Choose an option from the menu:
  - Smartphone Demo
  - Polymorphism Demo
  - Exit
    
Concepts Covered

Classes & Objects – Defining custom data types.

Constructors (__init__) – Initializing objects with unique values.

Encapsulation – Using protected attributes and getters/setters.

Inheritance – Extending functionality of parent classes.

Polymorphism – Same method name, different behaviors.

