import modules


def main(prompt: str):
    args = prompt.split()

    if len(args) < 2 or args[1][0] not in "wbksfmMWSzphld":
        print("<<< Help >>>")
        print("Enter a valid module command as an argument.")
        print("Use `l` to list modules.")
        print("<<< ---- >>>")
    else:
        getattr(modules, args[1][0]).help()
