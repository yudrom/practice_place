# 1)
n = int(input())  # через 1-й вид цикла
summa = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        summa += i
print(summa)

n = int(input())  # через 2-й вид цикла
summa = 0
while n != 0:
    if n % 2 == 0:
        summa += n
    n -= 1
print(summa)

# 2)
m = ['dragon', 'knight', 'fire', 'tie', 'elephant']  # через 1-й вид цикла
temp = ''
for i in m:
    if len(i) > len(temp):
        temp = i
print(temp)

m = ['dragon', 'knight', 'fire', 'tie', 'elephant']  # через 2-й вид цикла
temp = ''
while len(m) != 0:
    if len(m[0]) > len(temp):
        temp = m[0]
    del(m[0])
print(temp)

# 3)
def faq():
    n = int(input('1. Введите число для подсчёта факториала: '))
    total = 1
    for i in range(n, 0, -1):
        total *= i
    print(f'2. Полученный факториал от числа {n} = {total}')

faq()

# 4)
m = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
for i, j in enumerate(m):
    if (i + 1) % 3 == 0:
        print(i, j)

# 5)
n = int(input('Введите число: '))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f'{i} * {j} = {i*j}', end='  ')
    print()

# 6)
n = int(input())  # через 1-й вид цикла
cnt = 0
for i in str(n):
    if i.isdigit():
        cnt += 1
print(cnt)

n = int(input())  # через 2-й вид цикла
cnt = 0
while cnt != len(str(n)):
    cnt += 1
print(cnt)

# 7)
n = input()
a = n.split()
if ''.join(a) == ''.join(a)[::-1]:
    print(f'Строка "{n}" является палиндромом')
else:
    print(f'Строка "{n}" не является палиндромом')

# 8)
a = [1, 2, 3, 4, 4, 5, 6]
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        print('Список содержит дубликаты')
        break
else:
    print('Список не содержит дубликаты')

# 9)
a = [1, 2, 3, 4, 4, 5, 6, 2, 8, 13, 9, 4]  # через 1-й вид цикла
for i in a:
    if a.count(i) != 1:
        a.remove(i)
a.sort()
print(a)

a = [1, 2, 3, 4, 4, 5, 6, 2, 8, 13, 9, 4]  # через 2-й вид цикла
cur_ind = 0
while cur_ind < len(a):
    cur_znach = a[cur_ind]
    while a.count(cur_znach) != 1:
        a.remove(cur_znach)
    else:
        cur_ind += 1
a.sort()
print(a)

# 10)
s = input()
for i in range(len(s)-1, -1, -1):
    if s[i].isalpha():
        print(s[i])

# 11)
day = 1
days_of_the_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
print(' '.join(days_of_the_week))
for _ in range(0, 7):
    for j in range(day, day + 7):
        if j < 10:
            print(j, end='  ')
        if 10 <= j < 32:
            print(j, end=' ')
    day += 7
    print()


