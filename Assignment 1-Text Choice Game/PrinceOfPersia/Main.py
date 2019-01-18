'''Name- Rajeshree Kale
    Assignment 1 - Text Choice game'''


import time
import csv
import pandas as pd

######Change utility_belt from ALL print Statements

player_name=input('Enter your name- ')
utility_belt={}
statistics={}
health: int = 45



def belt_updator(dictonary,item,type):
    ''' To upgrade the belt belt_udator function is used,
        the input for the functions are
        dictonary - dictonray in which data is stored
        item - the discription of actual item
        type - the type of item for eg. Sword,points,coins
    '''

    dictonary[type] = item

def ip_selector(selectionlist):

    ''' The function will be used to accept correct input and
        respectiev numberreturn
    '''

    choice = input(player_name + " Select your choice" "\n")

    if choice in selectionlist:
        return choice
    else:
        print("Entered an Invalid input. Last Chance to enter correct input")
        choice = input(player_name + " Select your choice" "\n")
        if choice in selectionlist:
            return choice
        else:
            print("Game Terminating")
            raise SystemExit

    '''elif print("\n Please select a correct option"):
        choice=input('Please select correct option otherwise the game will terminate')
        return choice'''


'''def stat_update():
    with open('PrinceOfPersia.csv', 'w') as file:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(file, stat.keys(), stat.values())
        w.writeheader()
        w.writerow(stat)'''

def level_upgrade(available_coins):
    ''' If player wants to skip the level level_upgrade function is called
        input parameter is number of coins player has
        the return statement shows the eligibility of the player
        1- eligible
        0- not eligible '''

    if available_coins > 150:
        return 1
    else:
        return 0


def transitionValidator(temp_choice):

    '''This function will be used to verify whether user really wants to exit the room or not'''


    if temp_choice == 'Y' or temp_choice == 'y':
        print('You will enter the next level')
        return 1
    elif temp_choice == 'n' or temp_choice == 'N':
        print('You have selected to return to the previous level, THE PRINCE IS RETURNING')
        return 0
    elif (temp_choice != 'Y' and temp_choice != 'y' and temp_choice != 'N' and temp_choice != 'n'):
            temp_choice = input('You need to input correct letter to proceed to next level\n'
                                'Please select the correct input')


def intro():
    '''The intro part of game will displayed at the beginning'''

    print("WELCOME " + player_name + " TO THE “PRINCE OF PERSIA: SANDS OF TIME\n”"
                                     "In the holy city of Alamut resides the Sands of Time, which gives mortals the power\n"
                                     "to turn back time. After leading an attack on the city, Dastan (The Devil), the adopted\n "
                                     "son of Persias king, acquires a dagger that gives the one who holds it access to the Sands.\n "
                                     "The Prince needs to traverse through 5 rooms to protect the ancient treasure from\n"
                                     "dark forces and unmask the kings assassin by killing Dastan!\n")
    #name = input('Select your name')

def update_health(health,pellet):

    '''To change the health of player this function takes input as current health and health bonus
        updated health will be returned
    '''
    if health < 100:
        health += pellet
        if health>100:
            health=100

    else:health=100
    return health


def got_hit(health, hitcount):

    '''if player gets hit the function will be used to reduce the health of player according to the hitcount
        the inputs are given as - health of player and hitcount
        the function return the updated health
    '''
    if health<hitcount:
        raise SystemExit

    else:
        health-=hitcount
        return health

def update_coins(utility_belt, num):

    '''when the player collects any coins those coins will be added to utility belt
        update_coin(dictonary name , number of received coins)

        the function returns the updated count of coins
    '''

    oldCoin_count=utility_belt['coins']
    newCoin_num =oldCoin_count + num
    belt_updator(utility_belt,newCoin_num,'coins')

    pass


