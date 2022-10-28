def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    c= 0
    i = 0
    m = len(s)-1
    while m:
        c+=s[i].isdigit()
        i+=1

    return c