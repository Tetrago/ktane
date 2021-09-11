from color import *
from storage import batteries, lit_indicators


def hold():
    print("Hold.")
    color = input("Color of the strip: ")

    if color == BLUE:
        print(">>> Release when the timer has a 4 in any position.")
    elif color == WHITE:
        print(">>> Release when the timer has a 1 in any position.")
    elif color == YELLOW:
        print(">>> Release when the timer has a 5 in any position.")
    else:
        print(">>> Release when the timer has a 1 in any position.")


def main(prompt: str):
    print("<<< Button >>>")

    args = prompt.split()
    if len(prompt) < 3 or len(args[1]) > 1:
        print("Invalid arguments.")
        print("<<< ------ >>>")
        return

    color = args[1]
    text = args[2].lower()

    if color == BLUE and text == "abort":
        hold()
    elif len(batteries) > 1 and text == "detonate":
        print(">>> Press and release.")
    elif color == WHITE and "car" in lit_indicators:
        hold()
    elif len(batteries) > 2 and "frk" in lit_indicators:
        print(">>> Press and release.")
    elif color == YELLOW:
        hold()
    elif color == RED and text == "hold":
        print(">>> Press and release.")
    else:
        hold()

    print("<<< ------ >>>")


def help():
    print("<<< Help: Button >>>")
    print("Pass the color character (h c) and the text.")
    print("<<< ------------ >>>")