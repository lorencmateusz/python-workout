def get_final_lina(file):
    final_line = ''
    for line in open(file):
        final_line = line
    return final_line


print(get_final_lina('test.txt'))
