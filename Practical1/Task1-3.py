def tsk1():
    print("Who broke my heart?")
    print(f"My first love, {input()}, broke my heart for the first time.")


def tsk2():
    opts = dict(cops="They see me rolling. They hating. They hoping they gonna catch me riding dirty!",
                wardens="My music's so loud. I'm swanging. They hoping they gonna catch me riding dirty!")

    defstr = "Trying to catch me riding dirty!"

    inp = input("Who sees me rolling? (cops, wardens, other) ").lower()

    print(opts[inp] if inp in opts else defstr)


def tsk3():
    inp = int(input("How many times should I break free?"))

    print("\nI'm stronger than I've ever been before")

    for i in range(inp, 0, -1):
        print(f"...{i}: this is the part where I break free.")

    print("\n'Cus I can't resist it no more.")