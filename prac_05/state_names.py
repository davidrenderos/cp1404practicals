"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_NAMES)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in STATE_NAMES:
        print(state_code, "is", STATE_NAMES[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Prints states with abbreviations
for state in STATE_NAMES:
    print("{:>3} is {}".format(state, STATE_NAMES[state]))
