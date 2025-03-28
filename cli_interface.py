# Ensure that these functions are defined or imported correctly
from directory_manager import create_directory, list_files, move_file, delete_file
from file_analytics import FileSearch
from auth import register_user, authenticate_user

def show_menu():
    print("\nWelcome to the Directory Management System")
    print("1. Create Directory")
    print("2. List Files")
    print("3. Move File")
    print("4. Delete File")
    print("5. Search Files")
    print("6. Register User")
    print("7. Login User")
    print("8. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            path = input("Enter directory path to create: ")
            create_directory(path)
        elif choice == '2':
            directory = input("Enter directory path to list files: ")
            print(list_files(directory))
        elif choice == '3':
            src = input("Enter source file path: ")
            dest = input("Enter destination directory: ")
            move_file(src, dest)
        elif choice == '4':
            file_path = input("Enter file path to delete: ")
            delete_file(file_path)
        elif choice == '5':
            query = input("Enter search query: ")
            # Assuming FileSearch is a class that needs file paths and contents
            file_search = FileSearch([], [])  # Make sure this is properly initialized with file contents
            print(file_search.search(query))
        elif choice == '6':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == '7':
            username = input("Enter username: ")
            password = input("Enter password: ")
            authenticate_user(username, password)
        elif choice == '8':
            print("Exiting system.")
            break  # Exits the loop and ends the program
        else:
            print("Invalid choice. Please try again.")  # Properly handle invalid input

if __name__ == "__main__":
    main()
