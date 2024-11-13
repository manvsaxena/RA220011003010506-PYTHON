list = ["manav","sanchari","keshav","priyansh","admin"]


admin_message = "Hello Admin, would you like to see a status report ?"
message = ", Thank you for logging in again"

for i in list:
    if(i=="admin"):
        print(admin_message)
    else:
        print("Hello " + i + message)