# to do:

# deck object
#  - methods: shuffle, draw
# hand object
#  - methods: play, discard
# Somewhere: score evaluation, card ranking
# card object
# UI menu

# PoV: have a deck, have a hand, play cards into void, redraw to keep handsize = 7

import pdb
from objects import Deck, Hand
from ui import Menu
import os


mydeck = Deck()
myhand = Hand()
game_menu = Menu(mydeck, myhand)
# mydeck._populate_deck()
# print(mydeck)
# mydeck.fan()
# print(mydeck.cards[1].rank)
# print(mydeck.cards[1].suit)

# mydeck.draw(myhand)
# print(f"myhand: {myhand}")

# Game loop

os.system('clear')
input(
    "\n\n\n\n " +
    "###################################\n " +
    "############# DECK 52 #############\n " + 
    "###################################\n\n " +
    "    Press any key to continue")
while 1:
    # pdb.set_trace()
    os.system('clear')
    print("***   Enter number to act:   ***\n")
    game_menu.display_menu()
    # pdb.set_trace()
    myhand.fan()
    # mydeck.show_discard()
    
    # choice = int(input("\n\nEnter number to act:\n"))
    choice = int(input())
    game_menu.select(choice)
    

