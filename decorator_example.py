import sys
sys.path.append('src')
from decorators import my_decorator
from decorators import do_twice


def say_wee():
    print("Weeee!")


print("--- Before wrapping the function 'say_wee' with a decorator")
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


@do_twice
def say_once(word):
    return f"and the word is {word}"


print("\n--- Function 'say_once' wrapped with 'do_twice':")
say_once("bond")
