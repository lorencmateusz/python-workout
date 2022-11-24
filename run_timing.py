def average_time():
    total_time = 0
    total_distance = 0
    while True:
        run_time = input('Enter 10km time: ')
        if run_time == '':
            return f'Avg is {total_time/(total_distance/10)}'
        total_time += int(run_time)
        total_distance += 10


print(average_time())