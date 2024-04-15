# 1)
a = input('Введите строку: ')
print(a[::-1])

# 2)
a = input()
first_h = a.find('h')
last_h = a.rfind('h')
a = a[:first_h + 1] + a[first_h + 1:last_h].replace('h', 'H') + a[last_h:]
print(a)

# 3)
a = input()
print(len(a.split()))

# 4)
a = input()
print(a.strip().count(' ') + 1)

# 5)
words = input().split()
print(words[-1] + ' ' +words[0])

# 6)
a = input().split()
print(a[0], a[1][0] + '.', a[2][0] + '.', sep=' ')

# 7)
a = [6, [1.3, [3+2j, [[], 9, "Иголка"]]]]
print(a)

# 8)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # 1-й способ
a.extend(b)  # 2-й способ
print(a)

# 9)
a = [2, 1, 3]
b = [9, 3, 2]
print(sorted(set(a + b)))

# 10)
a = input().split()
if len(a) == len(set(a)):
    print('Все числа уникальные')
else:
    print('Не все числа уникальные')

# 11)
date_dict = {'year': 2024, 'month': 4, 'day': 14}
print(date_dict.get('year'), date_dict.get('month'), date_dict.get('day'), sep='-')

# 12)
a = [int(i) for i in input().split(',')]
print(a)
print(tuple(a))

# 13)
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
print(students | employees, students.union(employees))
print(students & employees, students.intersection(employees))
print(employees - students, employees.difference(students))
print(students ^ employees, students.symmetric_difference(employees))

# 14)
array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]

tr_array = []
for i in range(len(array[0])):
    column = []
    for stroka in array:
        column.append(stroka[i])
    tr_array.append(column)

for stroka in tr_array:
    print(stroka)

# 15)
default = ''
for j in range(0, 5):
    default += 'X'
    default += 'xx' * j
    default += 'X'
    print(default)
    default = ''