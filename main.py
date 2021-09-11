import modules
import storage


def input_data():
    print("<<< Data >>>")
    storage.serial_number = input("Serial number: ").upper()
    storage.batteries = input("Comma delimited string of batteries [a,a,d]: ").split(',')
    storage.lit_indicators = input("Comma delimited list of lit indicators [snd,trn]: ").split(',')
    print("<<< ---- >>>")


def input_modules():
    modules_list()

    while modules_prompt():
        pass


def modules_prompt() -> bool:
    prompt = input("# ")
    if len(prompt) == 0:
        return True
    elif prompt[0] == 'd':
        return False
    elif prompt[0] == 'r':
        print("<<< Reset >>>")
        input_data()
        print("<<< ----- >>>")
    elif prompt[0] == 'l':
        modules_list()
    elif prompt[0] in "wbksfmMWSzphld":
        getattr(modules, prompt[0]).main(prompt)

    return True


def modules_list():
    print("<<< Modules >>>")
    print("Please enter the details of ever module on the device.")
    print("Unless otherwise specified, enter lowercase letters.")
    print("- [w]    Wires")
    print("- [b]    Button")
    print("- [k]    Keypad")
    print("- [s]    Simon Says")
    print("- [f]    Who's on First")
    print("- [m]    Memory")
    print("- [M]    Morse Code")
    print("- [W]    Complicated Wires")
    print("- [S]    Wire Sequences")
    print("- [z]    Mazes")
    print("- [p]    Passwords")
    print("- [h_]   Help")
    print("- [l]    List modules")
    print("- [d]    Done")
    print("- [r]    Reset")
    print("<<< ------- >>>")


if __name__ == '__main__':
    input_data()
    input_modules()
