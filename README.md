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
