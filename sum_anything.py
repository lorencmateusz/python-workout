def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:0]:
        output += item
    return output
