import streamlit as st

def display_menu():
    st.title("Contact Manager")
    st.write("1. View contacts")
    st.write("2. Add a new contact")
    st.write("3. Search for a contact")
    st.write("4. Delete a contact")
    st.write("5. Exit")

def view_contact(contacts):
    if not contacts:
        st.write("No contacts found.")
    else:
        st.write("Contacts:")
        for name, phone in contacts.items():
            st.write(f"Name: {name}, Phone: {phone}")

def add_contact(contacts):
    name = st.text_input("Enter a name to add:", key="add_name")
    phone = st.text_input("Enter a phone number to add:", key="add_phone")
    if name and phone:
        contacts[name] = phone
        st.write(f"Contact {name} added successfully.")
    else:
        st.write("Please enter both name and phone number.")

def search_contact(contacts):
    name = st.text_input("Enter a name to search:", key="search_name")
    if name in contacts:
        st.write(f"Contact {name} found.")
        st.write(f"Phone: {contacts[name]}")
    else:
        st.write(f"Contact {name} not found.")

def delete_contact(contacts):
    name = st.text_input("Enter a name to delete:", key="delete_name")
    if name in contacts:
        del contacts[name]
        st.write(f"Contact {name} deleted successfully.")
    else:
        st.write(f"Contact {name} not found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = st.text_input("Enter a number from (1-5):", key="menu_choice")
        if choice == '1':
            view_contact(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            st.write("Exiting the Contact Manager.")
            break
        else:
            st.write("Enter a number from 1-5.")

if __name__ == "__main__":
    main()
