# FIXME - Need to add timing for all print functions
import random
from storyline import *
from logo_d import *
from wpog import *

insert_logo()
name = input("Before we go on our quest what shall I call you?\n")

#########################################################################
# title screen


def title():
    wp()
    insert_logo()
    print('\x1B[3mAre you ready to begin your journey against the forces of infinite darkness?')
    print()

# intro credits


def lore():
    wp()
    insert_logo2()
    print('')
    print('\x1B[3m In the time after the great collapse, the abyss had consumed the old world.\x1B[0m')
    print('\x1B[3m Ancient creatures of evil ruled the realms with chaos and destruction.\x1B[0m')
    print('\x1B[3m When the gods decided to create the new world, they used a spark from the Origin Flame.\x1B[0m')
    print('\x1B[3m It contained the combined will of the gods to bring light and life to creation.\x1B[0m')
    print('\x1B[3m This light pushed back the darkness and the evil creatures that dwell within.\x1B[0m')
    print('\x1B[3m For thousands of years, the shadows have been held at bay by the embers of the spark.\x1B[0m')
    print('\x1B[3m But the hunger of the abyss has grown and seeks to devour the lands graced by light.\x1B[0m')
    print('\x1B[3m The long forgotten creatures of darkness have broken free of their chains and descend upon the realm.\x1B[0m')
    print('\x1B[3m The cries of mankind have reached the gods and they have chosen a hero to push back the dark.\x1B[0m')
    print('\x1B[3m And now a new journey begins to find the Origin Flame and use the spark to bring back the light.\x1B[0m')
    print('')
    time.sleep(4)

# character creation


def hero_mission():
    print('\x1B[3m At the grand temple of Lewrac an oracle from the gods declare that a new hero has been chosen.\x1B[0m')
    print('\x1B[3m This hero will have to journey to the great dungeon and fight against the creatures of the abyss.\x1B[0m')
    print('\x1B[3m They have received the blessings of the gods and will become the champion of in the realm.\x1B[0m')


# travel to dungeon


def dungeon_journey():
    print('\x1B[3m The sun has lead you to cross the Aleshian Mountains and the moon guided you through the Forest of Morveir.\x1B[0m')
    print('\x1B[3m You have arrived at the entrance of the Dungeon of the Origin Flame.\x1B[0m')
    print('\x1B[3m The blessings of the gods rest upon you young hero.\x1B[0m')
    print('\x1B[3m Go forth and claim the spark that will become the weapon against those from the abyss.\x1B[0m')



# the intro to the first enemy encounter in the dungeon

def intro_fight():
    print('\x1B[3m Upon searching the dungeon, you have encountered a dark creature.\x1B[0m')
    print('\x1B[3m This will be your first battle against the enemies of mankind.\x1B[0m')
    print('\x1B[3m Fear has no place in the heart of a hero.  Summon your courage and do not let your enemy pass.\x1B[0m')
    print('\x1B[3m Prepare yourself and defeat your foe.')


# when they return to the dungeon from town, temple, etc.


def dungeon_return():
    print('\x1B[3m Your battle against the forces of darkness and chaos has not ended yet.\x1B[0m')
    print('\x1B[3m Calm your heart and fulfil your destiny.\x1B[0m')
    print('\x1B[3m Are you ready to continue your conquest of the dungeon?: Yes or No?\x1B[0m')


def hero_win_spark():
    print('\x1B[3m With the defeat of the dungeon enemies you have obtained the power of the Origin Flame.\x1B[0m')
    print('\x1B[3m The warmth of the fire embraces you and the light shines forth destroying the shadows.\x1B[0m')
    print('\x1B[3m Across the realm no darkness can within the power of the flame.\x1B[0m')
    print('\x1B[3m Hope has been restored and chaos has been returned to the abyss.\x1B[0m')
#########################################################################

monster = ''
monster_hp = 0
monster_gp = 0
monster_xp = 0
total_player_hp = 40
player_hp = 40
player_gp = 0
player_xp = 0
monster_kills = 0
weapon = ''
mon_wep_dam = 0
mon_wep_value = 0
armor = ''
mon_armor_points = 0
mon_armor_value = 0
ran_junk1 = ''
ran_junk2 = ''
ran_treasure = ''
junk1_value = 0
junk2_value = 0
treasure_valure = 0
monster_gp_mult = 1
monster_xp_mult = 1
wep_dam_mult = 1


