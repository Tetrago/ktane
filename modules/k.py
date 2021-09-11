patterns = [
    "O,A,lambda,resistor,alien,xy,cdot".split(','),
    "edot,O,cdot,cursive,*,xy,?".split(','),
    "C,w,cursive,X,bolt,lambda,*".split(','),
    "6,P,b,alien,X,?,:)".split(','),
    "psi,:),b,cdot,P,snake,dark*".split(','),
    "6,edot,#,ae,psi,H,omega".split(',')
]


def main(prompt):
    print("<<< Keypad >>>")

    args = prompt.split()
    if len(args) < 2 or len(args[1].split(',')) != 4:
        print("Invalid arguments.")
        print("<<< ------ >>>")
        return

    symbols = args[1].split(',')

    for i in patterns:
        for s in symbols:
            if s not in i:
                break
        else:
            order = []

            for s in symbols:
                order.append(i.index(s))

            order.sort()

            for o in order:
                print(f">>> Press {i[o]}.")

    print("<<< ------ >>>")


def help():
    print("<<< Help: Keypad >>>")
    print("Enter a comma-delimited string of symbols:")
    print("- O")
    print("- A")
    print("- lambda")
    print("- resistor")
    print("- alien")
    print("- xy")
    print("- cdot")
    print("- edot")
    print("- cursive")
    print("- *")
    print("- ?")
    print("- C")
    print("- w")
    print("- X")
    print("- bolt")
    print("- 6")
    print("- P")
    print("- b")
    print("- :)")
    print("- psi")
    print("- snake")
    print("- dark*")
    print("- #")
    print("- ae")
    print("- H")
    print("- omega")
    print("<<< ------------ >>>")
