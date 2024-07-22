def display_menu():
    print("Note taking application")
    print("1. View notes")
    print("2. Add notes")
    print("3. Delete notes")
    print("4. Search notes")
    print("5. Exit")

def view_notes(notes):
    if not notes:
        print("No notes found")
    else:
        print("Listing all notes:")
        for title, content in notes.items():
            print(f"Title: {title}")
            print(f"Content: {content}")
            print("--------------")

def add_notes(notes):
    title = input("Enter a title for the note: ")
    content = input("Enter content for the note: ")
    notes[title] = content
    print(f"Note '{title}' added successfully")

def del_notes(notes):
    title = input("Enter the title of the note you want to delete: ")
    if title in notes:
        del notes[title]
        print(f"Note '{title}' deleted successfully")
    else:
        print(f"Note '{title}' not found")

def search_notes(notes):
    title = input("Enter the title of the note you want to search for: ")
    if title in notes:
        print(f"Note found:")
        print(f"Title: {title}")
        print(f"Content: {notes[title]}")
    else:
        print(f"Note '{title}' not found")

def main():
    notes = {}
    while True:
        display_menu()
        
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
                view_notes(notes)
        elif choice == 2:
                add_notes(notes)
        elif choice == 3:
                del_notes(notes)
        elif choice == 4:
                search_notes(notes)
        elif choice == 5:
                print("Exiting the application")
                break
        else:
                print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