def troll_c():
    print("  ⋌⁻⁻⋋.-⁻⁻⁻⁻⁻-.⋌⁻⁻⋋  ")
    print("  \ ./          \. /  ")
    print("   \ | ≤≥⁽  ⁾≤≥ | /   ")
    print("    ⋁\ ._^__^_. /⋁     ")
    return


def human_c():
    print('         ||||| ')
    print('          o   o')
    print('            >' )
    print('          ooooo')
    return


def ratman_c():
    print('   .--,       .--,')
    print('  ( (  \.---./  ) ) ')
    print("   '.__/o   o\__.' ")
    print('      {=  ^  =}')
    return


def goblin_c():
    print('       .-----.    ')
    print("     \⸃)      (⸂/   ")
    print('      \≤≥ ⋎ ≤≥/    ')
    print("       '^---^'   ")
    return


def orc_c():
    print('      .------.          ')
    print('  .  / __  __ \ .')
    print("   \⸃) ≤≥\∨/≤≥ (⸂/   ")
    print('     \ ▴_\/_▴ / ')
    print("      \______/   ")
    return


def hobgoblin_c():
    print("     .-⁻⁻⁻⁻⁻⁻⁻-.   ")
    print("    / ⋰⋱   ⋰⋱ \  ")
    print("   /⋰≤≥ \  / ≤≥⋱\ ")
    print("   ∖⋱          ⋰/ ")
    return


def body_figure1():
    print('     .⁻⁻||⁻⁻.')
    print("    / / || \ \ ")
    print('   (_/  ||  \_)')


def body_figure2():
    print('     .⁻⁻    ⁻⁻.')
    print("    / / |  | \ \ ")
    print('   (_/  |  |  \_)')


def body_figure3():
    print('      .⁻⁻    ⁻⁻.')
    print("     / /\    /\ \ ")
    print('    (_/ |    | \_)')


def body_figure4():
    print("    .⁻⁻       ⁻⁻.    ")
    print("   / /\ ._|_, /\ \  ")
    print("  (_/ |       | \_)   ")


def body_figure5():
    print("   .⁻⁻    Y    ⁻⁻.    ")
    print("  /  Y  ._|_,  Y  \  ")
    print("( _/ |         | \_ )   ")


##########################################################################

#Monster List
monster_size = ['Puny', 'Smallish', 'Average-sized', 'Beefy', 'Huge']
monster_type = ['Cave', 'Swamp', 'Forest', 'Desert', 'Snow']
monster_race = ['Ratman', 'Goblin', 'Orc', 'Hobgoblin', 'Troll']
monster_rank = ['Scout', 'Bandit', 'Warrior', 'Chief', 'Lord']

#Weapon List
weapon_mat = ['wooden', 'iron', 'steel', 'mithril', 'crystal']
weapon_type = ['stick', 'dagger', 'sword', 'axe', 'hammer', 'maul']

#Armor List
armor_mat = ['cloth', 'leather', 'chain', 'steel', 'mithril', 'crystal']
armor_type = ['shirt', 'breastplate', 'suit']

#Random Loot List
junk_loot = ["some pocket lint", "a decent-looking crust of bread", "a cool bird skull", "a robin's egg", "a short piece of string", "a bit of cheese", "the keys to a 96 Geo Metro"]
treasure_loot = ["10 gold pieces", "a pair of silver earrings", "a bronze ceremonial dagger", "a bag of shiny rocks", "a book of poetry in an unknown language", "about two thirds of a gold ingot", "an obsidian sculpture of an Ancient god", "a ruby the size of your fist", "a gold and sapphire circlet", "a perfectly clear diamond"]

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

