def add_vote(x) -> int:
    """
    Adds a vote to the candidate
    int: power of vote to add
    """
    try:
        int(x)
        x += 1
    except:
        quit("Error")
    return x

def total_votes(x, y) -> int:
    """
    Gives the total amount of votes cast
    int: total votes
    """

    try:
        total = x + y
        int(total)
    except:
        quit("Error")
    return total


