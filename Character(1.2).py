# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = input("Ahhh, another potential soul is amongst us. Tell us, what is you're name? \n")
    print(f'{name}..... What a fascinating name, now tell us, what are your pronouns?')
    pronouns = input()
    print("We see, now let us begin the reincarnation process.\nWe will bestow upon your choices.\n1. Human (All-rounder)"
          "\n2. Elves (Extra XP)\n3. Dwarves (Hearty)\n4. Goliaths (Extra Pow)\n5. Dragonkin (Extra Gold)" )
    choice = input()
    redef = str()
    health = int
    power = int
    gold = 0
    XP = 0
    H_intake = int
    P_intake = int
    XP_intake = int
    gold_intake = int

    def majin_mode():
        print("    ------         ------")
        print("  /        \     /        \ ")
        print("<            \ /            > ")
        print("                              ")
        print("             / \              ")
        print("            /   \               ")
        print("           /     \               ")
        print("          /       \               ")
        print("         /_________\               ")
        print("                         ")
        print(" _____________________________")
        print("/    |    |    |    |    |    \ ")
        print("|    |    |    |    |    |     |")
        print("|    |    |    |    |    |     |")
        print("\    |    |    |    |    |     /")
        print(" \----------------------------/")
        print("  \  |    |    |    |    |   /")
        print("   \ |    |    |    |    | /")
        print("    \|    |    |    |    |/")
        print("     \    |    |    |    /")
        print("     ------________------")



while choice != "Human" or choice != "human" or choice != "Elves" or choice != "elves" or choice != "Dwarves" or choice != "dwarves" or choice != "Goliaths" or choice != "goliaths" or choice != "Dragonkin" or choice != "dragonkin" or choice != "46-12-25":
    print("Lets try that again, Here are the choices again.")
    print("1. Human (All-rounder)\n2. Elves (Extra XP)\n3. Dwarves (Hearty)\n4. Goliaths (Extra Pow)\n5. Dragonkin (Extra Gold)")
    choice = input()

    if choice == "Human" or choice == "human":
        redef = "Human"
        print("Ah a Human, a good choice for those who want a little bit of everything. Are you satisfied with this choice?")
        confirm = input()
        if confirm == "Yes" or confirm == "yes":
            health = 25
            power = 15
            H_intake = 2
            P_intake = 2
            XP_intake = 2
            gold_intake = 2
            print(f"Then you are ready to enter this world, we wish you the best of luck, {name} the {pronouns} {redef}.")
            break

    elif choice == "Elves" or choice == "elves":
        redef = "Elf"
        print("The Elves, this life form is best suitable for the souls who wish to play smart. Are you satisfied with this choice?")
        confirm = input()
        if confirm == "Yes" or confirm == "yes":
            health = 20
            power = 10
            H_intake = 1
            P_intake = 1
            XP_intake = 3
            gold_intake = 1
            print(f"Then you are ready to enter this world, we wish you the best of luck, {name} the {pronouns} {redef}.")
            break

    elif choice == "Dwarves" or choice == "dwarves":
        redef = "Dwarf"
        print("Dwarves are known to be one of the most long living life forms. Are you satisfied with this choice?")
        confirm = input()
        if confirm == "Yes" or confirm == "yes":
            health = 35
            power = 10
            H_intake = 3
            P_intake = 1
            XP_intake = 1
            gold_intake = 1
            print(f"Then you are ready to enter this world, we wish you the best of luck, {name} the {pronouns} {redef}.")
            break

    elif choice == "Goliaths" or choice == "goliaths":
        redef = "Goliath"
        print("If you want more power, then the Goliaths are your best option. Are you satisfied with this choice?")
        confirm = input()
        if confirm == "Yes" or confirm == "yes":
            health = 20
            power = 35
            H_intake = 1
            P_intake = 3
            XP_intake = 1
            gold_intake = 1
            print(f"Then you are ready to enter this world, we wish you the best of luck, {name} the {pronouns} {redef}.")
            break

    elif choice == "Dragonkin" or choice == "dragonkin":
        redef = "Dragonkin"
        print(f"With their Midus touch, You can obtain more gold when fighting with the Dragonkin. Are you satisfied with this choice?")
        confirm = input()
        if confirm == "Yes" or confirm == "yes":
            health = 20
            power = 20
            H_intake = 1
            P_intake = 1
            XP_intake = 1
            gold_intake = 3
            print(f"Then you are ready to enter this world, we wish you the best of luck, {name} the {pronouns} {redef}.")
            break

    elif choice == "46-12-25":
        majin_mode()
        print("Are you ready to have Infinite FUN?")
        confirm = input()
        if confirm == "Yes" or confirm == "yes":
            health = 99
            power = 99
            H_intake = 99
            P_intake = 99
            XP_intake = 99
            gold_intake = 99
            name = "Majin"
            pronouns = "Infinite"
            redef = ""
            print("Enjoy....(:")
            break









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
