def dictdiff(dict1, dict2):
    output = {}
    all_keys = dict1.keys() | dict2.keys()

    for key in all_keys:
        if dict1.get(key) != dict2.get(key):
            output[key] = [dict1.get(key), dict2.get(key)]
    return output


d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}

print(dictdiff(d3, d4))
