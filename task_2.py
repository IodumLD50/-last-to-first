

num = int(input('Введите размер массива:\n'))
while num < 1:
    num = int(input(f'Число {num} не подходит! Число не может быть меньше 1.\nВведите другое значение: ')) 
while num > 100000:
    num = int(input(f'Число {num} не подходит! Число не может быть больше 100000.\nВведите другое значение: '))   

n = list(map(int,input('Введите значения, через пробел:\n').split()))
x = 0
for i in range(len(n)):
    while n[x] < 1:
        print(f'число {n[x]} не может быть записанно по условию числа не долны быть < 1 !')
        n = list(map(int,input('Попробуйте ввести значения заново через пробел:\n').split()))
    

    while n[x] > 10e9:
        print(f'число {n[x]} не может быть записанно по условию числа не долны быть > 10e9 !')
        n = list(map(int,input('Попробуйте ввести значения заново через пробел:\n').split()))
    x +=1

a = len(n)
while num != a:
        print(f'Записей должно быть {num} !')
        n = list(map(int,input('Введите значения:\n').split()))
        a = len(n)
if num == a:
    n = n[-1:] + n[:-1] 
    
    print(f'Ответ: ',*n)


