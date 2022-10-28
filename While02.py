def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    c= 0
    i = 0
    m = len(s)
    while m:
        c+=s[i].isalpha()
        i+=1

    return c