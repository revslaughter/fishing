#These three lists are just fish found in those locales.
lake_fish = ["Brown Trout", "Rainbow Trout", "Lake Trout", "Largemouth Bass", "Black Crappie", "Tench", "Common Carp", "Roach", "Common Bream", "Rudd",
"Wels Catfish", "Blue Catfish", "Channel Catfish", "Zander", "European Perch"]

river_fish = ["Brown Trout", "Rainbow Trout", "Largemouth Bass", "White Crappie", "Barbel", "European Chub", "Wels Catfish", "Blue Catfish", "Channel Catfish", "Zander", "Striped Bass", "Gray Mullet"]

beach_fish = ["Sea Trout", "Steelhead", "Ling", "Coalfish", "Pollack", "Sea Bass", "Conger Eel", "Ballan Wrasse", "Red Drum", "Black Drum", "Bull Huss", "Winter Flounder", "European Plaice", "Turbot", "Striped Bass", "Gray Mullet", "Black Seabream", "Common Skate", "Blonde Ray", "Bluefish", "Tarpon"]

size = ["tiny", "small", "average-sized", "large", "giant"]

menu_item = 0
while menu_item !=("Q"):
    print "Where would you like to fish?  At the Lake, the River, or the Beach?"
    print "To quit, press Q."
    menu_item = raw_input("Pick an option: ")
#Okay, so there's not much gameplay atm.  It just picks a random fish.  I'm working on adding some gameplay elements.
    if menu_item == ("Lake"):
        from random import choice
        print "You caught a", choice(size), choice(lake_fish), "!"

    elif menu_item == ("River"):
        from random import choice
        print "You caught a", choice(size), choice(river_fish), "!"
        
    elif menu_item == ("Beach"):
        from random import choice
        print "You caught a", choice(size), choice(beach_fish), "!"
     
print "Goodbye."
