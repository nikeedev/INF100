running = True
while running:
    cmd = input("Hi! Do you want to talk to me?\n")

    if cmd == "yes":
        print("That's cool!")
    elif cmd == "no":
        running = False
        print("All right, bye!")
    else:
        print("That's cool!")

