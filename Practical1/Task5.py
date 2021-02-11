# Initial variable that will be incremented by the program.
pno = 0

for i in range(4):
    inp = input("...Baby, how do you sleep when you lie to me?").lower()

    if inp == "very well":
        pno -= 10
        print("I'm hopin' that my love will keep you up tonight.")

    elif inp == "poorly":
        pno += 20
        print("All that fear and all that pressure.")

    else:
        print("Love to you is just a game.")

print(f"You achieved {pno} points.")
