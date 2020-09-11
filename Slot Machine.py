import random
import os
import time

keepLoop = True
coins = 100

clear = lambda: os.system('cls')

def roll():
    slots = []

    for x in range(3):
        slots.append(random.randint(0, 9))
    
    return slots
    




while keepLoop:
    clear()
    print(f'You have {coins} coins.\n1 - Roll\n2 - Exit')

    ask = input(': ')

    if ask == '1':
        clear()
        if coins < 10:
            print(f'You have {coins} coins.\nYou don\'t have enough coins for that!')
            time.sleep(2)
        else:
            bet = input(f'You have {coins} coins.\nHow many spins do you want: ')
            for x in range(int(bet)):
                if coins < 10:
                    break
                clear()
                slots = roll()
                if slots[0] == slots[1] and slots[1] == slots[2]:
                    print(f'You have {coins} coins.\nYou won!\n{slots[0]} {slots[1]} {slots[2]}')
                    coins += 10
                else:
                    print(f'You have {coins} coins.\nYou lost!\n{slots[0]} {slots[1]} {slots[2]}')
                    coins -= 5
                time.sleep(0.5)
    elif ask == '2':
        keepLoop = False
    else:
        print('Uh oh! Choose again!')
