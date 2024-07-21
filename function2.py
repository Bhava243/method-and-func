def display_menu():
    print("the Contact Manager")
    print("1.View notes")
    print("2.Add a new contact")
    print("3.Search for a contact")
    print("4.Delete a contact")
    print("5. Exist")

def view_contact(contacts):
    if not contacts:
        print("The name is not found")
    else:
        print("The name is found")
        for name,phone in contacts.item(): 
            print(f"{name}")
            print(f"{phone}")

def add_contact(contacts):
    name = input("Enter a name to add in contact")
    phone = input("Enter a phone number to add in contact")
    if name in contacts:
        print(f"The {name} and{phone} is added successfully")
    else:
        print(f"the {name} and {phone} is not added")

def search_contact(contacts):
    name = input("Enter a name to be searched")
    if name in contacts:
        print(f"The {name} is found in search")
    else:
        print(f"The {name} is not found")

def delete_contact(contacts):
    name  = input("Enter a name to be deleted")
    if name in contacts:
        print(f"The {name} has deleted")
    else:
        print(f"The {name} is not deleted")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter a number from (1-5):")
        if choice == 1:
            view_contact(contacts)
        elif choice == 2:
            add_contact(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 43:
            delete_contact(contacts)
        elif choice == 5:
            print("Exist the Contact Manager")
            break
        else:
            print("Enter a number from 1-5")

if __name__ == "__main__":
    main()            







