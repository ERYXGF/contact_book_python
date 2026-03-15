"""Contains every validation function: validate name, validate phone, validate email, validate city. 
These are completely separate from contacts.py because validation is a distinct responsibility. 
If you ever need to change the email validation rule you know exactly which file to go to without touching anything else."""

"""Validation Rules:
1) Name — cannot be empty, cannot be only spaces, must contain at least two words (first and last name), must contain only letters and spaces (no numbers or symbols), cannot already exist in the contact book unless the user explicitly confirms overwrite.
2) Phone number — must contain only digits, spaces, hyphens and the + symbol, must be between 7 and 15 digits long when all non-digit characters are stripped out, must not be identical to a phone number already saved to another contact.
3) Email — must contain exactly one @ symbol, must have at least one character before the @, must have a dot in the domain section after the @, must not be identical to an email already saved to another contact, must not have any spaces in it.
4) City — cannot be empty, must contain only letters spaces and hyphens (to allow names like Saint-Étienne).
5) Category — must be one of the five predefined options (family, friend, work, school, other), selected by number from a displayed list rather than typed freely. Never accept free text for category.
6) Birthday - Must be in the ISO format
"""

#Function that validates name:
def validate_name(name : str,contacts):
    #Normalizes name:
    normal = name.strip()
    #Checks if name is normalized
    if not normal: 
        return False
    #Checks if name has more than 2 words in it:
    elif  len(normal.split()) < 2:
        return False
    #Checks if name contains any unauthorized characters in it:
    elif not all(ch.isalpha() or ch.isspace() for ch in normal):
        return False
    #Checks if name is already an existing contact:
    new = normal.lower()
    for contact in contacts:
        existing = str(contact.get("name","")).strip().lower()
        if existing == new:
            return False
    #Returns True if all needed conditionss are met:
    return True 

#Function that validates phone number:
def validate_phone(phone : str,contacts):
    #Normalizes phone:
    normal = phone.strip()
    #Takes off non-digits from phone:
    perfect = "".join(ch for ch in normal if ch.isdigit())
    #Checks if any character is not a digit space, hyphen or plus:
    if not all(ch.isdigit() or ch.isspace() or ch in "+-" for ch in normal):
        return False
    #Checks if digits <7 or >15 after removing non-digits:
    if len(perfect) < 7 or len(perfect) > 15:
        return False
    #Checks if the digits match an already existing phone number:
    for contact in contacts:
        existing = str(contact.get("phone","")).strip()
        existing_digits = "".join(ch for ch in existing if ch.isdigit())
        if existing_digits == perfect:
            return False
    #Returns True if all needed conditions are met:
    return True

#Function that validates email:
def validate_email(email : str,contacts):
    #Normalizes email:
    email = email.strip().lower()
    #If there's a space in the email:
    if " " in email:
        return False
    #If email is empty:
    if not email:
        return False
    #If there's no at symbol in the email:
    if email.count("@") != 1:
        return False
    #If there's nothing before the at symbol:
    if email[0] == "@":
        return False
    #Establishes the domain
    email_half = email.split("@")
    domain = email_half[1]
    #If the domain name doesnt have a dot:
    if "." not in domain:
        return False
    #If the domain name starts or ends with a dot:
    if domain[0] == "." or domain[-1] == ".":
        return False
    #If the email is already saved in another contact:
    for contact in contacts:
        existing = str(contact.get("email","")).strip().lower()
        if existing == email:
            return False
    #Return True if all needed conditions are met:
    return True

#Function that validates city:
def validate_city(city : str):
    #Normalizes city:
    city = city.strip()
    #If city is empty:
    if not city:
        return False
    #If city contains anything else than hyphens, spaces or characters:
    if not all(ch.isalpha() or ch.isspace() or ch in "-" for ch in city):
        return False
    #Return True if all needed conditions are met:
    return True

#Function that validates category (expects a numeric choice):
def validate_category(category_choice : str):
    #Defines what categories exist:
    categories = ("Family","Friend","Work","School","Other")
    #Normalizes the users category choice:
    choice = str(category_choice).strip()
    #If cboice isn't a number:
    if not choice.isdigit():
        return False
    index = int(choice)
    #If choice is outside of the given categories numerical values:
    if index < 1 or index > len(categories):
        return False
    #Return True if all needed conditions are met:
    return True

#Imports datetime so that birthday can be properly validated:
from datetime import datetime

#Function that validates birthday:
def validate_birthday(birthday : str):
    #Normalizes birthday
    birthday = str(birthday).strip()
    #Check if birthday is empty:
    if not birthday:
        return False
    #Check if birthday is in ISO format:
    if len(birthday) != 10 or birthday[4] != "-" or birthday[7] != "-":
        return False
    #Check if everythong in birthday is a number (or hyphen):
    a,b,c = birthday.split("-") #Splits birthday in 3 parts
    if not (a.isdigit() and b.isdigit() and c.isdigit()):
        return False
    #Checks if each digit is in the correct date range (days, months, years):
    try:
        datetime(int(a), int(b), int(c))
    except ValueError:
        return False
    #Return True if all needed conditions are met:
    return True