from time import sleep
import os
import platform
from threading import Thread

# Окончание добычи
end = False

# Создание предметов
not_created = "Не создано"
created = "Создано"

wood_pick = not_created
wood_axe = not_created
wood_shovel = not_created
stone_pick = not_created
stone_axe = not_created
stone_shovel = not_created

# Покупка предметов
not_purchased = "Не приобретено"
purchased = "Приобретено"

strange_mechanism = not_purchased
gloves = not_purchased
haste_potion = not_purchased
haste_potion_count = 4

# Время на добычу
wood_time = 2
stone_time = 2
dirt_time = 2

# Количество добычи
wood_stacks = 1
stone_stacks = 1
dirt_stacks = 1

# Ресурсы
wood = 0
stone = 0
dirt = 0
coins = 0

# Очистка консоли
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Покупка предметов
def shop_buy():
    clear_console()
    global coins
    global strange_mechanism
    global gloves
    global haste_potion
    global haste_potion_count
    global wood_time
    global stone_time
    global dirt_time
    print("Что вы хотите купить:\n"
          "[1] Странный механизм - 150 монет - Повышает скорость добычи всех ресурсов на 1", " [",  strange_mechanism, "]" , "\n"
          "[2] Строительные перчатки - 75 монет - Повышает скорость добычи всех ресурсов на 0.5", " [", gloves, "]", "\n"
          "[3] Зелье спешки (",haste_potion_count, "штуки на складе ) - 20 монет - Повышает скорость добычи всех ресурсов на 0.1", " [", haste_potion, "]", "\n"
          "[4] Обратно\n")
    buy = input("> ")

    if buy == "1" and strange_mechanism == "Не приобретено":
        print("Странный механизм - Стоимость 150 монет - Повышает скорость добычи всех ресурсов на 1\n"
              "Купить?\n"
              "[1] Да\n"
              "[2] Нет\n")
        a = input("> ")
        if a == "1" and coins >= 150:
            print("Приобретено")
            strange_mechanism = purchased
            wood_time -= 1
            stone_time -= 1
            dirt_time -= 1
            coins -= 150
            shop_buy()
            
        elif a == "1" and coins < 150:
            print("Не хватает монет")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_buy()

        else:
            shop_buy()
            
    elif buy == "2" and gloves == "Не приобретено":
        print("Строительные перчатки - Стоимость 75 монет - Повышает скорость добычи всех ресурсов на 0.5\n"
              "Купить?\n"
              "[1] Да\n"
              "[2] Нет\n")
        a = input("> ")
        if a == "1" and coins >= 75:
            print("Приобретено")
            gloves = purchased
            wood_time -= 0.5
            stone_time -= 0.5
            dirt_time -= 0.5
            coins -= 75
            shop_buy()
            
        elif a == "1" and coins < 75:
            print("Не хватает монет")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_buy()

        else:
            shop_buy()

    elif buy == "3" and haste_potion == "Не приобретено":
        print("Зелье спешки (",haste_potion_count, "штуки на складе ) - Стоимость 20 монет - Повышает скорость добычи всех ресурсов на 0.1\n"
              "Купить?\n"
              "[1] Да\n"
              "[2] Нет\n")
        a = input("> ")
        if a == "1" and coins >= 20:
            wood_time -= 0.1
            stone_time -= 0.1
            dirt_time -= 0.1
            coins -= 20
            haste_potion_count -= 1 
            if haste_potion_count == 0:
                haste_potion = purchased
            shop_buy()
        elif a == "1" and coins < 20:
            print("Не хватает монет")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_buy()

        else:
            shop_buy()

    elif buy == "4":
        start_point()

    else:
        print("Вы перешли на несуществующий раздел, либо предмет уже был приобретен")
        for i in range(2, 0, -1):
                print(i)
                sleep(1)
        shop_buy()
    
# Продажа предметов
def shop_sell():
    clear_console()
    global coins
    global wood
    global stone
    global dirt
    print("Текущее количество монет: ", coins, "\n"
          "Что вы хотите продать:\n"
          "[1] Дерево - 1 монета за 1 дерево", "                          [ Текущее количество дерева: ", wood,"]\n"
          "[2] Камень - 1 монета за 1 камень", "                          [ Текущее количество камня: ", stone,"]\n"
          "[3] Земля - 1 монета за 1 землю", "                            [ Текущее количество земли: ", dirt,"]\n"
          "[4] Обратно\n")
    sell = input("> ")

    if sell == "1":
        count = int(input("Сколько вы хотите продать: \n"
                      "> "))
        if count <= wood:
            coins += count
            wood -= count
            shop_sell()

        else:
            print("Введено значение, превышающее текущее количество ресурсов")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_sell()

    elif sell == "2":
        count = int(input("Сколько вы хотите продать: \n"
                      "> "))
        if count <= stone:
            coins += count
            stone -= count
            shop_sell()

        else:
            print("Введено значение, превышающее текущее количество ресурсов")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_sell()

    elif sell == "3":
        count = int(input("Сколько вы хотите продать: \n"
                      "> "))
        if count <= dirt:
            coins += count
            dirt -= count
            shop_sell()

        else:
            print("Введено значение, превышающее текущее количество ресурсов")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_sell()

    else:
        start_point()

