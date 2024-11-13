# List of users
users = []  # Empty list

# Check if the list of users is empty
if not users:
    print("We need to find some users!")
else:
    # If the list is not empty, continue with the original logic (e.g., greet the admin)
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")

# Remove all usernames from the list (to test the message when the list is empty)
users.clear()

# Check again if the list is empty
if not users:
    print("We need to find some users!")
