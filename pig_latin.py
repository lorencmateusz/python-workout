def pig_latin(string):
    if string[0].lower() in 'aeiou':
        return string + 'way'
    else:
        return string[1:] + string[0] + 'ay'


print(pig_latin('python'))
print(pig_latin('air'))


def pig_latin_sentence(sentence):
    return ' '.join([pig_latin(x) for x in sentence.split(' ')])


print(pig_latin_sentence('this is a test translation'))
