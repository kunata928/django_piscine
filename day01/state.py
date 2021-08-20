import sys


def init(capital_city):
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
    for key, value in capital_cities.items():
        if value == capital_city:
            for state, ab in states.items():
                if ab == key:
                    print(state)
                    return
    print("Unknown state")


if __name__ == '__main__':
    inpt = sys.argv
    if len(inpt) == 2:
        init(inpt[1])
