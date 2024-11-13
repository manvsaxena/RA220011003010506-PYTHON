current_user = ["manav","sanchari","keshav","prisha","aditya"]

new_users = ["MANAV","Sanchari","kshitij","pandiraj"]

for i in new_users:
    if(i.lower() in current_user):
        print("person will need to enter a new username! ")
    else:
        print("username is available! ")



