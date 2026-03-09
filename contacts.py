"""Contains the functions that actually operate on contact data: 
add a contact, edit a contact, delete a contact, search for a contact, toggle favourite. 
This is the core business logic of the application."""

#Function that Ill be able to use for add, edit, search and delete contact.
def contact_reusage(contact):
    return {
        "name" : str(contact.get("name","")).strip(),
        "phone" : str(contact.get("phone","")).strip(),
        "email" : str(contact.get("email","")).strip(),
        "city" : str(contact.get("city","")).strip(),
        "category" : str(contact.get("category","")).strip(),
        "favourite" : str(contact.get("favourite","")).strip(),
        #Find a way to implement date
    }

#Function that adds contact:
def add_contact(contact):
    return contact_reusage(contact)