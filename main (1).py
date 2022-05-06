#Imports
from colorama import init
from colorama import Fore, Back, Style
import time

#Start Username Menu
print(Fore.BLUE + 'Welcome!')
time.sleep(0.7)
print(' ')
username = input(Fore.MAGENTA+ 'Whats Your Name for later? ')
time.sleep(0.7)
print(' ')
print(Fore.RED + 'Starting up menu')
time.sleep(0.9)
#Space Out
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
#Start Main Menu
print(Fore.GREEN + '----------------------------------------------')
print(Fore.GREEN + '≋3≋5≋3≋m≋s≋s≋ ≋M≋e≋n≋u≋')
print(' ')
time.sleep(0.6)
print('≋3≋5≋3≋m≋s≋s≋ ≋M≋e≋n≋u≋')
print(' ')
time.sleep(0.6)
print('≋3≋5≋3≋m≋s≋s≋ ≋M≋e≋n≋u≋')
print(' ')
time.sleep(0.6)
print('≋3≋5≋3≋m≋s≋s≋ ≋M≋e≋n≋u≋')
print(' ')
time.sleep(0.6)
print('≋3≋5≋3≋m≋s≋s≋ ≋M≋e≋n≋u≋')
print(' ')
time.sleep(0.6)
print('≋3≋5≋3≋m≋s≋s≋ ≋M≋e≋n≋u≋')
print(' ')
print('----------------------------------------------')
time.sleep(1)
#Start Full Menu
print(Fore.RED + 'Welcome!')
print(' ')
print(' ')
print(Fore.MAGENTA + "Welcome To our menu! " + username)
print(' ')
menu_options = {
    1: 'My Discord!',
    2: 'My Github!',
    3: 'My Youtube!',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('https://discord.gg/cyjGXpuPP3')

def option2():
     print('https://github.com/353mss')

def option3():
     print('https://www.youtube.com/channel/UCWJbbR4o8Gqf4ipHBiUU4kw')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Thanks For using my program!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')

      #Use this all you want -353mss