# Магазин
def shop():
    a = input("Что вы хотите сделать:\n[1] Купить\n[2] Продать\n[3] Обратно\n> ")
    if a == "1":
        shop_buy()

    elif a == "2":
        shop_sell()
    else:
        start_point()

# Создание предметов
def craft():
    global wood
    global stone
    global dirt
    global wood_stacks
    global stone_stacks
    global dirt_stacks
    global wood_pick
    global wood_axe
    global wood_shovel
    global stone_pick
    global stone_axe
    global stone_shovel
    print("Что вы хотите создать:\n"
          "[1] Деревянная кирка - 14 дерева - Повышает количество добываемого камня на 1", "              [", wood_pick, "]" , "\n"
          "[2] Деревянный топор - 14 дерева - Повышает количество добываемого дерева на 1", "             [", wood_axe, "]" , "\n"
          "[3] Деревянная лопата - 14 дерева - Повышает количество добываемой земли на 1", "              [", wood_shovel, "]" , "\n"
          "[4] Каменная кирка - 14 камня и 14 дерева - Повышает количество добываемого камня на 1", "     [", stone_pick, "]" , "\n"
          "[5] Каменный топор - 14 камня и 14 дерева - Повышает количество добываемого дерева на 1", "    [", stone_axe, "]" , "\n"
          "[6] Каменная лопата - 14 камня и 14 дерева - Повышает количество добываемой земли на 1", "     [", stone_shovel, "]" , "\n"
          "[7] Выйти")
    crafting = input("> ")
    if crafting == "1" and wood_pick == "Не создано":
        print("Деревянная кирка\nСтоимость - 14 дерева\nПовышает количество добываемого камня на 1")
        b = input("Создать?\n[1] Да\n[2] Нет\n")
        if b == "1" and wood >= 14:
            wood -= 14
            stone_stacks += 1
            wood_pick = created
            craft()
        elif wood < 14:
            print("Не хватает дерева. Текущее количество =",wood)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
            
        else:
            craft()
            
    elif crafting == "2" and wood_axe == "Не создано":
        print("Деревянный топор\nСтоимость - 14 дерева\nПовышает количество добываемого дерева на 1")
        b = input("Создать?\n[1] Да\n[2] Нет\n")
        if b == "1" and wood >= 14:
            wood -= 14
            wood_stacks += 1
            wood_axe = created
            craft()
        elif wood < 14:
            print("Не хватает дерева. Текущее количество =",wood)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()
            
    elif crafting == "3" and wood_shovel == "Не создано":
        print("Деревянная лопата\nСтоимость - 14 дерева\nПовышает количество добываемой земли на 1")
        b = input("Создать?\n[1] Да\n[2] Нет\n")
        if b == "1" and wood >= 14:
            wood -= 14
            dirt_stacks += 1
            wood_shovel = created
            craft()
        elif wood < 14:
            print("Не хватает дерева. Текущее количество =",wood)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()

    elif crafting == "4" and stone_pick == "Не создано":
        print("Каменная кирка\nСтоимость - 14 камня и 14 дерева\nПовышает количество добываемого камня на 1")
        b = input("Создать?\n[1] Да\n[2] Нет\n")
        if b == "1" and stone >= 14 and wood >= 14:
            wood -= 14
            stone -= 14
            stone_stacks += 1
            stone_pick = created
            craft()
        elif wood < 14 or stone < 14:
            print("Не хватает дерева либо камня\nТекущее количество дерева =",wood, "\n", "Текущее количество камня =",stone)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()

    elif crafting == "5" and stone_axe == "Не создано":
        print("Каменный топор\nСтоимость - 14 камня и 14 дерева\nПовышает количество добываемого дерева на 1")
        b = input("Создать?\n[1] Да\n[2] Нет\n")
        if b == "1" and stone >= 14 and wood >= 14:
            wood -= 14
            stone -= 14
            wood_stacks += 1
            stone_axe = created
            craft()
        elif wood < 14 or stone < 14:
            print("Не хватает дерева либо камня\nТекущее количество дерева =",wood, "\n", "Текущее количество камня =",stone)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()

    elif crafting == "6" and stone_shovel == "Не создано":
        print("Каменная лопата\nСтоимость - 14 камня и 14 дерева\nПовышает количество добываемой земли на 1")
        b = input("Создать?\n[1] Да\n[2] Нет\n")
        if b == "1" and stone >= 14 and wood >= 14:
            wood -= 14
            stone -= 14
            dirt_stacks += 1
            stone_shovel = created
            craft()
        elif wood < 14 or stone < 14:
            print("Не хватает дерева либо камня\nТекущее количество дерева =",wood, "\n", "Текущее количество камня =",stone)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()
            
    elif crafting == "7":
        start_point()
        
    else:
        print("Вы перешли на несуществующий раздел, либо предмет уже был создан")

