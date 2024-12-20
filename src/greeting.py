# src/greeting.py
def greet(name):
    """
    Greet the user with their name.

    :param name: The name of the person to greet
    :return: A greeting string
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("What's your name? ")
    print(greet(name))