#body for everyone
    #'Ratman', 'Goblin', 'Orc', 'Hobgoblin', 'Troll'
    if ran_mon_race == 'Orc':
        orc_c()
    if ran_mon_race == 'Ratman':
        ratman_c()
    if ran_mon_race == 'Goblin':
        goblin_c()
    if ran_mon_race == 'Hobgoblin':
        hobgoblin_c()
    if ran_mon_race == 'Troll':
        troll_c()


    if ran_mon_size == 'Puny':
        body_figure1()
    if ran_mon_size == 'Smallish':
        body_figure2()
    if ran_mon_size == 'Average-sized':
        body_figure3()
    if ran_mon_size == 'Beefy':
        body_figure4()
    if ran_mon_size == 'Huge':
        body_figure5()


#FIXME - add Curtis' gold generation code
    global monster_gp
    monster_gp = monster_hp * 2
    global monster_xp
    monster_xp = monster_hp * 2

#Monster Armor Generator
def make_armor():
    ran_mon_armor_mat = random.choice(armor_mat)
    ran_mon_armor_type = random.choice(armor_type)
    global armor
    armor = ran_mon_armor_mat + ' ' + ran_mon_armor_type
    global mon_armor_points
    mon_armor_points = ((int(armor_mat.index(ran_mon_armor_mat)) + int(armor_type.index(ran_mon_armor_type)) + 2) / 2)
    global mon_armor_worth
    mon_armor_worth = int(mon_armor_points * 2)

#Monster Weapon Generator
def make_weapon():
    ran_mon_wep_mat = random.choice(weapon_mat)
    ran_mon_wep_type = random.choice(weapon_type)
    global weapon
    weapon = ran_mon_wep_mat + ' ' + ran_mon_wep_type
    global mon_wep_dam
    mon_wep_dam = int(weapon_mat.index(ran_mon_wep_mat)) + int(weapon_type.index(ran_mon_wep_type)) + 2

#Monster Loot Generator
def make_loot():
    ran_junk1 = random.choice(junk_loot)
    junk1_value = 1
    ran_junk2 = random.choice(junk_loot)
    junk2_value = 1
    ran_treasure = random.choice(treasure_loot)
    treasure_value = int(treasure_loot.index(ran_treasure))*10
    global monster_bag
    monster_bag = ran_junk1 + ', ' + ran_junk2 + ', ' + ran_treasure
    global monster_bag_value
    monster_bag_value = int(junk1_value + junk2_value + treasure_value)

#---------------------------------------------------------------------

#Player Weapon Generator
ran_play_wep_mat = random.choice(weapon_mat)
ran_play_wep_type = random.choice(weapon_type)
player_weapon = ran_play_wep_mat + ' ' + ran_play_wep_type
player_wep_dam = int(weapon_mat.index(ran_play_wep_mat)) + int(weapon_type.index(ran_play_wep_type)) + 2

#Player Armor Generator
player_armor = "Old Rags"
player_armor_points = 0

##########################################################################
##########################################################################

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
    global armor
    global mon_armor_points
    global player_armor
    global player_armor_points
    total_damage = player_wep_dam - mon_armor_points
    #FIXME Update Armor Dialogue
    print(f'You encountered a {monster} wielding a {weapon}. It appears to be wearing a {armor}.')
    while monster_hp > 0:
        #monster attack
        if player_armor_points < mon_wep_dam:
            print(f'The {monster} hit you! It dealt {mon_wep_dam} damage. Your {player_armor} reduced the damage by {player_armor_points} points.')
            player_hp -= (mon_wep_dam - player_armor_points)
            print(f"You have {player_hp} HP left.")
        else:
            print(f'Your {player_armor} absorbed all the damage!')
