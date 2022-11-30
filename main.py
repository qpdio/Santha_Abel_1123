from os import system
from functions import menu, szamkitalalos, rekordok, osszes_rekordok_kilistazasa, rekordok_betoltese, ko_papir_ollo, pontok_mentese_fajlba

rekordok_betoltese()

choice=''
while choice!='0':
    system('cls')
    choice=menu()
    if choice=='1':
        system('cls')
        #Amőba
    elif choice=='2':
        system('cls')
        ko_papir_ollo()
    elif choice=='3':
        system('cls')
        szamkitalalos()
        rekordok_betoltese()
    elif choice=='4':
        system('cls')
        rekordok_choice = ''
        while rekordok_choice!='0':
            system('cls')
            rekordok_choice = rekordok()
            if rekordok_choice=='0':
                system('cls')
            elif rekordok_choice=='1':
                system('cls')
                osszes_rekordok_kilistazasa()
            elif rekordok_choice=='2':
                system('cls')
                #legjobb_rekord_kilistazasa()
