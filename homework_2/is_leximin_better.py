def is_leximin_better (x: list, y: list) -> bool:
    """
    gets two vectors of the same length
    @return true if x is leximin-better than y.

    >>> is_leximin_better([50,100], [50,50])
    True

    >>> is_leximin_better([3,1,3], [2,99,1])
    True

    >>> is_leximin_better([3,1,3.114], [2.9187,99,1])
    True

    >>> is_leximin_better([4,0,55,2,7], [0,3,20,7,3])
    False

    >>> is_leximin_better([0,1,2,3], [0,1,2,3])
    False

    is_leximin_better([0,1], [0,1,2,3])
    Traceback (most recent call last):
    ValueError: Vectors must be equal in length
    """

    if len(x) != len(y):
        raise ValueError("Vectors must be equal in length")
        
    x.sort()
    y.sort()

    for i in range(len(x)):
        if x[i]>y[i]:
            return True
        if x[i]<y[i]:
            return False

    return False # x = y is not considered an improvement

if __name__ == "__main__":
    import doctest
    (failures,tests) = doctest.testmod(report=True)
    print ("{} failures, {} tests".format(failures,tests))
