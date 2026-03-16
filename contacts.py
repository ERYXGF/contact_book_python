"""Contains the functions that actually operate on contact data: 
add a contact, edit a contact, delete a contact, search for a contact, toggle favourite. 
This is the core business logic of the application."""

#Imports the datetime library to be used in the add_contact function:
from datetime import date
#Function that Ill be able to use for add, edit, search and delete contact.
def contact_reusage(contact):
    return {
        "name" : str(contact.get("name","")).strip(),
        "phone" : str(contact.get("phone","")).strip(),
        "email" : str(contact.get("email","")).strip(),
        "city" : str(contact.get("city","")).strip(),
        "category" : str(contact.get("category","")).strip(),
        "favourite": str(contact.get("favourite", "")).strip().lower() in ("y", "yes", "true", "1"),
        "birthday" : str(contact.get("birthday","")).strip(),
        "date_added": contact.get("date_added") or date.today().isoformat() #Implements date
    }

#Function that adds contact:
def add_contact(contact):
    return contact_reusage(contact)

#Function that seraches a particular contact:
def search_contact(contacts,query):
    query =  str(query).strip().lower()
    results  = []
    #If the user inputs nothing but an empty list:
    if not query:
        return []
    #Conjures and returns/gives the contact the person searched for:
    for contact in contacts:
        if (
            query in str(contact.get("name","")).strip().lower()
            or query in str(contact.get("phone","")).strip().lower()
            or query in str(contact.get("email","")).strip().lower()
            or query in str(contact.get("city","")).strip().lower()
            or query in str(contact.get("category","")).strip().lower()
            or query in str(contact.get("favourite","")).strip().lower()
            or query in str(contact.get("birthday","")).strip().lower()
        ):
            results.append(contact)
    #Line that ties everything together and returns the result:
    return results 

#Function that deletes a contact:
def delete_contact(contacts,name_find):
    #Variable defining what the user wants to delete (target):
    target = str(name_find).strip().lower()
    #Loop through the different contacts:
    for index, contact in enumerate(contacts):
        #Determines if target is an already existing contact:
        if str(contact.get("name","")).strip().lower() == target:
            contacts.pop(index)
            #Confirms the contact has been deleted:
            print(f"The contact {target} has been succesfully deleted.")
            return True
    #Returns False and prints message if there is no cntact to delete:
    print("Contact cannot be deleted as it doesn't exist. ")
    return False

#Function that edits a contact:
def edit_contact(contacts, identifier, updates):
    identifier = identifier.strip().lower()
    #Searches every individual contact in contacts:
    for contact in contacts:
        #If the contacts key called name is equal to the identifier:
        if str(contact.get("name", "")).strip().lower() == identifier:
            #For the key and value of that key in the contact:
            for key, value in updates.items():
                if key not in contact:
                    return False
                if key == "date_added":
                    return False
                #Updates the contact's key:
                contact[key] = (
                    str(value).strip().lower() in ("y","Y","yes","true","1")
                    if key == "favourite"
                    else str(value).strip()
                )
            print("The contact has been succesfully edited.")
            return True
    #If one of the conditions isn't met:
    print("The contact wasn't found.")
    return False




        
    

    