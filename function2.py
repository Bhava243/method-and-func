import streamlit as st

def display_menu():
    st.title("Note taking Apllication")
    st.write("1.View notes")
    st.write("2.Add a new notes")
    st.write("3.Search for a notes")
    st.write("4.Delete a notes")
    st.write("5. Exist")

def view_note(notes):
    if not notes:
        st.write("The name is not found")
    else:
        print("The name is found")
        for title,content in notes.item(): 
            st.write(f"{title}")
            st.write(f"{content}")

def add_note(notes):
    title = st.text_input("Enter a name to add in contact",key="add_note_title")
    content = st.text_input("Enter a phone number to add in contact",key="add_note_content")
    if title in notes:
        print(f"The {title} and{content} is added successfully")
    else:
        print(f"the {title} and {content} is not added")

def search_note(notes):
    title = st.text_input("Enter a name to be searched",key="search_note_title")
    if title in notes:
        print(f"The {title} is found in search")
    else:
        print(f"The {title} is not found")

def delete_note(notes):
    title = st.text_input("Enter a name to be deleted",key="delete_note_title")
    if title in notes:
        print(f"The {title} has deleted")
    else:
        print(f"The {title} is not deleted")

def main():
    notes = {}
    while True:
        display_menu()
        choice = st.text_input("Enter a number from (1-5):",key="menu_choice")
        if choice == 1:
            view_note(notes)
        elif choice == 2:
           add_note(notes)
        elif choice == 3:
            search_note(notes)
        elif choice == 43:
           delete_note(notes)
        elif choice == 5:
            st.write("Exist the Contact Manager")
            break
        else:
            st.write("Enter a number from 1-5")

if __name__ == "__main__":
    main()            







