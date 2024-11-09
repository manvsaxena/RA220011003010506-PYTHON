#Inviting you for the dinner

guest = ['sanchari','manav','kshitij','keshav']
message = " i'm pleased you invite for the dinner"

print("Hello, " + guest[0].title() + message)
print("Hello, " + guest[1].title() + message)
print("Hello, " + guest[2].title() + message)
print("Hello, " + guest[3].title() + message)

#print statement to person you can't make to party

busy_guest = " can't make to party"

print(guest[2].title() + busy_guest)
print(guest[3].title() + busy_guest)

#modifying the guest in list 

guest[2] = "shorya"
guest[3] = "priyansh"

#printing the invitation message for above two

print("Hello, " + guest[2].title() + message)
print("Hello, " + guest[3].title()  + message)

#using insert command now add one more guest

guest.insert(0,"nouman")
guest.insert(2,"devnit")
guest.append("abhinandan")

#printing new set of messages

print("Hello, " + guest[0].title() + message)
print("Hello, " + guest[2].title() + message)
print("Hello, " + guest[-1].title() + message)


