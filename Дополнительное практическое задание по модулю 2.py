def get_password(number):
    password = ''
    for i in range(1, number):
        for h in range(2, number):
            if h  <= i:
                continue
            if number % (i + h) == 0:
                password += str(i) + str(h)
    return password

n = int(input('Введите целое число от 3 до 20: '))

result = get_password(n)
print('Пароль:', result)