def word_count(file):
    words = 0
    lines = 0
    chars = 0
    all_words = []
    with open(file) as f:
        for line in f:
            chars += len(line)
            words += len(line.split(' '))
            lines += 1
            for word in line.split(' '):
                all_words.append(word)
    unique_words = len(set(all_words))
    return words, lines, chars, unique_words


print(word_count('test.txt'))
