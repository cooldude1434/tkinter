def add(*args):
    total = 0
    for n in args:
        total +=n

    print(type(args))
    return total


print(add(1,2,3,4,3,2,3,3,3,33,23,2,2,2,3,33,332,22))

# this exercises used for args