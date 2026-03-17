def add_all(*args):
    return sum(args)
if __name__ == "__main__":
    print(add_all(1, 2, 3, 4, 5))
    print(add_all(10, 20, 30))
    print(add_all())
    print(add_all(1.5, 2.5, 3.0))
    print(add_all(-1, -2, -3))
    print(add_all(1, 2.5, -3, 4.0))
