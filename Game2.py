import time
#FIXME - Need to add timing for all print functions
import random

#########################################################################

monster = ''
monster_hp = 0
monster_gp = 0
monster_xp = 0
player_hp = 40
player_gp = 0
player_xp = 0
monster_kills = 0
weapon = ''
mon_wep_dam = 0

##########################################################################

#Monster List
monster_size = ['Puny', 'Smallish', 'Average-sized', 'Beefy', 'Huge']
monster_type = ['Cave', 'Swamp', 'Forest', 'Desert', 'Snow']
monster_race = ['Ratman', 'Goblin', 'Orc', 'Hobgoblin', 'Troll']
monster_rank = ['Scout', 'Bandit', 'Warrior', 'Chief', 'Lord']

#Weapon List
weapon_mat = ['wooden', 'iron', 'steel', 'mithril', 'crystal']
weapon_type = ['stick', 'dagger', 'sword', 'axe', 'hammer', 'maul']

###########################################################################

#Monster Generator

def make_monster():
    ran_mon_size = random.choice(monster_size)
    ran_mon_type = random.choice(monster_type)
    ran_mon_race = random.choice(monster_race)
    ran_mon_rank = random.choice(monster_rank)
    global monster
    monster = ran_mon_size + ' ' + ran_mon_type + ' ' + ran_mon_race + ' ' + ran_mon_rank
    global monster_hp
    monster_hp = int(monster_size.index(ran_mon_size)) + int(monster_type.index(ran_mon_type)) + int(monster_race.index(ran_mon_race)) + int(monster_rank.index(ran_mon_rank)) + 4
#FIXME - add Curtis' gold generation code
    global monster_gp
    monster_gp = monster_hp * 2
    global monster_xp
    monster_xp = monster_hp * 2

######################################################################

#Monster Weapon Generator

def make_weapon():
    ran_mon_wep_mat = random.choice(weapon_mat)
    ran_mon_wep_type = random.choice(weapon_type)
    global weapon
    weapon = ran_mon_wep_mat + ' ' + ran_mon_wep_type
    global mon_wep_dam
    mon_wep_dam = int(weapon_mat.index(ran_mon_wep_mat)) + int(weapon_type.index(ran_mon_wep_type)) + 2

#---------------------------------------------------------------------

#Player Weapon Generator

ran_play_wep_mat = random.choice(weapon_mat)
ran_play_wep_type = random.choice(weapon_type)
player_weapon = ran_play_wep_mat + ' ' + ran_play_wep_type
player_wep_dam = int(weapon_mat.index(ran_play_wep_mat)) + int(weapon_type.index(ran_play_wep_type)) + 2

##########################################################################
#########################################################################

def monster_fight():
    global monster
    global monster_hp
    global monster_gp
    global monster_xp
    global player_hp
    global player_gp
    global player_xp
    global monster_kills
    global weapon
    global mon_wep_dam
    global player_weapon
    global player_wep_dam
    print(f'You encountered a {monster} wielding a {weapon}.')
    while monster_hp > 0:
        print(f'The {monster} hit you!')
        player_hp -= mon_wep_dam
        print(f'You hit the {monster}!')
        monster_hp -= player_wep_dam
        if player_hp <= 0:
            print("You're dead, game over")
            break
        if player_hp > 0:
            if monster_hp <= 0:
                print('Congratulations, you killed it!')
                player_gp += monster_gp
                player_xp += monster_xp
                monster_kills += 1
                print(f'Player GP: {player_gp}, Player XP: {player_xp}, Monsters Killed: {monster_kills}')
                new_wep = input(f"Do you want to keep the {monster}'s {weapon}, and throw away your {player_weapon}?\n")
                if new_wep == 'Yes':
                    player_weapon = weapon
                    print(f"Sweet! You've got a nice new {weapon} now.")
                elif new_wep == 'No':
                    print(f"You leave the {weapon} where it was.")
                else:
                    print(f"Invalid command.")
            if monster_hp > 0:
                keepon = input('What do you want to do? Attack or Run?\n')
                if keepon != 'Attack' and keepon != 'Run':
                    print('Your only options are to Attack or Run. You must choose one.')
                if keepon == 'Run':
                    break

