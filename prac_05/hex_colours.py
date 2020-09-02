COLOURS = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4", "azure4": "#838b8b", "black": "#000000",
           "BlueViolet": "#8a2be2", "#brown2": "#8a2be2", "CadetBlue1": "#98f5ff", "chocolate": "#d2691e",
           "CornflowerBlue": "#6495ed", "DarkGoldenrod1": "#ffb90f"}

colour_choice = input("Enter colour: ")
while colour_choice != "":
    if colour_choice in COLOURS:
        print(colour_choice, "is", COLOURS[colour_choice])
    else:
        print("Invalid colour")
    colour_choice = input("Enter colour: ")
