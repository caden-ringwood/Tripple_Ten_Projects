print("hello world")
print("learning about commits today!")


import random

greetings = [
    "Hello, Git!",
    "Greetings, developer!",
    "Welcome to branching!",
    "Hi there, coding friend!",
    "Happy coding!",
]


def get_random_greeting():
    return random.choice(greetings)


print(get_random_greeting())
print("Learning about branches today!")


def average(numbers):
    if not numbers:
        return 0  # or raise ValueError("List is empty")
    return sum(numbers) / len(numbers)
