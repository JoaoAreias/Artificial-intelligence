""" From udacity's quiz, determine which
of the mappings is a contraction mapping

A) B(x) = x/2
B) B(x) = x + 1
C) B(x) = x - 1
D) B(x) = .9*(x + 100)
"""

def apply_map(func, x, n, args=()):
    """ Apply map to x n times

    :param func: Function to be applied
    :param x: Value which you are applying the map
    :param n: How many time to iterate
    :param args: additional arguments to the function
    """
    for _ in range(n):
        x = func(x, *args)
    return x

def is_contraction(func, args=()):
    """ Test if the map will be a contraction map
    
    :param func: Mapping to be tested
    :param args: Additional arguments to be passed to the function
    """
    
    """ Choosing very close numbers so they are in to
    make sure they are in the same basin of atraction
    """
    eps = 1e-5
    x = 1.
    _x = x + eps

    y  = apply_map(func,  x, 100, args)
    _y = apply_map(func, _x, 100, args)

    return (abs(y - _y)/abs(x - _x)) < 1


print(f"x/2:  {is_contraction(lambda x: x/2)}")
print(f"x+1:  {is_contraction(lambda x: x+1)}")
print(f"x-1:  {is_contraction(lambda x: x-1)}")
print(f".9*(x+100):  {is_contraction(lambda x: .9*(x+100))}")
