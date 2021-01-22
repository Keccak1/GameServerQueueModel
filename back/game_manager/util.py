def to_iterarable(l):
    try:
        iter(l)
    except TypeError:
        return [l]
    return l


