# Define a class for user accounts
class User:
    # Initialize the user object with username and password attributes
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Define a method to check if the user credentials are valid
    def login(self, username, password):
        return self.username == username and self.password == password

# Create a list to store the user objects
users = []

# Define a function to create a new user account
class UserFunctionality():
    def signup():
    # Ask the user to enter a username and a password
     username = input("Enter a username: ")
     password = input("Enter a password: ")

    # Check if the username is already taken
     for user in users:
        if user.username == username:
            print("Username already exists. Please try again.")
            return

    # Create a new user object and add it to the list
     user = User(username, password)
     users.append(user)
     print("Account created successfully.")

# Define a function to log in an existing user account
    def login():
    # Ask the user to enter a username and a password
     username = input("Enter your username: ")
     password = input("Enter your password: ")

    # Check if the user credentials are valid
     for user in users:
        if user.login(username, password):
            print("Login successful.")
            return

    # If no match is found, print an error message
    print("Invalid username or password. Please try again.")

# Define a function to ask the user to choose between login or signup
class main(UserFunctionality):
    # Loop until the user chooses to exit
    while True:
        # Print the menu options
        print("Welcome to the Python OOP login/signup program.")
        print("Please choose an option:")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

        # Get the user input
        choice = input("Enter your choice: ")

        # Perform the corresponding action
        if choice == "1":
            UserFunctionality.login()
        elif choice == "2":
            UserFunctionality.signup()
        elif choice == "3":
            print("Thank you for using the program. Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function
main()

if __name__=='main':
    user1=User("vishnu","vis")
    User.users.append(user1)
