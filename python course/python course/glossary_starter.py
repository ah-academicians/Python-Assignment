""" Program framework for module 9 graded program 
    Creating a dictionary of technical terms and basic definitions
        key - the word to define
        value - the definition of the word
    Note: This isn't a usable application, as new data added is just temporary.
"""

tech_terms = { "dict": "stores a key/value pair",
               "list": "stores a value at each index",
               "map": "see 'dict'",
               "set": "stores unordered unique elements" }

def main():
    """ Keeps presenting the menu to the user till user asks to quit """
    # Present main menu 
    choice = menu()

    # While user hasn't asked to quit
    while choice != "6":
        try:
            # Run the code depending on user's choice
            choice = int(choice)
            run(choice)
        except:
            # User didn't enter a number
            print("Invalid input, please enter a valid number (1-5)")

        # Get next choice from user
        choice = menu()

def menu():
    """ Print a simple menu to the user """
    print("Systems Dictionary")
    print("1) Add a term")
    print("2) List terms")
    print("3) Get a definition")
    print("4) Delete a term")
    print("5) Print out dictionary")
    print("6) Quit")
    return input("Enter your choice: ")


def run(choice):
    """ Runs one of the actions that the user choose.  Valid choices are:
        1-5 each of which corresponds to a specific action """
    if choice == 1:
        add()
    elif choice == 2:
        list()
    elif choice == 3:
        lookup()
    elif choice == 4:
        delete()
    elif choice == 5:
        show_it()
    else:
        print("Invalid input, please enter a valid number (1-6)")


def add():
    """ Adds a term to the dictionary """
    # Get a new term and definition from the user
    term = input("Enter the term you want to add in glossary: ")
    if term not in tech_terms.keys():
        definition = input("Enter definition of the term :")
        # Add the term/definition from the user to the dictionary
        tech_terms[term] = definition
    else:
        print("term is already in glossary.")

def list():
    """ List all the terms (no definitions) that are in the dictionary.
        Once all terms have been listed, this function will also print
        the total number of entries in the dictionary """
    # TODO: Add your code here
    print("gllossary contains following terms.")
    termCount = 0
    for i in tech_terms.keys():
        print(termCount+1,") ",i)
        termCount += 1
    print("There are total ",termCount," in glossary.")

def lookup():
    """ Lookup a term and print the definition """
    # Get a term to lookup in the dictionary from the user
    term = input("Enter the term you want to seacrh in glossary: ")
    # Print the definition for the term
    # TODO: Add your code here
    try:
        print("definiton of term ",term," is ",tech_terms[term])
    except:
        print(term," is not present in glossary.")

def delete():
    """ Deletes a term from the dictionary """
    # Get a term to delete from the user
    term = input("Enter the term you want to delete: ")
    try:
        tech_terms.pop(term)
        print(term, " is deleted from glossary.")
    except:
        print("term is not in dictionary.")
    # Delete the term specified by the user from the dictionary
    # TODO: Add your code here

def show_it():
    """ Displays the full dictionary """
    print(tech_terms)
    # Display the terms and definitions nicely formatted
    # TODO: Add your code here

# Run the program
main()    
