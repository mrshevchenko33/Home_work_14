my_num = input('Enter your num: ')
result = 1

for i in my_num:
    result *= int(i)

while result > 9:
    my_num = str(result)
    result = 1
    for i in my_num:
        result *= int(i)
print(result)