# Остановка добычи
def ending():
    global end
    input()
    end = True

# Добыча дерева
def wood_collect():
    global wood
    global wood_time
    global wood_stacks
    global wood_limit
    clear_console()
    listener = Thread(target=ending)
    listener.start()
    while not end:
        clear_console()
        print("Идет добыча дерева\n"
              "Количество добываемого:",wood_stacks, "каждые", wood_time, "секунды", "\n"
              "Добыто:", wood, "\n"
              "Нажмите любую кнопку, чтобы закончить добычу. После остановки пройдет", wood_time, "секунд, прежде чем цикл остановится")
        wood += wood_stacks
        sleep(wood_time)
    listener.join()
    resources()

# Добыча камня
def stone_collect():
    global stone
    global stone_time
    global stone_stacks
    global stone_limit
    clear_console()
    listener = Thread(target=ending)
    listener.start()
    while not end:
        clear_console()
        print("Идет добыча камня\n"
              "Количество добываемого:",stone_stacks, "каждые", stone_time, "секунды", "\n"
              "Добыто:", stone, "\n"
              "Нажмите любую кнопку, чтобы закончить добычу. После остановки пройдет", stone_time, "секунд, прежде чем цикл остановится")
        stone += stone_stacks
        sleep(stone_time)
    listener.join()
    resources()

# Добыча земли
def dirt_collect():
    global dirt
    global dirt_time
    global dirt_stacks
    global dirt_limit
    clear_console()
    listener = Thread(target=ending)
    listener.start()
    while not end:
        clear_console()
        print("Идет добыча земли\n"
              "Количество добываемого:",dirt_stacks, "каждые", dirt_time, "секунды", "\n"
              "Добыто:", dirt, "\n"
              "Нажмите любую кнопку, чтобы закончить добычу. После остановки пройдет", dirt_time, "секунд, прежде чем цикл остановится")
        dirt += dirt_stacks
        sleep(dirt_time)
    listener.join()
    resources()

# Добыча ресурсов
def resources():
    clear_console()
    global wood
    global end
    end = False
    print("Добыто:\n"
          "[1] Дерева:", wood,"\n"
          "[2] Камней:", stone,"\n"
          "[3] Земли:", dirt,"\n"
          "[4] Обратно")
    
    res = input("Какой ресурс вы хотите добыть:\n> ")
    
    if res == "1":
        wood_collect()

    elif res == "2":
        stone_collect()

    elif res == "3":
        dirt_collect()

    else:
        start_point()
        
# Меню выбора действия
def start_point():
    clear_console()
    start = input("Что вы хотите сделать?\n\n"
                  "[1] Добыть ресурсы\n"
                  "[2] Открыть магазин\n"
                  "[3] Создать предметы\n"
                  "[4] Статистика\n"
                  "[5] Выйти в главное меню\n> ")
    if start == "1":
        resources()
        
    elif start == "2":
        shop()
        
    elif start == "3":
        craft()

    elif start == "4":
        stats()
        
    else:
        mainmenu()

