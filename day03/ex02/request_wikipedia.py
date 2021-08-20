import requests
import json
import dewiki
import sys


class wiki(object):

    def __init__(self):
        pass
    
    href = ""

    params = {
        action : 
        search :
        prop :
        format :
        inprop : 
    }



if __name__ == '__main__':
    inp = sys.argv
    if len(inp) == 2:
        init(inp[1])
    else:
        print("only one link must be writted")