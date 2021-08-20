import sys


def init(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if state in states:
        print(capital_cities[states[state]])
    else:
        print("Unknown state")


if __name__ == '__main__':
    inpt = sys.argv
    if len(inpt) == 2:
        init(inpt[1])
