def fun():
    d = [(1, 2), (3, 4), (5, 6), (7, 8)]
    for k, v in d:
        print('key: ', k,'Value: ', v)
    
    d = {'a': 1}
    print(d.items())

fun()