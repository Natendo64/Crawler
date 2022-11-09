import time
import random

#Monster List
monster_size = ['Puny', 'Smallish', 'Average-sized', 'Beefy', 'Huge']
monster_type = ['Cave', 'Swamp', 'Forest', 'Desert', 'Snow']
monster_race = ['Ratman', 'Goblin', 'Orc', 'Hobgoblin', 'Troll']
monster_rank = ['Scout', 'Bandit', 'Warrior', 'Chief', 'Lord']

#Weapon List
weapon_mat = ['wooden', 'iron', 'steel', 'mithril', 'crystal']
weapon_type = ['stick', 'dagger', 'sword', 'axe', 'hammer', 'maul']

monster = ''
monster_hp = ''

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
    monster_gp = monster_hp*2
    (monster(monster_hp, monster_gp, monster_xp))
#FIXME - add Curtis' gold generation code
    global monster_gp
    monster_gp = monster_hp * 2

weapon = ''
mon_wep_dam = ''
#Monster Weapon Generator
def make_weapon():
    ran_mon_wep_mat = random.choice(weapon_mat)
    ran_mon_wep_type = random.choice(weapon_type)
    global weapon
    weapon = ran_mon_wep_mat + ' ' + ran_mon_wep_type
    global mon_wep_dam
    mon_wep_dam = int(weapon_mat.index(ran_mon_wep_mat)) + int(weapon_type.index(ran_mon_wep_type)) + 2

#Player Weapon Generator
ran_play_wep_mat = random.choice(weapon_mat)
ran_play_wep_type = random.choice(weapon_type)
player_weapon = ran_play_wep_mat + ' ' + ran_play_wep_type
player_wep_dam = int(weapon_mat.index(ran_play_wep_mat)) + int(weapon_type.index(ran_play_wep_type)) + 2

#Player Stats
player_hp = 20
#FIXME - Add Landon's Character creation code

#Game Start
print(f'Before entering the dungeon, you found a {player_weapon} lying on the ground. Lucky!')
time.sleep(1)
print('Are you ready to proceed? Yes or No.')
time.sleep(1)

proceed = input()
if proceed == 'Yes':
    make_monster()
    make_weapon()
    print(f'You have encountered a {monster} carrying a {weapon}. Fight, or Run?')
    time.sleep(1)
    if input() == 'Fight':
        while player_hp >= 1:

#FIXME Test Line to ensure HP and Weapon Damage are calculating properly. Remove eventually
            print(f'The {monster} has {monster_hp} HP. Its {weapon} does {mon_wep_dam} damage.')
            time.sleep(.5)
            print(f'You have {player_hp} HP. Your {player_weapon} does {player_wep_dam} damage.')
            time.sleep(.5)
#Monster fight
            print(f'The {monster} swings its {weapon} at you for {mon_wep_dam} damage. Ouch!')
            time.sleep(2)
            player_hp -= mon_wep_dam
            if player_hp <= 0:
                print('You have died. Game over.')
                time.sleep(3)
                break
            else:
                print(f"You're down to {player_hp} HP.")
                time.sleep(1)
            print(f'You strike out with your {player_weapon} and do {player_wep_dam} damage.')
            time.sleep(2)
            monster_hp -= player_wep_dam
#Killed the monster
            if monster_hp <= 0:
                print(f'Congratulations! You killed the {monster}!')
                print(f'Before you move on, do you want to take the {weapon} it was carrying, and throw your {player_weapon} away?')
                print('Yes or No')
                time.sleep(3)
                new_wep = input()
                if new_wep == 'Yes':
                    player_weapon = weapon
                    continue
                elif new_wep == 'No':
                    print(f'Yeah, that {weapon} probably sucks.You decide to hold onto your {player_weapon}.')
                    time.sleep(3)
                    continue
                else:
                    print(f"That's not an option. Alright, wise guy, you leave the {weapon} there and keep your {player_weapon}.")
                    time.sleep(3)
                    pass
            else:
                print(f'That was a good hit. The {monster} has {monster_hp} left. Do you want to continue Fighting, or Run?')
        else:
            print(f'Are you ready to continue to the next room in the dungeon? Yes or No.')
            time.sleep(3)
            keepon = input()
            while keepon == 'Yes':
                continue
            else:
                pass
#        else:
#            print('That is not a valid command.')

    else:
        print(f'You manage to escape from the {monster}. Whew!')



#FIXME - Typing No doesn't do anything
elif proceed == 'No':
    print(f'Okay, then you go back home. Game over.')
    time.sleep(3)
else:
    print('That is not a valid command.')
    time.sleep(3)