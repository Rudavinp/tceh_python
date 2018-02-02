

#TASK1

def is_panogram(string):
    list_alpha = []

    if ord(string[1]) > 1000:
        srt_alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    else:
        srt_alpha = 'abcdefghijklmnopqrstuvwxyz'
    for s in srt_alpha:
        list_alpha.append(s)
    for letter in string:
        try:
            list_alpha.remove(letter.lower())
        except ValueError:
            continue
    if len(list_alpha) == 0:
        print('This panogram!')
    else:
        print('This not panogram.')
        print(list_alpha)

#is_panogram('Широкая электрификация южных губерний даст мощный сельского хозяйства.')


#TASK2


def field_dreams(string):
    list_guess_char =  []
    list_string_char = []

    for i in range(len(string)):
        list_guess_char.append('_')

    print('Начинаем играть ')
    for i in list_guess_char:
        print(i, end='')
    print('')

    for s in string:
         list_string_char.append(s)

    while True:
        char = input('Введите букву: ')
        try:
            index_char = list_string_char.index(char)
            list_guess_char[index_char] = char

            print('Есть такая буква')
            for i in list_guess_char:
                print(i, end='')
            print('')

            if '_' not in list_guess_char:
                print('Поздравляем вы отгадали слово {}'.format(string))
                break

            list_string_char[index_char] = '_'

        except ValueError:
            if char in list_guess_char:
                print('Такую букву уже называли.')
            else:
                print('Такой буквы нет')




#--TASK3--#

"""Третью задачу я честно подсмотрел в интернете =)
    :param disc: кол-во дисков в башне
    :param from_pole: с какого колышка снимается диск
    :param to_pole: на какой колышек надевается диск
    :param with_pole: промежуточный колышек"""


def move_disc(disc, from_pole, to_pole, with_pole):
    if disc >= 1:
        move_disc(disc - 1, from_pole, with_pole, to_pole)
        print("moving disk {} from {} to {}".format(disc, from_pole, to_pole))
        move_disc(disc - 1, with_pole, to_pole, from_pole)
















