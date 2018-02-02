import random

#пустая клетка
EMPTY_MARK = 'X'

#словарь возможных ходов 
MOVES = {
         'w': -4,
         's': 4,
         'a': -1,
         'd': 1
}

START_FIELD = {
        1: 1, 2: 2, 3: 3, 4: 4,
        5: 5, 6: 6, 7: 7, 8: 8,
        9: 9, 10: 10, 11: 11, 12: 12,
        13: 13, 14: 14, 15: 15, 16: EMPTY_MARK
    }

"""
Функция shuffle_field перемешивает игровое поле и возвращает его.
Перемешивание происходит путем вызова функции perform_move
случайное кол-во раз. Фуекция perform_move вызывается с флагом printed_err=False
что бы не выводить ошибку каждый раз, когда ход окажется не верным.
"""


def shuffle_field(field):
    new_field = field.copy()
    for i in range(random.randint(40, 100)):
        perform_move(new_field, random.choice(list(MOVES.values())), printed_err=False)
    return new_field

    # Еще один способ перемешать поле
    # По правилу: если кол-ло во любых переставлений от начального вида - четное, то
    # на этом поле можно выиграть (это правило я в инете нашел, не знаю на сколько оно рабочее =))
    # field_ok = False
    # while not field_ok:
    #     rand_list = random.sample(range(1, 16), 15)
    #     for key in field:
    #         if field[key] == 'X':
    #             break
    #         else:
    #             field[key] = rand_list[key - 1]
    #     n = 0
    #     for key in field:
    #         if field[key] == key:
    #             n += 1
    #     if n % 2 == 0 and n != 0:
    #         field_ok = True

"""
Функция perform_move перемещает пустую клетку по полю в зависимости от хода игрока.
Функция принимает два позиционных аргумента: игровое поле и ход игрока
и один именнованый аргумент по умолчанию равный True,
который показывает печатать ли ошибку хода.

"""


def perform_move(field, key, printed_err=True):
    for square in field:
        if field[square] == 'X':
            try:
                if key == 1 and square in (4, 8, 12, 16):
                    raise KeyError
                elif key == -1 and square in (1, 5, 9, 13):
                    raise KeyError
                field[square] = field[square + key]
                field[square + key] = 'X'
                break
            except KeyError as e:
                if printed_err:
                    print('Не верный ход. Попыдка выйти за рамки поля!')
    return field


"""
В функции handle_user_input проеряется пользовательский ввод
который долже соответствовать ключам словаря MOVES
Если ввод верный функция вернет значение хода из словаря.

"""


def handle_user_input():
    try_moving = False
    moving = None
    while not try_moving:
        moving = input('Пожалуйста делайте свой ход: ')
        if moving.lower() not in ('w', 'a', 's', 'd'):
            print('Пользуйтесь, командами (w, a, s, d)')
        else:
            try_moving = True
    return MOVES[moving.lower()]


"""
Функция print_field выводит поле на экран в формате 4х4

"""


def print_field(field):
    for key, value in field.items():
        if key % 4 != 0 and value == 'X':
            print(value, ' ', end=' ')
        elif key % 4 != 0 and value < 10:
            print(value, ' ', end=' ')
        elif key % 4 != 0 and value >= 10:
            print(value, '', end=' ')
        else:
            print(value, end='\n')
    print('\n')


"""
Функция is_game_finished сравнивает поле с START_FIELD
если они равны возвращает True

"""


def is_game_finished(field):

    if field == START_FIELD:
        print('<<<Ура, вы победили!!!>>>')
        return True
    else:
        return False


def main():
    over_game = False
    start_field = shuffle_field(START_FIELD)
    print_field(start_field)
    new_field = start_field

    while not over_game:
        moving = handle_user_input()
        new_field = perform_move(new_field, moving)
        print_field(new_field)
        over_game = is_game_finished(new_field)
    print('Конец игры')


print('<<< Добро пожаловать в игру "Пятнашки" ! >>>')
print('Управление происходи с помощью клавишь WASD.')
print('Если хотите выйти из игры нажмите сочетание клавишь Ctrl+C.\n')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('Игра закрыта')

