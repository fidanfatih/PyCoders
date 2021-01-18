'''
Rock-Paper-Scissors Game
* Oyuncularin adlarini alip tas - kagit - makas oyunu oynatiniz. 
* Oyun 10 el surecektir. 10 el sonunda kazanan belli olacaktir. 
* Skor sonucta gosterilecektir.

Human vs PC
'''

from random import choice
from time import sleep

player_1 =input('1st Player Name: ').upper()
player_1_points =0

player_2 = input('2st Player Name: ').upper()
print('\n**Player_2 is your PC. You will play against it!**\n')
player_2_points=0

colors={player_1:'\033[92m', #green
        player_2:'\033[94m', #blue
        'draw':'\033[91m', #red
         0:'\033[00m'} #black

mylist = ["Rock","Paper","Scissors"]
tour = 10

print({v:i+1 for i,v in enumerate(mylist)},end='\n')
for i in range(tour):
    print(f'{colors[0]}\nChoose Your Move From the List Above: ',end='')
    case_1 = mylist[int(input())-1]
    case_2=choice(mylist)
    winner='draw'
    if (case_1 != case_2):
        if ((case_1=='Rock' and case_2=='Scissors') or 
            (case_1=='Scissors' and case_2=='Paper') or 
            (case_1=='Paper' and case_2=='Rock')):
            winner=player_1
            player_1_points+=1
        else: 
            winner=player_2
            player_2_points+=1
    print(f'{colors[winner]}\n{i+1:<2}- {player_1} :{case_1:<8}',
          f'{player_2} :{case_2:<8}',
          f'=====> Winner:{winner}')

    
winner=player_1 if player_1_points > player_2_points else player_2 if player_1_points < player_2_points else 'draw'
print(f'\n{colors[winner]}{player_1}:{player_1_points}   {player_2}:{player_2_points}'
        f'\nWINNER is {winner} !')