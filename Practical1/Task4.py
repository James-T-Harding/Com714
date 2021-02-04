def explain(what,where):
    """
    Task 4 function.
    """
    what,where = what.lower(), where.lower()

    if what == "monster" and where == "bed":
        print("I'm friends with the monster that's under my bed")

    elif what == "doctor" and where == "hospital":
        print("You're trying to save me, stop holding your breath")

    else:
        print("You think I'm crazy, yeah, you think I'm crazy.")