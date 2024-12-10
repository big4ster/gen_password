#Password generated
import string
import random

random_punctuation = random.randint(0, 4)
#use_punctuation = True Не реализовано
#use_punctuation = True
punctuation = ['!','~','#','$','*']
print('''
***** Генератор паролей *****
1. быстрая генерация пароля 
2. настраиваемая длинна генерации и сложности пароля
3. выход
''')
def generate_password(user_count):
    count = user_count - 1
    gen_string = random.sample(list(string.ascii_lowercase),user_count) + random.sample(list(string.ascii_uppercase),user_count) + list(string.digits)
    gen_random = random.sample(gen_string, count) + list(punctuation[random_punctuation])
    gen_random2 = random.sample(gen_random, user_count)
    print(''.join(map(str, gen_random2)),sep='')
gen = True
while gen:
    userсhoice = int(input('Выберите параметр генерации: '))
    if userсhoice == 1:
        generate_password(10)
        while True:
            next = input('Повторить генерацию? Да - Enter \ Нет')
            if next == '':
                generate_password(10)
            else: break

    elif userсhoice == 2:
        usergen = int(input('Укажите количество символов: '))
        generate_password(usergen)
        while True:
            next = input('Повторить генерацию? Да - Enter \ Нет')
            if next == '':
                generate_password(usergen)
            else: break
    elif userсhoice == 3:
        break
    else:
        print('Введите валидный параметр')