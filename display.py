"""Contains every function that prints something to the screen: displaying the menu, displaying a single contact's details, displaying all contacts, displaying the statistics page. 
If you ever want to change how something looks visually you only touch this file.
This is the view layer of the application, completely separate from the business logic in contacts.py and the data handling in file_handler.py. 
It should only be responsible for taking data and printing it to the screen in a nice format."""

def display_menu():
    print("Welcome to the CLI Contact Book!")
    print("1. View all contacts")
    print("2. Add a contact")
    print("3. Search for a contact")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. View Favourites")
    print("7. View by category")
    print("8. View statistics")
    print("9. Export to a .txt file")
    print("0. Quit/Exit from the Contact Book")
    while True:
        try:
            decision = int(input("Enter your choice (0-9): "))
            break
        except ValueError:
            print("Invalid choice. Please enter a number (0-9).")
    return decision

def display_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"City: {contact['city']}")
    print(f"Favourite: {'Yes' if contact['favourite'] else 'No'}")
    print(f"Category: {contact['category']}")
    print(f"Birthday: {contact['birthday']}")

def display_all_contacts(contacts):
    if not contacts:
        print("There are no contacts yet.")
    else:
        for contact in contacts:
            print (f"{contact['name']} - {contact['phone']} - {contact['email']} - {contact['city']} - {'Favourite' if contact['favourite'] else 'Not Favourite'} - {contact['category']} - {contact['birthday']}")

def display_statistics(contacts):
    total_contacts = int(len(contacts))
    total_favourites = 0
    for contact in contacts:
        if contact["favourite"]:
            total_contacts += 1
        total_contacts += 0
        break
    if not contacts:
        print("There are no statistics to print as there are no contacts.")
    else:
        print(f"There are {total_contacts} contacts in this Contact Book")
        print(f"There are {total_favourites} favourite contacts in this Contact Book")
        print(f"")#Print a breakdown of how many contacts are in each category
        print(f"")#Print the most recently added contact and their date added
        print(f"")#Print the oldest contact in the book by date added
        print(f"")#Print the total count of contacts added this month specifically.

