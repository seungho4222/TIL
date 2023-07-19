def say_hi():
    print("Hi!")


def decorate(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper


@decorate
def say_bye():
    print("Bye~")

say_bye()