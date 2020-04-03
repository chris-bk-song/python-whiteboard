place = int(input('How many places? '))

num_1 = 0
num_2 = 1
print (num_2)

count = 0
while count <= place:
    sum = num_1 + num_2 
    print(sum)
    num_1 = num_2
    num_2 = sum
    count += 1