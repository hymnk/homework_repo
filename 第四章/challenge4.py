def a(x):
    """
    Print y And exec b(y)
    :param x: int.
    """
    y = int(x) / 2
    print(y)
    b(y)

def b(y):
    """
    Print(y * 4)
    """
    print(y * 4)

a(4)