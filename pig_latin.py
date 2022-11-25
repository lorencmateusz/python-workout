def pig_latin(string):
    if string[0] in 'aeiou':
        return string + 'way'
    else:
        return string[1:] + string[0] + 'ay'


print(pig_latin('python'))
print(pig_latin('air'))
