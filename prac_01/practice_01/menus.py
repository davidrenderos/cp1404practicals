user_name = input("Enter Name: ")
MENU = input("(H)ello\n(G)oodbye\n(Q)uit").upper()
while MENU != "Q":
    if MENU == "H":
        print("hello", user_name)
    elif MENU == "G":
        print("goodbye", user_name)
    else:
        print("Invalid choice")
    MENU = input("(H)ello\n(G)oodbye\n(Q)uit").upper()
print("Finished.")
