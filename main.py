import random
#1.Kamień    2.Papier     3.Nożyczki
player = input("wybierz 1.Kamień    2.Papier     3.Nożyczki")
bot = random.randint(1, 2, 3)

if player == 1 and bot == 1:
    print("bot wybrał Kamień")
    print("Remis")

if player == 1 and bot == 2:
    print("Bot wybrał papier")
    print("Przegrałeś")

if player == 1 and bot == 3:
    print("bot wybrał nożyczki")
    print("Wygrałeś")

if player == 2 and bot == 1:
    print("bot wybrał kamień")
    print("Wygrałeś")

if player == 3 and bot == 3:
    print("bot wybrał nożyczki")
    print("Remis")



if player == 2 and bot == 2:
    print("bot wybrał papier")
    print("Remis")

if player == 3 and bot == 3:
    print("bot wybrał nożyczki")
    print("Remis")