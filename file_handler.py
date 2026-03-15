"""Contains only two functions: one that loads contacts from JSON and one that saves contacts to JSON. 
All the error handling for corrupt files lives here too. 
No other file touches the JSON directly — they all go through this file.
"""

#Import JSON Library
import json

#Function that saves contacts to a json file:
def save(contacts, path = "contacts.json"):
    with open(path, "w", encoding  = "utf-8") as f:
        json.dump(contacts, f, ensure_ascii = False, indent = 4) #Saves the data to the file

#Function that loads contacts from json file:
def load(path = "contacts.json"):
    #Try to see if file already exists:
    try:
        with open(path, "r", encoding = "utf-8") as f:
            return json.load(f) #Loads already existing data from the file
    #If file doesnt exist
    except FileNotFoundError:
        return []
    #If another error shows up:
    except json.JSONDecodeError:
        return []