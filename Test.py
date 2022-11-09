def firstroom():
    print("What is the way you would like to go? (LEFT/RIGHT)")
    direction=input()
    if direction == "right":
        print ("Nice choice you are entering a new dungeon space")
        secondroom()
    else:
        deathroom()

def secondroom():
    print("You have entered the second-room (WOULD YOU LIKE TO...)")
    print("CONTINUE FORWARD? (YES OR NO)")
    # you can conitnue to keep adding lines using this format and make the story as long as you would
    # like using the siad print("THIS IS KENDALLS EXAMPLE")
    direction=input()
    if direction == "yes":
        print("GOOD CHOICE")
        print("this is as far as development has reach....")
        #yall call easily build upon this -kendall 10/14/22
        thirdroom()
    else:
        deathroom()

def thirdroom():
    quit()

def deathroom():
    print("You Just DIED!!!")
    quit()

firstroom()