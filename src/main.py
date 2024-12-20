# src/main.py
from greeting import greet

if __name__ == "__main__":
    name = input("What's your name? ")
    print(greet(name))
    
print('Hello from main.py')
