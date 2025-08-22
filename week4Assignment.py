# File Read & Write + Error Handling Lab with Modification Options

def modify_content(content):
    """Provides options for modifying file content"""
    print("\n--- Modification Options ---")
    print("1. Convert to UPPERCASE")
    print("2. Convert to lowercase")
    print("3. Add line numbers")
    print("4. Reverse text")
    print("5. No modification (copy as is)")

    choice = input("Choose a modification (1-5): ")

    if choice == "1":
        return content.upper()
    elif choice == "2":
        return content.lower()
    elif choice == "3":
        lines = content.splitlines()
        numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        return "\n".join(numbered_lines)
    elif choice == "4":
        return content[::-1]
    elif choice == "5":
        return content
    else:
        print("Invalid choice, no modification applied.")
        return content


def file_read_write():
    """Reads a user-chosen file, modifies content, and writes to a new file"""
    source_file = input("Enter the name of the file to read: ")
    try:
        with open(source_file, "r") as infile:
            content = infile.read()

        # Let user choose how to modify the content
        modified_content = modify_content(content)

        # Ask user for output file name
        output_file = input("Enter the name of the new file to save modified content: ")
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"File '{source_file}' has been modified and saved to '{output_file}'")

    except FileNotFoundError:
        print(f"The file '{source_file}' was not found.")
    except PermissionError:
        print(f"You don’t have permission to read '{source_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def safe_file_read():
    """Asks user for a filename and reads it with error handling"""
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            print("\nFile content:\n")
            print(file.read())

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except PermissionError:
        print(f"You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main menu
def main():
    while True:
        print("\n--- File Operations Menu ---")
        print("1. File Read & Write Challenge")
        print("2. Error Handling Lab")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            file_read_write()
        elif choice == "2":
            safe_file_read()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()
