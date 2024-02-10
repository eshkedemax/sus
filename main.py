import random
health = 75
score = 0

while True:
      print("вы попали в открытое море")
      print("что вы делаете?")
      print("1. грести к острову")
      print("2.принять свою смерть")
      choice = input()
      if choice == "1":
            print("вы видите бункер")
            print("но рядом с его дверью лежит карта доступа от двери")
            print("1. открыть дверь")
            print("2.попытаться уплыть с острова")
            inner_choise = input("введите номер выбора")
            if inner_choise == "1":
                  print("вы видите сейф")
                  print("отгадайте код")
                  num = random.randint(1,100)
                  while True:
                        player_num = int(input())
                        if num>player_num:
                              print("похоже число больше")
                        elif num<player_num:
                              print("похоже число меньше")
                        elif num==player_num:
                            print("код введён")
                            break
                  print("сейф открылся")
                  print("в нём летающий шар")
                  print("1.дотронуться до шара")
                  print("2.попытаться выжить в бункере ")
                  s_choice = input()
                  if s_choice == "1":
                        print("перед вами появилось оружие ")
                        print("'это оружие похоже на гарпун")
                        print("благодоря гарпуну вы забираетесь на гору")
                        print("и видите летающею акулу")
                        baby_shark = 50
                        boba = 1
                        while baby_shark>0:
                              print("1.ударить")
                              print("2.гарпун")
                              a_choice = input()
                              if a_choice == "1":
                                    print("вы нанесли акуле 20hp")
                                    baby_shark -= 20
                                    print("но акула вам тоже нанесла урон")
                                    health -= 25
                              elif a_choice == "2" and boba !=2:
                                    print("при помощи гарпуна вы нанесли акуле 10hp")
                                    baby_shark -= 10
                                    print("акула не может до вас долететь")
                                    boba = random.randint(1,2)
                                    if boba == 2:
                                          print("гарпун застрял в акуле,больше вы не можете её отаковать гарпуном")
                        print("вы победили акулу")
                        print("вы оторвали кусок от акулы и пожарили его")
                        print("и съели его")
                        print("КОНЕЦ!")
                        break

