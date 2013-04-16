lake_fish = ["Trout", "Old Boot"]

river_fish = ["Trout", "Salmon"]

beach_fish = ["Conger Eel", "Flounder"]

menu_item = 0
while menu_item !=("Q"):
    print "Where would you like to fish?  At the Lake, the River, or the Beach?"
    print "To quit, press Q."
    menu_item = raw_input("Pick an option: ")

    if menu_item == ("Lake"):
        from random import choice
        if choice(lake_fish) == "Old Boot":
            print "Oh . . . it was just an old boot . . ."
        else:
            print "You caught a", choice(lake_fish),"!"

    elif menu_item == ("River"):
        from random import choice
        print "You caught a ", choice(river_fish), "!"
        
    elif menu_item == ("Beach"):
        from random import choice
        print "You caught a ", choice(beach_fish), "!"
            
print "Goodbye."
