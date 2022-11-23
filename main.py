from os import system
from functions import menu, szamkitalalos

choice=''
while choice!='0':
    system('cls')
    choice=menu()
    if choice=='1':
        system('cls')
        #Amőba
    elif choice=='2':
        system('cls')
        #Kő papír olló
    elif choice=='3':
        system('cls')
        szamkitalalos()
    elif choice=='4':
        system('cls')
        #rekordok
