string = input("文字を入れて:")

def mozi(string):
    """
    Returns float(strings)
    :param string: int, string.
    """
    return float(string)

try:
    a=mozi(string)
    print(a)
except (ZeroDivisionError,TypeError,ValueError):
    print("floatになるやつにして")
