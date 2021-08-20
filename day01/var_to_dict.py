def print_sorted_dict(dict_my):
    list_keys = list(dict_my.keys())
    list_keys.sort()
    for key in list_keys[::-1]:
        print(str(key) + " : " + ' '.join(dict_my[key]))


def list_to_dict(d):
    dict_my = dict()
    for value, key in d:
        dict_my.setdefault(key, []).append(value)
    return dict_my


def init():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    print_sorted_dict(list_to_dict(d))


if __name__ == '__main__':
    init()