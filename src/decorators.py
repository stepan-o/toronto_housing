import functools


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


def do_twice(func):
    """
    decorator to execute a function twice
    :param func: function
        function to be executed twice
    :return: func(*args, **kwargs)
        results of calling a function for the second time
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
