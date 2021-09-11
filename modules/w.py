from color import *
from storage import serial_number_last_odd


def main(prompt: str):
    print("<<< Wires >>>")

    args = prompt.split()
    wires = args[1]

    if len(args) < 2 or not  3 <= len(wires) <= 6:
        print("Invalid arguments.")
        print("<<< ----- >>>")
        return

    if len(wires) == 3:
        if RED not in wires:
            print(">>> Cut the second wire.")
        elif wires[-1] == WHITE:
            print(">>> Cut the last wire.")
        elif wires.count(BLUE) > 1:
            print(">>> Cut the last blue wire.")
        else:
            print(">>> Cut the last wire.")
    elif len(wires) == 4:
        if wires.count(RED) > 1 and serial_number_last_odd():
            print(">>> Cut the last red wire.")
        elif RED not in wires and wires[-1] == YELLOW:
            print(">>> Cut the first wire.")
        elif wires.count(BLUE) == 1:
            print(">>> Cut the first wire.")
        elif wires.count(YELLOW) > 2:
            print(">>> Cut the last wire.")
        else:
            print(">>> Cut the second wire.")
    elif len(wires) == 5:
        if wires[-1] == BLACK and serial_number_last_odd():
            print(">>> Cut the fourth wire.")
        elif wires.count(RED) == 1 and wires.count(YELLOW) > 1:
            print(">>> Cut the first wire.")
        elif BLACK not in wires:
            print(">>> Cut the second wire.")
        else:
            print(">>> Cut the first wire.")
    elif len(wires) == 6:
        if YELLOW not in wires and serial_number_last_odd():
            print(">>> Cut the third wire.")
        elif wires.count(YELLOW) == 1 and wires.count(WHITE) > 1:
            print(">>> Cut the fourth wire.")
        elif RED not in wires:
            print(">>> Cut the last wire.")
        else:
            print(">>> Cut the fourth wire.")
    else:
        print("Unknown solution.")

    print("<<< ----- >>>")


def help():
    print("<<< Help: Wires >>>")
    print("Enter a string of characters representing wires 1-6 from left to right respectively.")
    print("- [ ]    Color code (h c)")
    print("- [,]    None")
    print("Ex: `# w rwb,B,`")
    print("<<< ----------- >>>")
