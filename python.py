
bob = 1
while True:
    password = input("Password?")
    if password == 12345:
        print("correct")
        break
    else:
        print("incorrect")
        bob += 1

        