#Stages of Life

age = int(input("Enter the age: "))

if(age < 2):
    print("the person is baby")
elif(age == 2 & age < 4):
    print("person is a toddler")
elif(age == 4 & age < 13):
    print("person is a kid")
elif(age == 13 & age < 20):
    print("person is a teenager")
elif(age == 20 & age < 65):
    print("person is an adult")
else:
    print("person is an elder")