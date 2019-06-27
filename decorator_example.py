def my_decorator(func):

    def wrapper():

        print("something is happening before the function is called")
        func()
        print("Something is happening after the function is called")

    return wrapper


def say_wee():
    print("Weeee!")


print("--- Before wrapping the function 'say_wee' with a decorator\n")
say_wee()

say_wee = my_decorator(say_wee)

print("\n--- After wrapping the function 'say_wee' with a decorator")
say_wee()
