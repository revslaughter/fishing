#This is not functioning code.  This is just a list of very simple concepts I wrote down when I was tired for the
#future of this game.  I wanted to add a true/false value to having caught or lost a fish.  True would add +1 to a
#count, while false adds 0.  You start at the easiest form of fishing and move up when you land enough fish to have 
#enough points.  There'll be a simple check when you select each level, to see if your score >= to the requirement.
#At each higher level you will get more impressive fish, and they will have new methods of fighting, like jumping
#or hiding.
#I meant to add this, but I also wanted to add a list that will be drawn from randomly for the size.  That way you
#can actually try to land that "giant" catfish or whatever.  That will be just random, of course.

option = raw_input("The fish seems tired . . .")
if option == "Reel it in":
    print "Good job!"
elif option != "Reel it in":
    print ". . . it got away."

print "Pick Your Level:"
print "Pond Fishing"
print "Requirement: 0"
print
print "River Fishing"
print "Requirement: 1"
print
print "Beach Fishing"
print "Requirement: 2"
print
print "Ocean Fishing"
print "Requirement: 3"
print
print "Monster Fishing"
print "Requirement: 4"

#fish seems tired, nibble, bite, running, hiding, jumping, line snagged

def fish_bite:


def fish_nibble:


def fish_run:
    

def fish_tired:
    print "The fish seems tired . . ."
    option = raw_input("What now? ")
    if option == ("Reel it in")
        print "Good job!"
    elif option != ("Reel it in")
        print ". . . it got away."
