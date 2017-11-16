# linear search
def linear(a, n):
    '''
    a: a list of positive integers
    n: key (positive integer)
    returns a boolean True or False
    '''
    for i in range(len(a)):
        if a[i] == n:
            return True
    return False


