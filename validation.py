"""Contains every validation function: validate name, validate phone, validate email, validate city. 
These are completely separate from contacts.py because validation is a distinct responsibility. 
If you ever need to change the email validation rule you know exactly which file to go to without touching anything else."""

"""Validation Rules:
1) Name — cannot be empty, cannot be only spaces, must contain at least two words (first and last name), must contain only letters and spaces (no numbers or symbols), cannot already exist in the contact book unless the user explicitly confirms overwrite.
2) Phone number — must contain only digits, spaces, hyphens and the + symbol, must be between 7 and 15 digits long when all non-digit characters are stripped out, must not be identical to a phone number already saved to another contact.
3) Email — must contain exactly one @ symbol, must have at least one character before the @, must have a dot in the domain section after the @, must not be identical to an email already saved to another contact.
4) City — cannot be empty, must contain only letters spaces and hyphens (to allow names like Saint-Étienne).
5) Category — must be one of the five predefined options, selected by number from a displayed list rather than typed freely. Never accept free text for category.
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