# Сохранить игру
def saving():
    a = input("Вы хотите сохранить игру?\n\n[1] Да\n[2] Нет\n")
    if a == "1":
        with open("save.txt", "w") as savefile:
            savefile.write("wood: \n")
            savefile.write(str(wood))
            
            savefile.write("\n\n")
            savefile.write("stone: \n")
            savefile.write(str(stone))
            
            savefile.write("\n\n")
            savefile.write("dirt: \n")
            savefile.write(str(dirt))
            
            savefile.write("\n\n")
            savefile.write("wood_stacks: \n")
            savefile.write(str(wood_stacks))
            
            savefile.write("\n\n")
            savefile.write("stone_stacks: \n")
            savefile.write(str(stone_stacks))
            
            savefile.write("\n\n")
            savefile.write("dirt_stacks: \n")
            savefile.write(str(dirt_stacks))
            
            savefile.write("\n\n")
            savefile.write("wood_time: \n")
            savefile.write(str(dirt_stacks))
            
            savefile.write("\n\n")
            savefile.write("stone_time: \n")
            savefile.write(str(dirt_stacks))
            
            savefile.write("\n\n")
            savefile.write("dirt_time: \n")
            savefile.write(str(dirt_stacks))

            savefile.write("\n\n")
            savefile.write("wood_pick: \n")
            savefile.write(str(wood_pick))

            savefile.write("\n\n")
            savefile.write("wood_axe: \n")
            savefile.write(str(wood_axe))

            savefile.write("\n\n")
            savefile.write("wood_shovel: \n")
            savefile.write(str(wood_shovel))

            savefile.write("\n\n")
            savefile.write("stone_pick: \n")
            savefile.write(str(stone_pick))

            savefile.write("\n\n")
            savefile.write("stone_axe: \n")
            savefile.write(str(stone_axe))

            savefile.write("\n\n")
            savefile.write("stone_shovel: \n")
            savefile.write(str(stone_shovel))

            savefile.write("\n\n")
            savefile.write("strange_mechanism: \n")
            savefile.write(str(strange_mechanism))

            savefile.write("\n\n")
            savefile.write("gloves: \n")
            savefile.write(str(gloves))

            savefile.write("\n\n")
            savefile.write("haste_potion: \n")
            savefile.write(str(haste_potion))

            savefile.write("\n\n")
            savefile.write("haste_potion_count: \n")
            savefile.write(str(haste_potion_count))

            savefile.write("\n\n")
            savefile.write("coins: \n")
            savefile.write(str(coins))
            
        print("Игра сохранена успешно")
        for i in range(2, 0, -1):
            print(i)
            sleep(1)
        mainmenu()
    else:
        mainmenu()

# Загрузить игру
def loading():
    global wood
    global stone
    global dirt
    global wood_stacks
    global stone_stacks
    global dirt_stacks
    global wood_time
    global stone_time
    global dirt_time
    global wood_pick
    global wood_axe
    global wood_shovel
    global stone_pick
    global stone_axe
    global stone_shovel
    global strange_mechanism
    global gloves
    global haste_potion
    global haste_potion_count
    global coins
    with open("save.txt", "r") as loadfile:
        a = loadfile.readlines()
        wood = int(a[1].rstrip("\n"))
        stone = int(a[4].rstrip("\n"))
        dirt = int(a[7].rstrip("\n"))
        wood_stacks = int(a[10].rstrip("\n"))
        stone_stacks = int(a[13].rstrip("\n"))
        dirt_stacks = int(a[16].rstrip("\n"))
        wood_time = float(a[19].rstrip("\n"))
        stone_time = float(a[22].rstrip("\n"))
        dirt_time = float(a[25].rstrip("\n"))
        wood_pick = a[28].rstrip("\n")
        wood_axe = a[31].rstrip("\n")
        wood_shovel = a[34].rstrip("\n")
        stone_pick = a[37].rstrip("\n")
        stone_axe = a[40].rstrip("\n")
        stone_shovel = a[43].rstrip("\n")
        strange_mechanism = a[46].rstrip("\n")
        gloves = a[49].rstrip("\n")
        haste_potion = a[52].rstrip("\n")
        haste_potion_count = int(a[55].rstrip("\n"))
        coins = int(a[58].rstrip("\n"))
    print("Игра загружена успешно")
    for i in range(2, 0, -1):
        print(i)
        sleep(1)
    mainmenu()

# Статистика
def stats():
    clear_console()
    print("Статистика:\n"
          "Количество дерева =",wood,"\n"
          "Количество камня =",stone,"\n"
          "Количество земли =",dirt,"\n"
          "Количество монет =",coins,"\n\n"
          "Количество добываемого дерева =",wood_stacks,"\n"
          "Количество добываемого камня =",stone_stacks,"\n"
          "Количество добываемого земли =",dirt_stacks,"\n\n"
          "Время добычи дерева =",wood_time,"\n"
          "Время добычи камня =",stone_time,"\n"
          "Время добычи земли =",dirt_time,"\n\n"
          "Странный механизм =",strange_mechanism,"\n"
          "Строительные перчатки =",gloves,"\n"
          "Зелье спешки =",haste_potion, haste_potion_count,"на складе\n\n"
          "Деревянная кирка =",wood_pick,"\n"
          "Деревянный топор =",wood_axe,"\n"
          "Деревянная лопата =",wood_shovel,"\n"
          "Каменная кирка =",stone_pick,"\n"
          "Каменный топор =",stone_axe,"\n"
          "Каменная лопата =",stone_shovel,"\n"
          "[1] Вернуться")
    stat = input("> ")
    start_point()

# Главное меню
def mainmenu():
    clear_console()
    menu = input("Главное меню\n\n"
                  "[1] Начать игру\n"
                  "[2] Сохранить игру\n"
                  "[3] Загрузить игру\n"
                  "[4] Выход\n> ")
    if menu == "1":
        start_point()
        
    elif menu == "2":
        saving()
        
    elif menu == "3":
        loading()
        
    else:
        return 0

mainmenu()
