#! /usr/bin/env python
#This is an interesting bit of code I found - I did not write it - that tracks the location of the mouse and
#prints the coordinates.  I think this code could be a basis in the future of having the game react to movements
#of the mouse instead of simply commands. IE, you'd move your mouse back to simulate pulling the rod back, maybe 
#rotate the wheel to simulate reeling it in.
 
import pygame

x = y = 0
running = 1
screen = pygame.display.set_mode((640, 400))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEMOTION:
        print "mouse at (%d, %d)" % event.pos

    screen.fill((0, 0, 0))
    pygame.display.flip()
