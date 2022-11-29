def passwd_file(file):
    pass_dict = {}
    with open(file) as f:
        for line in f:
            if not line.startswith(('#', '\n')):
                user_data = line.split(':')
                pass_dict[user_data[0]] = [user_data[2]]

    return pass_dict


print(passwd_file('test.txt'))
