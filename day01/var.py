def my_var():
    a = 42
    print("%s has a type %s" % (a, a.__class__))
    a = "42"
    print("%s has a type %s" % (a, a.__class__))
    a = "quarante-deux"
    print("%s has a type %s" % (a, a.__class__))
    a = 42.0
    print("%s has a type %s" % (a, a.__class__))
    a = True
    print("%s has a type %s" % (a, a.__class__))
    a = [42]
    print("%s has a type %s" % (a, a.__class__))
    a = {42: 42}
    print("%s has a type %s" % (a, a.__class__))
    a = (42,)
    print("%s has a type %s" % (a, a.__class__))
    a = set()
    print("%s has a type %s" % (a, a.__class__))


if __name__ == '__main__':
    my_var()