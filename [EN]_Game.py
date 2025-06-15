from time import sleep
import os
import platform
from threading import Thread

# Окончание добычи
end = False

# Создание предметов
not_created = "Not created"
created = "Created"

wood_pick = not_created
wood_axe = not_created
wood_shovel = not_created
stone_pick = not_created
stone_axe = not_created
stone_shovel = not_created

# Покупка предметов
not_purchased = "Not purchased"
purchased = "Purchased"

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
    print("What do you want to buy:\n"
          "[1] Strange mechanism - 150 coins - Increases the speed of mining all resources by 1", " [",  strange_mechanism, "]" , "\n"
          "[2] Construction gloves - 75 coins - Increases the speed of mining all resources by 0.5", " [", gloves, "]", "\n"
          "[3] Haste potion (",haste_potion_count, "pieces in stock ) - 20 coins - Increases the speed of mining all resources by 0.1", " [", haste_potion, "]", "\n"
          "[4] Return\n")
    buy = input("> ")

    if buy == "1" and strange_mechanism == "Не приобретено":
        print("Strange mechanism - Costs 150 coins - Increases the speed of mining all resources by 1\n"
              "Purchase?\n"
              "[1] Yes\n"
              "[2] No\n")
        a = input("> ")
        if a == "1" and coins >= 150:
            print("Purchased")
            strange_mechanism = purchased
            wood_time -= 1
            stone_time -= 1
            dirt_time -= 1
            coins -= 150
            shop_buy()
            
        elif a == "1" and coins < 150:
            print("Not enough coins")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_buy()

        else:
            shop_buy()
            
    elif buy == "2" and gloves == "Not purchased":
        print("Construction gloves - Costs 75 coins - Increases the speed of mining all resources by 0.5\n"
              "Purchase?\n"
              "[1] Yes\n"
              "[2] No\n")
        a = input("> ")
        if a == "1" and coins >= 75:
            print("Purchased")
            gloves = purchased
            wood_time -= 0.5
            stone_time -= 0.5
            dirt_time -= 0.5
            coins -= 75
            shop_buy()
            
        elif a == "1" and coins < 75:
            print("Not enough coins")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_buy()

        else:
            shop_buy()

    elif buy == "3" and haste_potion == "Not purchased":
        print("Haste potion (",haste_potion_count, "pieces in stock ) - Costs 20 coins - Increases the speed of mining all resources by 0.1\n"
              "Purchase?\n"
              "[1] Yes\n"
              "[2] No\n")
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
            print("Not enough coins")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_buy()

        else:
            shop_buy()

    elif buy == "4":
        start_point()

    else:
        print("You have navigated to a non-existent section, or the item has already been purchased")
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
    print("Coins: ", coins, "\n"
          "What do you want to sell:\n"
          "[1] Wood - 1 coin for 1 wood", "                               [ Wood: ",wood,"]\n"
          "[2] Stone - 1 coin for 1 stone", "                             [ Stones: ",stone,"]\n"
          "[3] Dirt - 1 coin for 1 dirt", "                               [ Dirt: ",dirt,"]\n"
          "[4] Return\n")
    sell = input("> ")

    if sell == "1":
        count = int(input("How much: \n"
                      "> "))
        if count <= wood:
            coins += count
            wood -= count
            shop_sell()

        else:
            print("A value has been entered that exceeds the current amount of resources")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_sell()

    elif sell == "2":
        count = int(input("How much: \n"
                      "> "))
        if count <= stone:
            coins += count
            stone -= count
            shop_sell()

        else:
            print("A value has been entered that exceeds the current amount of resources")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_sell()

    elif sell == "3":
        count = int(input("How much: \n"
                      "> "))
        if count <= dirt:
            coins += count
            dirt -= count
            shop_sell()

        else:
            print("A value has been entered that exceeds the current amount of resources")
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            shop_sell()

    else:
        start_point()

