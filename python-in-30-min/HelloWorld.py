# Task 1 -> Ask for the name of the user and greet him by displaying "Hello <user_name>" on the screen.

"""
Multi-line
comment
here
"""

# print("Date is April 18, 2020")  # Print statement

# month = "April"
# date = 18
# year = 2020
# # year = "Two thousand twenty"

# # print("Date is " + month + " " + date + ", " + year)  # ERROR

# print("Date is " + month + " " + str(date) + ", " + str(year))
# print("Date is {} {}, {}".format(month, date, year))

userName = input("What is your name? ")


def greetUser(name):
    """[summary]

    Arguments:
        name {string} -- ["Username"]

    Returns:
        [string] -- ["Hello <user_name>"]
    """
    return "Hello {}!".format(userName)


def greetUser1(name):
    # name is a string = array of characters
    # if name = "rahul" mean r is the 0th index and a is the 1st and so on
    return "Hello {}{}!".format(name[0].upper(), name[1:])


def greetUser2(name):
    """
    Check whether name is alphanumeric only as names cannot have special chars. 
    Throw exception if a string name has special char
    """

    if str.isalnum(name):  # means [a-z], [A-Z], [0-9] -> True
        return greetUser1(name)
    else:
        raise ValueError("Name cannot have special characters")
        # print("1")


# print(greetUser(userName))
# print(greetUser1(userName))
try:
    print(greetUser2(userName))
    print("\nTEST")
except ValueError:
    userName = input(
        "Special Character in username not allowed. What is your name? ")
    print(greetUser2(userName))

# * Important info
# ! Alerts
# ? Should this added? For Queries?
# TODO : Refactor Method
