from main import *

underline = '\33[4m'

#At character creation, each class receives a bonus to a certain game stat, based on the class chosen.
#Dwarves: Starting Health is higher (like 30 instead of 20)
#Elves: More XP (when xp is earned after defeating a boss, multiply by 2 instead of 1
#Dragonkin: More GP (same as Elves, but for gp instead)
#Goliaths: More damage (player weapon damage is multiplied by 2)
#Humans: Multiplier of 1.3 to everything



#startname is what is going to be used throughout the entirety of the game.

#def startname():
#    name = input("Ahhh, another potential soul is amongst us. Tell us, what is you're name? \n")
#    print(f'{name}..... What a fascinating name')
    

#use the respawn after you lose a fight and die. 
#there should be the option to either to die and quit and there should be the option to replay the game.

def respawn():
    print("We see, now let us begin the reincarnation process.\nWe will bestow upon your choices.\n1. Human (All-rounder)"
          "\n2. Elves (Extra XP)\n3. Dwarves (Hearty)\n4. Goliaths (Extra Pow)\n5. Dragonkin (Extra Gold)" )

#this is now going to be the list of characters as they are connected to the main screen

#each character is going to recieve
def dwarf():
    print("You have chosen Dwarf")
    player_hp = 50
    print("As a Dwarf ou now have increased HP!")
    where_to

def elf():
    print("You have chosen Elf")
    player_xp * 2
    print("As an Elf you now have Double XP")
    where_to

def dragonskin():
    print("You have chosen Dragonskin")
    player_gp * 2
    print("As a Dragonskin you now have Double GP")
    where_to

def goliath():
    print("You have chosen Goliath")
    player_wep_dam * 2
    print("As a Goliath you now have double weapon damage")
    where_to

def human():
    print("You have chosen Human")
    total_player_hp * 1.2
    player_hp * 1.2
    player_gp * 1.2
    player_xp * 1.2
    print("As a Human you now have a 20% BUFF in HP, GP, and XP")
    where_to

def character_selection():
    print("You now have the choice to choose you class.")
    time.sleep(.5)
    print("There are several classes and all have their advantages so choose wisely...")
    time.sleep(.5)
    print(underline + "CHARACTER SELECTION MENU")
    print("1 - DWARF (INCREASED PLAYER XP)")
    print("2 - ELF (DOUBLE XP)")
    print("3 - DRAGONSKIN (DOUBLE GP)")
    print("4 - GOLIATH (DOUBLE DAMAGE)")
    print("5 - HUMAN (COMPLETE 20% STAT INCREASE (INCREASED HP, GP, AND XP))")

    sel = input()
    if sel := "1":
        dwarf()
    if sel := "2":
        elf()
    if sel := "3":
        dragonskin()
    if sel := "4":
        goliath()
    if sel := "5":
        human()