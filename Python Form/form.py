print("Welcome to Python Form")
print("Please fill information below")
print("")

name = str(input("Enter your full name: "))
birth = str(input("Enter your birth: "))
origin = str(input("Enter your origin: "))

print("")
print("please check the data before send to server")
print(name)
print(birth)
print(origin)
print("")

print("If you are ready to send the data press 1 if not press 2")
choice = int(input("Enter your number: "))
print("")

if choice == 1 :
    print("sending data to server...........")
    print("the data sended successfully")
elif choice == 2 :
    print("Exiting...........")
else:
    print("Enter right number")