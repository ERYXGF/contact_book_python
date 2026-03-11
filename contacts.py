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
        "favourite" : str(contact.get("favourite","")).strip()
        #Find a way to implement date
    }

#Function that adds contact:
def add_contact(contact):
    return contact_reusage(contact)

#Function that edits contacts:
def search_contact(contacts,query):
    query =  str(query).strip().lower()
    results  = []
    #If the user inputs nothing but an empty list:
    if not query:
        return []
    #Conjures and returns/gives the contact the person searched for:
    for contact in contacts:
        if (
            query in str(contact.get("name","")).lower()
            or query in str(contact.get("phone","")).lower()
            or query in str(contact.get("email","")).lower()
            or query in str(contact.get("city","")).lower()
            or query in str(contact.get("category","")).lower()
            or query in str(contact.get("favourite","")).lower()
            or query in str(contact.get("favourite","")).lower()
        ):
            results.append(contact)
    #Line that ties everything together and returns the result:
    return results 

#Function that deletes a contact:
def delete_contact(contacts,name_find):
    #Variable defining what the user wants to delete (target):
    target = str(name_find).strip().lower()
    #Determines if target is an already existing contact:
    if contact.get("target","") not in contacts:
        print("Contact cannot be deleted as it doesn't exist. ")
        return False
    #Loop through the different contacts:
    for index, contact in enumerate(contacts):
        if str(contact.get("name","")).strip().lower() == target:
            contacts.pop(index)
        #Confirms the contact has been deleted:
        print(f"The contact {target} has been succesfully deleted.")
    return True

        
    

    