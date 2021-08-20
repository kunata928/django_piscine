import sys
import os
import re


def cv_html(data, settings, file_name):
    for key in settings:
        if data.find(str('{' + key + '}')):
            data = data.replace(str('{' + key + '}'), settings[key][0])
    try:
        with open(str(file_name) + ".html", "w") as file_html:
            file_html.write(data)
    except:
        print('cannot create file :(')
        return

def open_template(file):
    splited_path = os.path.splitext(file)
    if splited_path[1] != ".template":
        print("Not a valid file. Please write 'smth.template'.")
        return
    if not os.path.exists(file):
        print("file not exists")
        return
    if not os.path.isfile(file):
        print("no, try agane with file")
        return
    try:
        with open(file, "r") as template:
            data = template.read()
    except:
        print('bad file or acсess')
        return
    return data


def init(file):
    settings = dict()
    data = open_template(file)
    if not data:
        return 
    lines = open("settings.py", "r").readlines()
    for line in lines:
        if "=" in line:
            key = line.split('=')[0].strip(' \"\'')
            value = line.split('=')[1].strip(' \"\'\n')
            settings.setdefault(key, []).append(value)
    cv_html(data, settings, os.path.splitext(file)[0])
    

if __name__ == '__main__':
    inpt = sys.argv
    if len(inpt) == 2:
        init(inpt[1])
