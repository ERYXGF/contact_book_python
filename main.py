"""Contains only the main loop and menu logic. It imports functions from all the other files and orchestrates them. 
It as the manager who delegates everything but does no actual work itself. 
Handles input.
It should be short — ideally under 60 lines."""

#Imported the different functions from my files
from contacts import add_contact, search_contact, delete_contact, edit_contact
from validation import (
    validate_name,
    validate_phone,
    validate_email,
    validate_city,
    validate_category,
    validate_birthday,
)
from file_handler import save, load
from display import display_menu, display_contact, display_all_contacts, display_statistics


CATEGORIES = ("Family", "Friend", "Work", "School", "Other")

#Function that aks user for propmt until its valid:
def prompt_until_valid(prompt, validator, *args):
    while True:
        value = input(prompt).strip()
        if validator(value, *args):
            return value
        print("Invalid input. Please try again.")

#Function that determines the prompt's category:
def prompt_category():
    while True:
        print("Category choices:")
        print("1. Family")
        print("2. Friend")
        print("3. Work")
        print("4. School")
        print("5. Other")
        choice = input("Choose category (1-5): ").strip()
        if validate_category(choice):
            return CATEGORIES[int(choice) - 1]
        print("Invalid category. Please try again.")

#Function that asks user if the contact is a favourite or not:
def prompt_favourite():
    while True:
        fav = input("Favourite? (Y/N): ").strip().lower()
        if fav in ("y", "yes"):
            return True
        if fav in ("n", "no"):
            return False
        print("Invalid choice. Enter Y or N.")

#Function that creates a contact:
def build_contact(contacts):
    name = prompt_until_valid("Full name (first + last): ", validate_name, contacts)
    phone = prompt_until_valid("Phone number: ", validate_phone, contacts)
    email = prompt_until_valid("Email: ", validate_email, contacts)
    city = prompt_until_valid("City: ", validate_city)
    category = prompt_category()
    favourite = prompt_favourite()
    birthday = prompt_until_valid("Birthday (YYYY-MM-DD): ", validate_birthday)

    return {
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
        "category": category,
        "favourite": favourite,
        "birthday": birthday,
    }

#Function for the add contact flow:
def add_flow(contacts):
    contact = build_contact(contacts)
    contacts.append(add_contact(contact))
    save(contacts)
    print("Contact added successfully.")

#Function for the search contact flow:
def search_flow(contacts):
    query = input("Search for: ").strip()
    results = search_contact(contacts, query)
    if not results:
        print("No contacts found.")
        return
    for contact in results:
        display_contact(contact)

#Function for the edit contact flow:
def edit_flow(contacts):
    identifier = input("Enter full name of contact to edit: ").strip().lower()
    print("Fields: name, phone, email, city, category, favourite, birthday")
    field = input("Which field do you want to edit? ").strip().lower()

    if field not in ("name", "phone", "email", "city", "category", "favourite", "birthday"):
        print("Invalid field.")
        return

    if field == "name":
        value = prompt_until_valid("New name: ", validate_name, contacts)
    elif field == "phone":
        value = prompt_until_valid("New phone: ", validate_phone, contacts)
    elif field == "email":
        value = prompt_until_valid("New email: ", validate_email, contacts)
    elif field == "city":
        value = prompt_until_valid("New city: ", validate_city)
    elif field == "category":
        value = prompt_category()
    elif field == "favourite":
        value = prompt_favourite()
    else:
        value = prompt_until_valid("New birthday (YYYY-MM-DD): ", validate_birthday)

    updates = {field: value}
    if edit_contact(contacts, identifier, updates):
        save(contacts)

#Delete contact flow:
def delete_flow(contacts):
    name_find = input("Enter full name of contact to delete: ").strip()
    if delete_contact(contacts, name_find):
        save(contacts)

#Main func/logic that ties everything together:
def main():
    contacts = load()
    while True:
        choice = display_menu()
        if choice == 1:
            display_all_contacts(contacts)
        elif choice == 2:
            add_flow(contacts)
        elif choice == 3:
            search_flow(contacts)
        elif choice == 4:
            edit_flow(contacts)
        elif choice == 5:
            delete_flow(contacts)
        elif choice == 6:
            print("I have not implemented that feature yet.")
        elif choice == 7:
            print("I have not implemented that feature yet.")
        elif choice == 8:
            display_statistics(contacts)
        elif choice == 9:
            print("I have not implemented that feature yet.")
        elif choice == 0:
            print("Thank you for using my Contact Book! See you later!")
            break
        else:
            print("You have entered an invalid choice. Please select (0-9).")

#Executes/initializes the main func:
if __name__ == "__main__":
    main()
