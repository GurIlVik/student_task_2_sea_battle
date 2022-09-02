from random import randint
from unittest import result

# Игра морской бой:
# 1 модуль приветствия
# 1.2 модуль перезапуска программы
# 2 игровой модуль
# 2.1 комп загадывает количество кораблей:
# 2.1.1 загадать место 1ого элемента и уточнить положение по вертикали
# 2.1.2 удлинение коробля по этому показателю
# 2.1.3 проверка на возможнотсь его так постановки в блок листе
# 2.1.4 запись в блок лист и лист кораблей новых координат
# 2.1.5 сохранение и распечатка результата
# 2.2 ход игрока в цикле
# 2.2.1 проверка хода на правильную запись
# 2.2.2 внесение изменений в лист кораблей (при уничтожении фиксация факта с принтем)
# 2.2.3 принтинг нового поля после хода
# 2.2.4 в случает отсутствия кораблей распечатка результатов игры

# модуль расстановки кораблей компьютером
def module_computer_position_ship():
    # функция предоставления координат клетки для коробля
    def coordinaty(x=1):
        if x == 1:
            coord_x = randint(1, 10)
            coord_y = randint(1, 10)
        return coord_x, coord_y

    # функция рандомно определяющая положени по вертикали
    def position_tilt():
        result = randint(1, 2)
        return result

    # проверка позиции корабля в файле
    def control_position_ship(ship):
        result = False
        for i in ship:
            file_control = open('file_control.txt', 'r', encoding='utf-8')
            for line in file_control:
                crd = coord(i[0])
                if crd == line[0] and str(i[1]) in line:
                    result = True
            file_control.close()
        return result

    # вставление буквенной координаты
    def coord(crd):
        result = ''
        if crd == 1:
            result = 'а'
        elif crd == 2:
            result = 'б'
        elif crd == 3:
            result = 'в'
        elif crd == 4:
            result = 'г'
        elif crd == 5:
            result = 'д'
        elif crd == 6:
            result = 'е'
        elif crd == 7:
            result = 'ж'
        elif crd == 8:
            result = 'з'
        elif crd == 9:
            result = 'и'
        elif crd == 10:
            result = 'к'
        else:
            result = 'ё'
        return result

    # запись данных о корабле в файл
    # ????
    def memory_position_ship(ship):
        for i in ship:
            with open('file_control.txt', 'a', encoding='utf-8') as file:
                srting_of_save = ''
                for j in range(-1, 2):
                    coord_1 = coord(i[0] + j)
                    srting_of_save += coord_1
                    for n in range(-1, 2):
                        srting_of_save += str(i[1] + n)
                    file.write(srting_of_save + '\n')
                    srting_of_save = ''

    # функция блокировки не правильной расстановки кораблей
    def blok_list_position(elem, grid_coordinates_ship):
        result = True
        if elem == len(grid_coordinates_ship):
            result = control_position_ship(grid_coordinates_ship)
        else:
            result = True
        return result

    # функция расстановки кораблей
    def ships_coordinates(elem):
        grid_coordinates_ship = []
        cycle_password = True
        result = []
        # dict_blok = {}
        while cycle_password == True: 
            coordinat_x, coordinat_y = coordinaty()
            tilt_ship = position_tilt()
            grid_coordinates = [] 
            if tilt_ship == 1:
                for i in range(elem):
                    if coordinat_x + elem > 10:
                        grid_coordinates = [coordinat_x - i, coordinat_y]
                    else:
                        grid_coordinates = [coordinat_x + i, coordinat_y]           
                    grid_coordinates_ship.append(grid_coordinates)
                    grid_coordinates = []
            else: 
                for i in range(elem):
                    if coordinat_y + elem > 10:
                        grid_coordinates = [coordinat_x, coordinat_y - i]
                    else:
                        grid_coordinates = [coordinat_x, coordinat_y + i] 
                    grid_coordinates_ship.append(grid_coordinates)
                    grid_coordinates = []
            cycle_password = blok_list_position(elem, grid_coordinates_ship)
            if cycle_password == False:
                result = grid_coordinates_ship
                memory_position_ship(grid_coordinates_ship)
            else:
                cycle_password = False

        return result

    # открытие файла контроля позиции
    def open_file_control_position():
        nachalo = 'файл проверки позиции кораблей'
        file_control = open('file_control.txt', 'w', encoding='utf-8')
        file_control.write(nachalo + '\n')
        file_control.close()
        
    # модуль определения листа расстановки кораблей
    def computer_position_ship():
        list_position = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        list_n = []
        open_file_control_position()
        for i, elem in enumerate(list_position):
            list_n.append(ships_coordinates(elem))
            list_n.append('K')
            list_n.append(list_position[i])
            list_position[i] = list_n
            list_n = []
        count = 0
        while count < 10:
            for i, elem1 in enumerate(list_position):
                if elem1[0] != []:
                    count += 1
                else:
                    list_n.append(ships_coordinates(elem1[-1]))
                    list_n.append('K')
                    list_n.append(elem1[-1])
                    list_position[i] = list_n
                    list_n = []
            if count < 10:
                count = 0
        return list_position

    return computer_position_ship()