def update_points(utility_belt, points,upgrade):

    '''when the player clears any stage he'll receive some points accodingly and utility belt
            will be updated update_points(dictonary name , number of received points, updgrade/degrade)
            if player is on correct path points will be added otherwise points will be deducted from
            total
            the function stores the updated count of points'''

    if upgrade:
        previousPoints = utility_belt['Points']
        newPoints = previousPoints + points
        belt_updator(utility_belt,newPoints,'Points')

    else:
        previousPoints = utility_belt['Points']
        newPoints= previousPoints- points
        if newPoints<0:
            newPoints=0
        belt_updator(utility_belt,newPoints,'Points')


def First_room():
    print("Welcome to the GREAT HALL..... of the Castle of Time\n")
    print("AN EPIC SOLO CAMPAIGN")
    time.sleep(1);

    print("Hello " + player_name + " You have entered The Great Hall!\n"
                                   " In this room, you have to find a thing hidden inside the room that will help you fight and defend\n"
                                   "the treasure chest is filled with weapons and armor which you can collect to improve your character")
    print("\nDecide your next move carefully and Please select the options from the following list -")
    print(
        "1.Pick a Shield and gear for the mission\n2.Collect gold coins to buy armor and weaponry \n3.Gain 50 health points and save it for your latter half"
        "\n4.Master the elements by picking an Axe to kill the Devil in the upcoming rooms\n"
        "5.Find a castle map and explore the hidden passageways, structures and temples")

    selectionlist = ['1', '2', '3', '4', '5']
    choice = ip_selector(selectionlist)
    time.sleep(1)
    # print('choice from begin'+ choice)

    if choice == '1':
        print("Congratulations! You have picked the Shield. You can now move to your next room")
        type,item = 'Armor','Shield'
        belt_updator(utility_belt,item,type)
        #print("Your Updated utility belt", utility_belt)
        type, item = 'Weapon', 'Axe'
        print("Ohh you received a complimentary weapon")
        belt_updator(utility_belt, item, type)
        #print("Your Updated utility belt", utility_belt)

        points = 20
        update_points(utility_belt, points,1)
        print("Your utility_belt is updated", utility_belt)

    elif choice == '2':
        print("Hurray! You gain 100 gold coins. You can now buy weapons for your mission")
        num = 100
        update_coins(utility_belt,num)
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)

    elif choice == '3':
        print("Health is- " + str(health))
        print("Tada! You gain health to survive for the mission")
        local_health =update_health(health ,50)
        print("Your health is" + str(local_health))

        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)



    elif choice == '4':
        print("Congratulations! You have picked the Axe. You can now gear up for the fight.")
        type, item = 'Weapon', 'Axe'
        belt_updator(utility_belt, item, type)
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)


    elif choice == '5':
        print("Unleash the beauty of the Castle by using the Map!")
        type, item = 'Map', 'Castle Map'
        belt_updator(utility_belt, item, type)
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)

    print("Nice move there " + player_name)
    print("Your health is- ",str(health))
    temp_choice = input(
        "Would you like to go to the next room or revisit the great hall again \nPlease type " """Y""" " to go to next room or type ""N"""
        "to revisit the great hall again ")

    transition= transitionValidator(temp_choice)
    time.sleep(5)
    player_points=utility_belt['Points']
    level=1
    belt_updator(statistics, player_points, level)

    if transition:
        second_room()
    else:
        First_room()


