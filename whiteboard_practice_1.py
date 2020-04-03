number_fizzbuzz = input('Please enter a number: ')

count = 1

while count <= int(number_fizzbuzz):
    if count % 3 == 0 and count % 5 == 0:
        print('fizzbuzz')
    elif count % 3 == 0:
        print('fizz')
    elif count % 5 == 0:
        print('buzz')
    else:
        print(count)
    count += 1