# грамматический модуль
def grammar_module(number, word_1=''):
    # вспомагательный грамматический модуль
    def auxiliary_grammar_module(num):
        code_num = 0
        if len(str(num)) == 1:
            if num == 1:
                code_num = 1
            elif num in (2, 3, 4):
                code_num = 2
            else:
                pass
        else:
            if str(num)[-2] == '1':
                code_num = 0
            else:
                if str(num)[-1] == '1':
                    code_num = 1
                elif str(num)[-1] in ('2', '3', '4'):
                    code_num = 2

        return code_num
    
    # словарь грамматического модуля
    def grammar_dict(word_1):
        result = []
        if word_1 == 'игра':
            result = ['игр', 'игра', 'игры']
        if word_1 == 'попытка':
            result = ['попыток', 'попытку', 'попытки']
        return result

    # модуль определения окончания русского языка
    def grammar_function(number, word_1):
        number = auxiliary_grammar_module(number)
        word = grammar_dict(word_1)
        result = ''
        if number == 0:
            result += word[0]
        elif number == 1:
            result += word[1]
        else: 
            result += word[2]
        print(result)
        return result
        
   
    return grammar_function(number, word_1)

# модуль получения хода игрока
def module_gamer_moves():

    # проверка хода инрока
    def checking_gamers_progress(step):
        result = False
        if len(step) != 3:
            print(f'Вы ввели не три знака')
            result = True
        else:
            if step[0] not in 'абвгдежзикАБВГДЕЖЗИК':
                print(f'Вы ввели первый знак не ту букву или не на русской расскладке')
                result = True
            else:
                if step[2] < '0' or step[2] > '9':
                    print(f'Вы ввели ошибочный третий знак должна быть цифра')
                    result = True
                else:
                    result = False
        return result

    # преобразование хода игрока
    def converting_players_move(step):
        result = []
        for i, elem in enumerate('абвгдежзик'):
            if elem == step[0]:
                result.append(i+1)
            else:
                pass
        for i, elem in enumerate('АБВГДЕЖЗИК'):
            if elem == step[0]:
                result.append(i+1)
            else:
                pass
        if step[2] == '0':
            result.append(10)
        else:
            result.append(int(step[2]))
        return result

    # цикл получения значения
    def cycle_gamer_moves():
        password = True
        result = []
        while password:
            step_number = input(f'''Сделайте ваш ход (например : а-0) из трех знаков 
            обязательно буква первая и цифра последняя разделитель может быть лбой
            ОСТОРОЖНО - ВМЕСТО 10 НЕОБХОДИОМО ВВЕСТИ 0 (ноль): \n''')
            password = checking_gamers_progress(step_number)
            if password == False:
                result = converting_players_move(step_number)

        return result

    return cycle_gamer_moves() 

# проверка на полностью затопленность корабля
def ship_gum(elem):
    res = False
    for elem2 in elem[0]:
        if elem2 != []:
            res = True
    return res

# лист внесения точек вокруг корабля:
def field_around_ship(list_K, gemer_move):
    list_pro = []
    for j in range(-1, 2):
        q = gemer_move[0] + j
        if q < 1 or q > 10:
            pass
        else:
            for n in range(-1, 2):
                w = gemer_move[1] + n
                if w < 1 or w > 10:
                    pass
                else:
                    list_pro.append(q)
                    list_pro.append(w)
                    list_K.append(list_pro)
                    list_pro = []
    for i, elem in enumerate(list_K):
        if elem == gemer_move:
            list_K.pop(i)
    return list_K

# проверка на попадание в корабль
def hit_check(ship_positions=[], gemer_move=[], list_X=[], list_O=[], list_K=[]):
    res = False
    result = False
    for i, elem in enumerate(ship_positions):
        for j, elem2 in enumerate(elem[0]):
            if elem2 == gemer_move:
                list_X.append(elem2)
                elem[0][j] = []
                check_gum = ship_gum(elem)
                res = True
                if check_gum == True:
                    print('Попадание: корабль подбит... ')
                    list_K = field_around_ship(list_K, gemer_move)
                else:
                    print(f'Попадание: {elem[2]} палубный корабль затонул')
                    list_K = field_around_ship(list_K, gemer_move)
                    ship_positions.pop(i)
                    result = True
           
    if res != True:
        if gemer_move == []:
            pass
        else:
            print('молоко, делайте следующий ход')
            list_O.append(gemer_move)