def second_room():
    print('Welcome to Level 2')
    print('Hey! '+player_name+' Congratulations! You have successfully entered the Dungeon!\n'
          'In this room, you have to search for the “MAGIC POUCH.”\n'
          'You get an entry to the next room if you have the Magic Pouch.')
    time.sleep(1)
    print(
        "1.To gain a Magic Pouch either you can hunt down the monster or you can lose your 20 HP and go to the next room\n"
        "2.Open the door on your left \n"
        "3.Discover a variety of environments\n"
        "4.Be friends with the Devil\n"
        "5.Break the potCollect gold coins to buy armor and weaponry")

    selectionlist = ['1', '2', '3', '4', '5']
    choice = ip_selector(selectionlist)
    time.sleep(1)

    if choice == '1':
        dung_choice=input(
            "if you want to kill the monster then type " """1""" " to kill or to dodge and escape type ""2"" but doing so you will lose 20 HP Select your move-")
        if dung_choice=='1':
            Collected_weapon= utility_belt['Weapon']
            if Collected_weapon =='':
                print("Cannot kill the monster")
                print("You have one more option to choose wisely")
                second_room()
            else:
                print("Congratulations! You killed the Monster!")
                time.sleep(1)
                print("ohh look the monster dropped the magic pouch")

                type, item = 'Pouch', 'Magic Pouch'
                belt_updator(utility_belt, item, type)
                points = 20
                update_points(utility_belt, points, 1)

                print("Your Updated utility belt", utility_belt)

        #code is not working update the fuction -20 is not working
        else:
            print("Ohh! You saved yourself from the troll but unfortunately you lost 20 HP")
            time.sleep(1)
            levelTwo_Health= got_hit(health,20)
            print("Your health is- " + str(levelTwo_Health))

    elif choice == '2':
        print("\nOhh sorry the room was empty.")
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)

    elif choice == '3':
        print("\nExplore the beauty of the Castle")
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)

    elif choice == '4':
        print("\nCongratulation! You just got a new friend.")
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)

    elif choice == '5':
        print("\nHurray! You gain 100 gold coins. You can now buy weapons for your mission")
        num = 100
        update_coins(utility_belt, num)
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)

    print("Nice move there " + player_name)
    print("You are out of the dungeons")
    print("Your health is- ", str(health))
    time.sleep(1)
    player_points = utility_belt['Points']
    level = 2
    belt_updator(statistics,player_points,level)

    Third_room()

    #accepting yes or type input
    #temp_choice = input(
    #   'Would you like to go to the next room or revisit the great hall again \nPlease type ' '''Y''' ' to go to next room or type ''N'''
    #  'to revisit the great hall again ')





def Third_room():


    print('Welcome to the Gardens of Castle of Time\n')

    time.sleep(5);

    print('Hello ' + player_name + ' You have entered The Garden of Puzzles!\n'
                                   ' In this level you have to “SOLVE THE PUZZLE” to exit the room.\n '
                                   'You get an entry to the next room only by solving the Puzzle.\n'
                                   'Either you win or you lose the opportunity to gain the Treasure Chest.\n '
                                   'CAN YOU CRACK THIS CHALLENGE?\n')

    print('\nDecide your next move carefully and Please select the options from the following list -')
    print(
        '1.Solve the Puzzle in the garden area and get an entry in the next room\n'
        '2.Collect roses for the princess \n'
        '3.Collect Magic Stones\n'
        '4.Break the Vase!\n'
        '5.Directly gain Access to the next room by paying 200 coins\n')
    selectionlist = ['1', '2', '3', '4', '5']
    choice = ip_selector(selectionlist)
    # print('choice from begin'+ choice)
    time.sleep(1)
    if choice == '1':
        print('You have selected to solve the puzzle\n')
        print('Please select the correct order of words\n You have the following Phrase\n Phrase - _an_ O_ _ime')

        print(
            '1.G,G,P,Y\n'
            '2.Y,S,G,L \n'
            '3.S,D,F,T\n')

        #puzzle solver

        selectionlist = ['1', '2', '3']
        choice = ip_selector(selectionlist)

        if(choice=='3'):
            print('Congratulation! You successfully solved the puzzle!\n')
            points = 20
            update_points(utility_belt, points, 1)
            print("Your utility_belt is updated", utility_belt)

        else:
            print("Please solve the puzzle correctly")
            Third_room()

    elif choice == '2':
        print('Tada! You successfully collected 10 roses')
        type, item = 'Flower', 'Roses'
        belt_updator(utility_belt, item, type)
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)



    elif choice == '3':
        print('Congratulations! The collection of Magic stones gives you the immense invisibility power! Have fun')
        time.sleep(3)
        print("ohh snap the ugly creature snapped the")
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)

    elif choice == '4':
        print('Surprise! On breaking the vase you gain 100 gold points!')
        num = 100
        update_coins(utility_belt, num)
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)


    elif choice == '5':
        available_coins=utility_belt['coins']
        if level_upgrade(available_coins):
                print('Hurray! You gained access to Level 4')
                points = 15
                update_points(utility_belt, points, 1)
                print("Your utility_belt is updated", utility_belt)
                Fourth_room()

        else:
            print("You do not have enough coins to skip this room you will be re-entering the room")
            Third_room()
            #give five points here-Done

    print("Your health is- ", str(health))
    player_points = utility_belt['Points']
    level = 3
    belt_updator(statistics, player_points,level )
    Fourth_room()


