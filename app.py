import sys
from dbhelper import DBhelper

class Flipkart:

    def __init__(self):
        # connect to database
        self.db = DBhelper()
        self.user_menu()

    def loggedin_user_menu(self):
        user_input = input("""Hello how would you like to proceed?
        1. Enter 1 to see profile
        2. Enter 2 to update profile
        3. Enter 3 to delete profile
        4. Enter 4 to logout""")

    def user_menu(self):
        user_input = input("""Hello, how may I help you...
                1. Enter 1 to create an account
                2. Enter 2 to login 
                3. Press anything else to exit""")

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(0)

    def register(self):

        name = input("Enter your name")
        email = input("Enter your email")
        password = input("Enter your password")

        response = self.db.register(name,email,password)

        if response:
            print("Registration successful")
        else:
            print("Registration Failed")

        self.user_menu()

    def login(self):
        email = input("Enter your email")
        password = input("Enter your password")

        response = self.db.search(email,password)

        if len(response) != 0:
            print("Hello",response[0][1])
            self.loggedin_user_menu()
        else:
            print("Incorrect email/password")
            self.login()



obj = Flipkart()