# результ в правде показывает на уничтоженный корабль а рес просто на попадание 
    return res, ship_positions, list_X, list_O, list_K, result

# функция очищения списка от дублирующих элементов
def clearing_list(list_T=[], list_X=[], list_O=[]):
    list_T_1 = []
    if list_T != []:
        for elem in list_T:
            if elem not in list_X:
                if elem not in list_O:
                    if elem not in list_T_1:
                        list_T_1.append(elem)
            list_T = list_T_1.copy()
    return list_T


# модуль проверки хода и распечатки поля
def module_pole_print(ship_positions=[], gemer_move=[], list_X=[], list_O=[], list_K=[], list_T=[]):
    str_1 = ['  ','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10',]
    str_2 = '|\ А Б В Г Д Е Ж З И К'
    symbol_1 = '~~'
    symbol_2 = ' X'
    symbol_3 = "  "
    symbol_4 = ' o'
    
    hit, ship_positions, res_x, res_o, res_k, death_ship= hit_check(ship_positions, gemer_move, list_X, list_O, list_K)
    list_X = res_x
    list_O = res_o
    list_K = res_k
    print(death_ship)
    if death_ship == True:
        list_T = list_K.copy()
        print(list_T)
        # list_T = clearing_list(list_T, list_K, list_O)

    print(str_2)
    list_1 =[]
    for i in range(1, 11):
        list_1.append(str_1[i])
        for j in range(1, 11):
            figura = True
            if list_T == []:
                pass
            else:
                list_T = clearing_list(list_T, list_X, list_O)  
                for elem in list_T:
                    if elem[1] == i:
                        if elem[0] == j:
                            list_1.append(symbol_3)
                            figura = False
            if list_O == [[]]:
                pass
            else:
                for elem2 in list_O:
                    if elem2[1] == i:
                        if elem2[0] == j:
                            list_1.append(symbol_4)
                            figura = False
            if list_X == []:
                pass
            else:
                for elem3 in list_X:
                    if elem3[1] == i:
                        if elem3[0] == j:
                            list_1.append(symbol_2)
                            figura = False
            if figura == True:
                list_1.append(symbol_1)
            strings = ''.join(list_1)
        list_1 = []
        print(strings) 
        strings = ''  
    return ship_positions, list_X, list_O, list_K, list_T

def the_main_module_of_the_program():
    ship_positions = module_computer_position_ship()
    count = 0
    module_pole_print()
    cycle_main_modul = True
    list_X = []     # - список координат убиенных кораблей
    list_O = []     # - список координат попаданий в молоко
    list_K = []     # - список координат вокруг корабля
    list_T = []     # - список координат отмечаемых на карте
    while cycle_main_modul:
        gemer_move = module_gamer_moves()
        ship_positions, list_X, list_O, list_K, list_T = module_pole_print(ship_positions, gemer_move, list_X, list_O, list_K, list_T)
        print(list_K)
        print(list_O)
        print(list_T)
        print(list_X)
        if ship_positions == []:
            cycle_main_modul = False
            print('Вы победили!!!')
        count += 1
    return True, count

# распечатка финального результата
def finally_print(count):
    print(f"Вами сыграно: {count} {grammar_module(count, 'игра')}")

# главный цикл перезапуска программы
def general_cycle_of_the_program():
    password, count_step = the_main_module_of_the_program()
    count = 1
    while password:
        cycle_word = input(f"""В этой игре Вы победили за {count_step} {grammar_module(count_step, 'попытка')}!
        Если Вы хотите продолжить нажмите ввод, если хотите выйти из игры введите любой знак:""")   
        if cycle_word != '':
            password = False
        else:
            password = the_main_module_of_the_program()
            count += 1
    finally_print(count)
    return ...

# модуль приветствия 
def start_program():  
    print(f'''
        Игра: Морской бой(класический: поле 10х10, корабли 1-4хпал. 2-3пал. 3-2хпал. 4-1пал) !
Комп расставляет корабли, Ваша задача их перебить, впритык корабли стоять не могут. 

Если Вы готовы нажмите ввод, если хотите выйти из игры введите любой знак.''')
    enter_word = input('')
    if enter_word != '':
        print('Всего хорошего!')
    else:
        general_cycle_of_the_program()

if __name__ == '__main__':
    start_program()