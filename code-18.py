current_users = ["manav","sanchari","priyansh","anaenay","keshav"]
new_users = ["manav","sanchari","gaurav","vijay","prisha"]
current_user_upper = [user.upper() for user in current_users]

for j in new_users:
    if j.upper() in current_user_upper:
        print("Dear " + j + " this username is already is used!")
    elif j in current_users:
        print("Dear " + j + " this username is already is used!")
    else:
        print("Username is available! " + j)