#FIXME Should we have the player hp check here
        #player attack
        if player_wep_dam > mon_armor_points:
            print(f'You hit the {monster}! You did {player_wep_dam} damage, but it looks like the {armor} reduced it by {mon_armor_points} points.')
            monster_hp -= total_damage
            print(f"The {monster} has {monster_hp} HP left.")
        else:
            print("The armor negated the damage....")
            print(f"The {monster} still has {monster_hp} HP left.")

        #player hp check
        if player_hp <= 0:
            print("You're dead, game over.")
            break
        if player_hp > 0:
            if monster_hp <= 0:
                print('Congratulations, you killed it!')
                player_xp += monster_xp
                monster_kills += 1
                print(f"You loot the {monster} and find a bag containing {monster_bag}, and {monster_gp} gold pieces.")
                print(f"Of course, it's also carrying its {weapon} and wearing that {armor}.")
                new_wep = input(f"Do you want to keep the {monster}'s {weapon}, and put your {player_weapon} away?\n")
                if new_wep == 'Yes':
                    player_weapon = weapon
                    print(f"Sweet! You've got a nice new {weapon} now.")
                elif new_wep == 'No':
                    print(f"You leave the {weapon} where it was.")
                else:
                    print(f"Invalid command.")
                new_armor = input(f"Do you want to put on the {monster}'s {armor}?\n")
                if new_armor == 'Yes':
                    player_armor = armor
                    player_armor_points = mon_armor_points
                    print(f"Somehow, the {monster}'s {armor} fits you perfectly. This ought to help some.")
                elif new_wep == 'No':
                    print(f"Yeah, that makes sense. Peeling a {armor} off a dead guy? Ew.")
                else:
                    print(f"Invalid command.")
                player_gp += monster_gp
                print(f'Player GP: {player_gp}, Player XP: {player_xp}, Monsters Killed: {monster_kills}')
            if monster_hp > 0:
                keepon = input('What do you want to do? Attack or Run?\n')
                if keepon != 'Attack' and keepon != 'Run':
                    print('Your only options are to Attack or Run. You must choose one.')
                if keepon == 'Run':
                    break

def goto_dungeon():
    wp()
    insert_logo()
    dungeon_journey()
    enter_dungeon = input("Do you wish to enter the Dungeon " + name +"? (Yes/No)\n")
    if enter_dungeon == 'Yes' or enter_dungeon == 'yes':
        make_monster()
        make_weapon()
        make_armor()
        make_loot()
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
    wp()
    insert_logo()
    global player_wep_dam
    global player_weapon
    global player_gp
    print(f'The town blacksmith grins at you as you walk in. "Hail, {name}! Have you come to upgrade your weapon?"')
    print("A sign on the wall advertises this shop's speciality: '10 gp! Make your weapon hit harder!'")
    weapon_upgrade = input(f"Would you like to spend 10 gp to improve your {player_weapon}'s damage from {player_wep_dam} to {player_wep_dam +1 }? Yes or No?\n")
    if weapon_upgrade == 'Yes':
        if player_gp < 10:
            print('The blacksmith frowns down at you. "What is this? That\'s not enough gold."')
        if player_gp >= 10:
            player_gp -= 10
            player_wep_dam += 1
            player_weapon += '+'
            print(f'{player_weapon} {player_wep_dam}')
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
    wp()
    insert_logo()
    global player_xp
    global total_player_hp
    global player_hp
    #need to remove the function 'gloabal name' and then add it back.2

    print("The Temple stands before you, ancient and imposing. A Temple Maiden Greets you.")
    #add name into the Good Day (name) part
    print(f'"Good day. Have you come to fortify your flesh with the wisdom of your trials?"')
    health_upgrade = input('Spend 10 experience points to improve your health by 1? Yes or No.\n')
    if health_upgrade == 'Yes':
        if player_xp >= 10:
            player_xp -= 10
            player_hp += 1
            total_player_hp += 1
        if player_xp < 10:
            print(f"The Temple Maiden shakes her head sadly.")
            print(f"My dear {name}, I am sorry. You must complete more trials before I can help you.")
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
    wp()
    insert_logo()
    global player_hp
    print(f"Welcome home, {name}. Would you like to Rest and recover HP? Or do you want to just stay inside?")
    home_options = input("Rest or Quit?\n")
    if home_options == 'Rest':
        player_hp = total_player_hp
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
    if home_options == 'Quit':
        print(f'Very well. You sit in your rocking chair and watch as darkness swallows the land.')
        print(f'With your last breath, you know in your heart you could have stopped it, but chose to stay home.')
        print(f'Game Over.')
        player_hp = -10


underline = '\33[4m'


# At character creation, each class receives a bonus to a certain game stat, based on the class chosen.
# Dwarves: Starting Health is higher (like 30 instead of 20)
# Elves: More XP (when xp is earned after defeating a boss, multiply by 2 instead of 1
# Dragonkin: More GP (same as Elves, but for gp instead)
# Goliaths: More damage (player weapon damage is multiplied by 2)
# Humans: Multiplier of 1.3 to everything


