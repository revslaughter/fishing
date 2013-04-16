lake_fish = ["Trout", "Old Boot"]

river_fish = ["Trout", "Salmon"]

beach_fish = ["Conger Eel", "Flounder"]

line_cast = ["The float bobs down slightly", "The float disappears under the water", "The float stays serenely still"]

def cast():
    print "You cast your line into the water."
    from random import choice
    choice(line_cast)
    if choice(line_cast) == "The float bobs down slightly":
        option = raw_input("What do you do?  Reel it in, Pull back, Wait, Drink a beer")
        if raw_input == "Pull back":
            print "You hooked a fish!"
        elif raw_input == "Drink a beer":
            print "Well, you didn't catch a fish, but at least you're goofing off."
        elif raw_input != ("Pull back", "Drink a beer"):
            print "Whatever it was, it seems to have gotten away."

    elif choice(line_cast) == "The float disappears under the water":
        print "You've got a bite!"
        option = raw_input("What do you do?")
        if raw_input == "Reel it in":
            print "You got a fish, he's a fighter!"

        elif raw_input == "Drink a beer":
            print "Well, you didn't catch a fish, but at least you're goofing off."
        elif raw_input != ("Reel it in", "Drink a beer"):
            print "The fish got off away . . ."

menu_item = 0
while menu_item !=("Q"):
    print "Where would you like to fish?  At the Lake, the River, or the Beach?"
    print "To quit, press Q."
    menu_item = raw_input("Pick an option: ")

    if menu_item == ("Lake"):
        cast_choice = raw_input("Cast? Y/N? ")
        if cast_choice != "Y":
            print "You take a moment to relax on this fine day."

        if cast_choice == "Y":
            cast

        #from random import choice
        #if choice(lake_fish) == "Old Boot":
        #    print "Oh . . . it was just an old boot . . ."

        #else:
        #    print "You caught a", choice(lake_fish),"!"

    #elif menu_item == ("River"):
    #    from random import choice
    #    print "You caught a ", choice(river_fish), "!"
        
    #elif menu_item == ("Beach"):
    #    from random import choice
    #    print "You caught a ", choice(beach_fish), "!"
            
print "Goodbye."
