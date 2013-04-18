#This was originally intended to be a definition, but it wasn't working properly . . .  It's just printing 
#the choice and not giving the further options.  The "while" near the top was to hopefully make a loop.

#My goal if this worked was to then have it go into a new definition that functioned similarly, wherein 
#the fish did such actions as run, get tired, jump, et cetera, and you would have to react appropriately, 
#otherwise the fish would get away.  At its most basic it'd a be a trial-and-error memory game, but that's
#about the limit of my ability atm, though I have some thoughts for interesting ideas in the future.

from random import choice

bobs = "The float bobs down slightly"
dunks = "The float disappears under the water"
still = "The float stays serenely still"

reel = "Reel it in"
pull = "Pull back"
beer = "Drink a beer"

line_cast = [bobs, dunks, still]
bob_choices = [reel, pull, beer]

while choice(line_cast) == (bobs, dunks, still):
    print "You cast your line into the water."
    print choice(line_cast)

    if choice(line_cast) == bobs:
        option = raw_input("What do you do?  Reel it in, Pull back, Wait, or Drink a beer? ")
        if raw_input == pull:
            print "You hooked a fish!"
        elif raw_input == beer:
            print "Well, you didn't catch a fish, but at least you're goofing off."
        elif raw_input != (pull, beer):
            print "Whatever it was, it seems to have gotten away."

    elif choice(line_cast) == dunks:
        print "You've got a bite!"
        option = raw_input("What do you do?")
        if raw_input == reel:
            print "You got a fish, he's a fighter!"
        elif raw_input == beer:
            print "Well, you didn't catch a fish, but at least you're goofing off."
        elif raw_input != (reel, beer):
            print "The fish got away . . ."
    while choice(line_cast) == still:
        print ". . ."
