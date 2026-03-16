"""Contains every function that prints something to the screen: displaying the menu, displaying a single contact's details, displaying all contacts, displaying the statistics page. 
If you ever want to change how something looks visually you only touch this file.
This is the view layer of the application, completely separate from the business logic in contacts.py and the data handling in file_handler.py. 
It should only be responsible for taking data and printing it to the screen in a nice format."""
#Function that displays main/initial menu:
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
            if 0 <= decision <=9:
                return decision
            print("Please enter a number between 0 and 9: ")
        except ValueError:
            print("Invalid choice. Please enter a number (0-9).")

#Function that displays a particular contact's information:
def display_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"City: {contact['city']}")
    print(f"Favourite: {'Yes' if contact['favourite'] else 'No'}")
    print(f"Category: {contact['category']}")
    print(f"Birthday: {contact['birthday']}")

#Function that displays all contacts:
def display_all_contacts(contacts):
    if not contacts:
        print("There are no contacts yet.")
    else:
        for contact in contacts:
            print (f"{contact['name']} - {contact['phone']} - {contact['email']} - {contact['city']} - {'Favourite' if contact['favourite'] else 'Not Favourite'} - {contact['category']} - {contact['birthday']}")

#Imports datetime so that I can determine when contacts have been created:
from datetime import datetime

#Function that displays statistics: 
def display_statistics(contacts):
    
    #Check if there are no contacts:
    if not contacts:
        print("There are no statistics to print as there are no contacts.")
        return False
    
    #Total amount of contacts:
    total_contacts = len(contacts)
    
    #Total amount of favourite contacts:
    favourites = sum(1 for contact in contacts if contact["favourite"])
    
    #Category counting:
    categories = {}
    for contact in contacts:
        cat = contact["category"]
        categories[cat] = categories.get(cat, 0) + 1
    
    #Most recent contact:
    recentest = max(contacts, key=lambda contact: contact["date_added"])
    
    #Oldest contact:
    oldest = min(contacts, key=lambda contact: contact["date_added"])
    
    #Contacts added this month:
    now = datetime.now()
    monthly_contacts = 0

    for contact in contacts:
        creation = datetime.strptime(contact["date_added"], "%Y-%m-%d")
        if creation.year == now.year and creation.month == now.month:
            monthly_contacts += 1

    #What the user sees:
    print("\n --------------- Contact Statistics ---------------")

    print(f"There are {total_contacts} contacts in this Contact Book.")#Number of total contacts

    print(f"There are {favourites} favourite contacts in this Contact Book.")

    for category, count in categories.items(): #Assigns number of contacts in given category to that category.
        print(f"{category}: {count}") #Contacts per category

    print(f"The most recently added contact was {recentest['name']}.") #Most recent contact

    print(f"The oldest added contact in the book is {oldest['name']}.") #Oldest contact

    print(f"This month, {monthly_contacts} contacts have been added." ) #Monthly contacts

    print("------------------------------------------------------")

