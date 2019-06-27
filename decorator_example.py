def my_decorator(func):
    """
    Put simply: decorators wrap a function, modifying its behavior.
    :param func: function
        function to be wrapped
    :return: wrapper: function
        wrapped function
    """
    def wrapper():
        """
        function func with a wrapper
        :return: None
        """

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

# ---------- analogous script using Python @ symbol for decorators
@my_decorator
def say_woohoo():
    print("WooHoooo!")


print("\n--- Function 'say_woohoo' wrapped with 'my_decorator':")
say_woohoo()
