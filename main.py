"""Contains only the main loop and menu logic. It imports functions from all the other files and orchestrates them. 
It as the manager who delegates everything but does no actual work itself. 
Handles input.
It should be short — ideally under 60 lines."""

contact_input = {
    "name" : input("What is the contact's full name (both first and last one) ? "),
    "phone" : input("What is the contact's phone number ? "),
    "email" : input("What is the contact's email ? "),
    "city" : input("From which city is the contact from ?"),
    "category" : input("Please choose a category: "),
    "favourite" : input("Do you wish to add this contact as a favourite (Y or N) ? "),
    "birthday" : input("What is the person's birthday ?"),
}