def Fourth_room():
    print('\nCongratulations! You have successfully entered Level 4!\n')

    time.sleep(1);

    print('Greetings ' + player_name + ' You have entered The Portal!\n'
                                       'In this room, you need to find the water sword which you will need to kill Dastan in the next room.\n'
                                       'Either you win or you lose the opportunity to gain the Treasure Chest.\n '
                                       '"FIND & GAIN" \nYou have 5 options to choose from the following:')

    print('\nDecide your next move carefully and Please select the options from the following list -')
    print(
        '1.Find the water sword to help you in the journey of vengeance\n'
        '2.Find the key to unlock the treasure chest\n'
        '3.Fight the Garden Monster and win cold coins\n'
        '4.Give a rose to the princess and gain 50 health points\n'
        '5.Use key to enter the next Room')

    selectionlist = ['1', '2', '3', '4', '5']
    choice = ip_selector(selectionlist)
    # print('choice from begin'+ choice)


    if choice == '1':
        print('Congratulations! You have gained the sword. This sword will help you to fight with Dastan(The Devil)')
        type, item = 'Weapon', 'Water Sword'
        belt_updator(utility_belt, item, type)
        points = 20
        update_points(utility_belt, points, 1)
        print("Your utility_belt is updated", utility_belt)



    elif choice == '2':
        print('Congratulations! You now found a key under the vase')

        type, item = 'Key', 'Key of Time'
        belt_updator(utility_belt, item, type)
        points = 20
        update_points(utility_belt, points, 1)
        print("Your utility_belt is updated", utility_belt)

    elif choice == '3':
        print('Hurray! you just won 3 pouches of 25 gold coins but you lost 15 HP while fighting the monster')
        coin = 25
        num =3*coin
        update_coins(utility_belt, num)
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)
        levelfour_Health = got_hit(health, 15)
        print('Your health is- ' + str(levelfour_Health))

    elif choice == '4':
        print('Congratulations! You just won 50 health points which will help you in the journey of vengeance')
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated", utility_belt)
        local_health = update_health(health, 50)
        print('Your health is' + str(local_health))

    elif choice == '5':
        print('Remember, you can use the key only to once! Use it wisely')

    print("Your health is- ", str(health))

    player_points = utility_belt['Points']
    level = 4
    belt_updator(statistics, player_points, level)

    Five_room()


    '''temp_choice = input(
    "Would you like to go to the next room or revisit the previous room again \nPlease type " """Y""" " to go to next room or type ""N"""
    "to revisit the previous room again ")

    transition = transitionValidator(temp_choice)

    

    time.sleep(1)
    if transition:
      Five_room()
    else:
      Fourth_room()'''