# startname is what is going to be used throughout the entirety of the game.

# def startname():
#    name = input("Ahhh, another potential soul is amongst us. Tell us, what is your name? \n")
#    print(f'{name}..... What a fascinating name')


# use the respawn after you lose a fight and die.
# there should be the option to either to die and quit and there should be the option to replay the game.

def respawn():
    print(
        "We see, now let us begin the reincarnation process.\nWe will bestow upon your choices.\n1. Human (All-rounder)"
        "\n2. Elves (Extra XP)\n3. Dwarves (Hearty)\n4. Goliaths (Extra Power)\n5. Dragonkin (Extra Gold)")



def dwarf():
    wp()
    insert_logo()

    global monster_gp_mult
    global monster_xp_mult
    global total_player_hp
    global wep_dam_mult
    print("You have chosen Dwarf")
    print("As a Dwarf you now have increased HP!")
    monster_gp_mult = 1
    monster_xp_mult = 1
    total_player_hp = 60
    wep_dam_mult = 1

    time.sleep(2)



def elf():
    wp()
    insert_logo()
    global monster_gp_mult
    global monster_xp_mult
    global total_player_hp
    global wep_dam_mult
    print("You have chosen Elf")
    print("As an Elf you now have Double XP")
    monster_gp_mult = 1
    monster_xp_mult = 2
    total_player_hp = 40
    wep_dam_mult = 1
    time.sleep(2)




def dragonskin():
    wp()
    insert_logo()

    global monster_gp_mult
    global monster_xp_mult
    global total_player_hp
    global wep_dam_mult
    print("You have chosen Dragonskin")
    print("As a Dragonskin you now have Double GP")
    monster_gp_mult = 2
    monster_xp_mult = 1
    total_player_hp = 40
    wep_dam_mult = 1
    time.sleep(2)





def goliath():
    wp()
    insert_logo()

    global monster_gp_mult
    global monster_xp_mult
    global total_player_hp
    global wep_dam_mult
    print("You have chosen Goliath")
    print("As a Goliath you now have double weapon damage")
    monster_gp_mult = 1
    monster_xp_mult = 1
    total_player_hp = 40
    wep_dam_mult = 2
    time.sleep(2)





def human():
    wp()
    insert_logo()

    global monster_gp_mult
    global monster_xp_mult
    global total_player_hp
    global wep_dam_mult
    print("You have chosen Human")
    monster_gp_mult = 1.2
    monster_xp_mult = 1.2
    total_player_hp = 45
    wep_dam_mult = 1.2
    print("As a Human you now have a 20% BUFF in HP, GP, and XP")
    time.sleep(2)




def character_selection():
    print("You now have the choice to choose your class.")
    time.sleep(.5)
    print("There are several classes and all have their advantages, so choose wisely...")
    print('')
    time.sleep(.5)
    text = "CHARACTER SELECTION MENU"
    underlined_text = "\x1B[4m" + text + "\x1B[0m"
    print(underlined_text)
    print("1 - DWARF (INCREASED PLAYER HP)")
    print("2 - ELF (DOUBLE XP)")
    print("3 - DRAGONSKIN (DOUBLE GP)")
    print("4 - GOLIATH (DOUBLE DAMAGE)")
    print("5 - HUMAN (COMPLETE 20% STAT INCREASE (INCREASED HP, GP, AND XP))")
    print("PLEASE SELECT FROM.. (1, 2, 3, 4, or 5) ")

    sel = input()
    if sel == '1':
        dwarf()
    elif sel == '2':
        elf()
    elif sel == '3':
        dragonskin()
    elif sel == '4':
        goliath()
    elif sel == '5':
        human()
#fix underline in character selection
#NEED TO DO - Add Name fucntionS

################################################################################



#--------------------GAME START----------------------#

#FIXME - Add Character Creation Codes Here or create a function
#FIXME - Add initial player_weapon to Character Creation

insert_logo()
wp()
title()


character_selection()

lore()

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