def goto_dungeon():
    enter_dungeon = input("Do you wish to enter the dungeon?\n")
    if enter_dungeon == 'Yes':
        make_monster()
        make_weapon()
        monster_fight()
    if player_gp >= 100:
        print("Congratulations! You've earned enough gold to settle down and retire.\nGame over.")
    elif monster_kills >= 10:
        print("Congratulations! Your efforts have successfully purged evil from this land. You may now rest.\nGame over.")
    elif player_hp <= 0:
        print("You're dead, game over.")
    else:
        where_to = input("Where would you like to go now? Available options are Dungeon, Blacksmith, Temple, and Home.\n")
        if where_to == 'Dungeon':
            goto_dungeon()
        if where_to == 'Blacksmith':
            goto_blacksmith()
        if where_to == 'Temple':
            goto_temple()
        if where_to == 'Home':
            goto_home()

def goto_blacksmith():
    global player_wep_dam
    global player_weapon
#FIXME - spend 10 player_gp to add 1 to player_wep_dam
    print('The town blacksmith grins at you as you walk in. "Hail, friend! Have you come to upgrade your weapon?"')
    print("A sign on the wall advertises this shop's speciality: '10 gp! Make your weapon hit harder!'")
    weapon_upgrade = input(f"Would you like to spend 10 gp to improve your {player_weapon}'s damage from {player_wep_dam} to {player_wep_dam +1 }? Yes or No?\n")
#FIXME - check for player_gp, subtract player_gp
    if weapon_upgrade == 'Yes':
        player_wep_dam += 1
        player_weapon += '+'
        print(f'{player_weapon}, {player_wep_dam}')
    where_to = input("Where would you like to go now? Available options are Dungeon, Blacksmith, Temple, and Home.\n")
    if where_to == 'Dungeon':
        goto_dungeon()
    if where_to == 'Blacksmith':
        goto_blacksmith()
    if where_to == 'Temple':
        goto_temple()
    if where_to == 'Home':
        goto_home()

def goto_temple():
#FIXME - Spend 10 player_xp to add 1 player_hp
    print("You're at the Temple, but no incense is burning. There's no one here.")
    where_to = input("Where would you like to go now? Available options are Dungeon, Blacksmith, Temple, and Home.\n")
    if where_to == 'Dungeon':
        goto_dungeon()
    if where_to == 'Blacksmith':
        goto_blacksmith()
    if where_to == 'Temple':
        goto_temple()
    if where_to == 'Home':
        goto_home()

def goto_home():
#FIXME - Rest to fully restore player_hp, or give option to give up on your quest (quit game).
    global player_hp
    print("You're home, but you've lost your key. You can't get in.")
    take_rest = input("Take a nap in your hammock?\n")
    if take_rest == 'Yes':
        player_hp = 40
        print(f"You feel rejuvenated. Your HP is now at {player_hp}.")
    where_to = input("Where would you like to go now? Available options are Dungeon, Blacksmith, Temple, and Home.\n")
    if where_to == 'Dungeon':
        goto_dungeon()
    if where_to == 'Blacksmith':
        goto_blacksmith()
    if where_to == 'Temple':
        goto_temple()
    if where_to == 'Home':
        goto_home()

################################################################################
#--------------------GAME START----------------------#

#FIXME - Add Character Creation Codes Here or create a function
#FIXME - Add initial player_weapon to Character Creation
while player_hp <= 0:
    break

where_to = input("Where would you like to go now? Available options are Dungeon, Blacksmith, Temple, and Home.\n")
if where_to == 'Dungeon':
    goto_dungeon()
if where_to == 'Blacksmith':
    goto_blacksmith()
if where_to == 'Temple':
    goto_temple()
if where_to == 'Home':
    goto_home()