def Five_room():
    print('Welcome to the Chambers of Time\n')

    time.sleep(1);

    print('Hello ' + player_name + ' This is the final room and your last chance to win the game.\n' 
                                   'In this room you have to kill the Dastan using the water sword!\n'
                                   'which will help you win the treasure chest.\n'
                                   'Either you win or you lose the opportunity to gain the Treasure Chest.\n'
                                   )

    print('Decide your next move carefully and Please select the options from the following list -')
    print(
        '1.Kill Dastan (The Devil) using the water sword and gain the treasure chest\n'
        '2.Use your skills and dodge the Devil\n'
        '3.Go to room 4 and get the keys to unlock the treasure chest\n'
        '4."Wield" over 100 pieces of armor and weaponry!\n'
        '5.Exit the game')

    selectionlist = ['1', '2', '3', '4', '5']
    choice = ip_selector(selectionlist)
    # print('choice from begin'+ choice)

    if choice == '1':
        Collected_weapon = utility_belt['Weapon']
        if Collected_weapon == 'Water Sword':
            print('You killed the monster')
            print('Congratulations! You have successfully won the treasure chest!')

            '''Collected_key = utility_belt['Key']
            if Collected_key == '':
                print('You cannot open the chest because you dont have the key but you can go \nto the previous room to collect the key')
                Fourth_room()

            elif Collected_key =='Key of Time':
               '''
            print("You have opened the treasure chest and you have the sands of time")
            print("Now you can reverse back the time and change your fate.")
            points = 20
            update_points(utility_belt, points, 1)
            print("Your utility_belt is updated", utility_belt)

#            print("Utility Belt",utility_belt)
            print("Health-",str(health))
            print("Game Over")

        else:
            print("The devil was so powerfull you didn't picked the water sword in level 4 so you died")
            print("Utility Belt", utility_belt)
            print("Health-", str(health))
            print("Game Over")


    elif choice == '2':
        print("Tada! You just tricked one of your obstacle\n")
        num = 30
        update_coins(utility_belt, num)
        print('You received 30 coins')
        points = 10
        update_points(utility_belt, points, 0)
        print("Health-", str(health))
        print("Your utility_belt is updated", utility_belt)
        print("You failed to change your fate. The devil regained his powers.\nGame Over")

    elif choice == '3':
        print("One more chance to win the treasure chest. You can go back to room 4 and get the keys to unlock the treasure chest\n")
        print("Health-", str(health))
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated\n", utility_belt)
        print("Unfortunately You cannot perform the shift.\n Game Over\n")

    elif choice == '4':
        print('Congratulations! You have won 100 pieces armor & weaponry\n')
        type, item = 'Armor', '100 pieces armor & weaponry'
        belt_updator(utility_belt, item, type)
        points = 10
        update_points(utility_belt, points, 0)
        print("Your utility_belt is updated\n", utility_belt)
        print("Your health is- ", str(health))
        print('Heres your Utility Belt-', utility_belt)
        print('Game Over\n')


    elif choice == '5':
        print('Sorry! You lost the game. Better luck next time\n')
        points = 10
        update_points(utility_belt, points, 0)
        print("Your health is- \n", str(health))
        print('Heres your Utility Belt-\n',utility_belt)
        print('Game Over\n')


    player_points = utility_belt['Points']
    level = 5
    belt_updator(statistics, player_points, level)
    fd = open('output.txt', 'w')
    fd.truncate(0)
    for level, player_points in statistics.items():
        num1 = str(level)
        num2 = str(player_points)
        r = num1 + "," + num2
        fd.write(r)
        fd.write("\n")

def utilityBelt_initializer():

    ''' To initialize utility belt at the beginning the utility belt initializer function is used primary items
        like points Weapon, coins, keys are initialized'''
    utility_belt['Points'] = 0
    utility_belt['Weapon']=''
    utility_belt['coins']=0
    utility_belt['Key']=''


if __name__ == '__main__':

    utilityBelt_initializer()
    intro()
    print('You have reached the first Level of Game')
    First_room()

    print("Stats Saved")
    raise SystemExit