# Магазин
def shop():
    a = input("What do you want to do:\n[1] Buy\n[2] Sell\n[3] Return\n> ")
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
    print("What do you want to craft:\n"
          "[1] Wooden Pickaxe - 14 Wood - Increases the amount of stone mined by 1", "                    [", wood_pick, "]" , "\n"
          "[2] Wooden Axe - 14 Wood - Increases the amount of wood mined by 1", "                         [", wood_axe, "]" , "\n"
          "[3] Wooden Shovel - 14 Wood - Increases the amount of earth mined by 1", "                     [", wood_shovel, "]" , "\n"
          "[4] Stone Pickaxe - 14 Stone and 14 Wood - Increases the amount of stone mined by 1", "        [", stone_pick, "]" , "\n"
          "[5] Stone Axe - 14 Stone and 14 Wood - Increases the amount of wood mined by 1", "             [", stone_axe, "]" , "\n"
          "[6] Stone Shovel - 14 Stone and 14 Wood - Increases the amount of earth mined by 1", "         [", stone_shovel, "]" , "\n"
          "[7] Return")
    crafting = input("> ")
    if crafting == "1" and wood_pick == "Not created":
        print("Wooden Pickaxe\nCost - 14 wood\nIncreases the amount of stone mined by 1")
        b = input("Create?\n[1] Yes\n[2] No\n")
        if b == "1" and wood >= 14:
            wood -= 14
            stone_stacks += 1
            wood_pick = created
            craft()
        elif wood < 14:
            print("Not enough wood. Current quantity =",wood)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
            
        else:
            craft()
            
    elif crafting == "2" and wood_axe == "Not created":
        print("Wooden Axe\nCost - 14 wood\nIncreases the amount of wood mined by 1")
        b = input("Create?\n[1] Yes\n[2] No\n")
        if b == "1" and wood >= 14:
            wood -= 14
            wood_stacks += 1
            wood_axe = created
            craft()
        elif wood < 14:
            print("Not enough wood. Current quantity =",wood)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()
            
    elif crafting == "3" and wood_shovel == "Not created":
        print("Wooden Shovel\nCost - 14 wood\nIncreases the amount of land mined by 1")
        b = input("Create?\n[1] Yes\n[2] No\n")
        if b == "1" and wood >= 14:
            wood -= 14
            dirt_stacks += 1
            wood_shovel = created
            craft()
        elif wood < 14:
            print("Not enough wood. Current quantity =",wood)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()

    elif crafting == "4" and stone_pick == "Not created":
        print("Stone Pickaxe\nCost - 14 stone and 14 wood\nIncreases the amount of stone mined by 1")
        b = input("Create?\n[1] Yes\n[2] No\n")
        if b == "1" and stone >= 14 and wood >= 14:
            wood -= 14
            stone -= 14
            stone_stacks += 1
            stone_pick = created
            craft()
        elif wood < 14 or stone < 14:
            print("Not enough wood or stone\nCurrent amount of wood =",wood, "\n", "Current amount of stone =",stone)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()

    elif crafting == "5" and stone_axe == "Not created":
        print("Stone Axe\nCost - 14 stone and 14 wood\nIncreases the amount of wood mined by 1")
        b = input("Create?\n[1] Yes\n[2] No\n")
        if b == "1" and stone >= 14 and wood >= 14:
            wood -= 14
            stone -= 14
            wood_stacks += 1
            stone_axe = created
            craft()
        elif wood < 14 or stone < 14:
            print("Not enough wood or stone\nCurrent amount of wood =",wood, "\n", "Current amount of stone =",stone)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()

    elif crafting == "6" and stone_shovel == "Not created":
        print("Stone Shovel\nCost - 14 stone and 14 wood\nIncreases the amount of earth mined by 1")
        b = input("Create?\n[1] Yes\n[2] No\n")
        if b == "1" and stone >= 14 and wood >= 14:
            wood -= 14
            stone -= 14
            dirt_stacks += 1
            stone_shovel = created
            craft()
        elif wood < 14 or stone < 14:
            print("Not enough wood or stone\nCurrent amount of wood =",wood, "\n", "Current amount of stone =",stone)
            for i in range(2, 0, -1):
                print(i)
                sleep(1)
            craft()
           
        else:
            craft()
            
    elif crafting == "7":
        start_point()
        
    else:
        print("You have navigated to a non-existent section, or the item has already been created")

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
        print("Wood is being chopped\n"
              "Amount mined:",wood_stacks, "every", wood_time, "seconds", "\n"
              "Chopped:", wood, "\n"
              "Press any button to stop mining. Once stopped, it will take", wood_time, "seconds before the cycle stops")
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
        print("Stone mining in progress\n"
              "Amount mined:",stone_stacks, "every", stone_time, "seconds", "\n"
              "Mined:", stone, "\n"
              "Press any button to stop mining. Once stopped, it will take", stone_time, "seconds before the cycle stops")
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
        print("The land is being mined\n"
              "Amount mined:",dirt_stacks, "every", dirt_time, "seconds", "\n"
              "Minced:", dirt, "\n"
              "Press any button to stop mining. Once stopped, it will take", dirt_time, "seconds before the cycle stops")
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
    print("Mined:\n"
          "[1] Wood:", wood,"\n"
          "[2] Stone:", stone,"\n"
          "[3] Dirt:", dirt,"\n"
          "[4] Return")
    
    res = input("What resource do you want to mine:\n> ")
    
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
    start = input("What do you want to do?\n\n"
                  "[1] Get resources\n"
                  "[2] Open shop\n"
                  "[3] Create items\n"
                  "[4] Statistics\n"
                  "[5] Exit to main menu\n> ")
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
    a = input("Do you want to save?\n\n[1] Yes\n[2] No\n")
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
            
        print("Game saved successfully")
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
    print("Game loaded successfully")
    for i in range(2, 0, -1):
        print(i)
        sleep(1)
    mainmenu()

# Статистика
def stats():
    clear_console()
    print("Stats:\n"
          "Amount of wood =",wood,"\n"
          "Amount of stone =",stone,"\n"
          "Amount of dirt =",dirt,"\n"
          "Amount of coins =",coins,"\n\n"
          "Amount of mined wood =",wood_stacks,"\n"
          "Amount of mined stone =",stone_stacks,"\n"
          "Amount of mined dirt =",dirt_stacks,"\n\n"
          "Wood mining time =",wood_time,"\n"
          "Stone mining time =",stone_time,"\n"
          "Dirt mining time =",dirt_time,"\n\n"
          "Strange mechanism =",strange_mechanism,"\n"
          "Construction gloves =",gloves,"\n"
          "Haste potion =",haste_potion, haste_potion_count,"in stock\n\n"
          "Wooden Pickaxe =",wood_pick,"\n"
          "Wooden Axe =",wood_axe,"\n"
          "Wooden Shovel =",wood_shovel,"\n"
          "Stone Pickaxe =",stone_pick,"\n"
          "Stone Axe =",stone_axe,"\n"
          "Stone Shovel =",stone_shovel,"\n"
          "[1] Return")
    stat = input("> ")
    start_point()

# Главное меню
def mainmenu():
    clear_console()
    menu = input("Main Menu\n\n"
                 "[1] Start Game\n"
                 "[2] Save Game\n"
                 "[3] Load Game\n"
                 "[4] Exit\n> ")
    if menu == "1":
        start_point()
        
    elif menu == "2":
        saving()
        
    elif menu == "3":
        loading()
        
    else:
        return 0

mainmenu()
