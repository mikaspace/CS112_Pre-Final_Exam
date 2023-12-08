print('CS112 PRE-FINAL EXAM')
print('------ LOOPS ------')
print('')

def praym(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
while True:
    start = int(input('Enter a number [start]: '))
    if start < 0:
        print('Enter a non-negative number.')
        continue

    end = int(input('Enter a number [end]: '))
    if end == 0:
        print('Program Terminated.')
        break
    if end <= start:
        print(f'Enter a number greater than {start}.')
        continue

    print(f'Prime numbers between {start} and {end} are: ')
    for number in range(start, end + 1):
        if praym(number):
            print(number)
