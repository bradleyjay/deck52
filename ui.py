import pdb
import os

class Menu:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand
        self.options = [
            Draw(self.deck, self.hand),
            Play(self.deck, self.hand), 
            Discard(self.deck, self.hand),
            PickCards(self.deck, self.hand)
        ]

        

    def display_menu(self):
        # print(self.options)
        i = 0
        for option in self.options:
            print(f'{i}) {option}')
            i+=1

    def select(self, option):
        # if str(option) in self.options:
        #     option.select()
        # else:
        #     print("Invalid entry")
        if option < len(self.options):
            self.options[option].select()
        
    


        
class PickCards:

    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand

    def select(self):
        # choice = int(input("Discard card - which one? Enter number"))
        # # discarded_cards = self.hand.hand[choice]
        # discarded_cards = self.hand.hand.pop(choice)
        # self.deck.discard_pile.append(discarded_cards)
        selection = []
        choice = 1
        
        while choice != '9':
            os.system('clear')
            
            self.hand.fan()
            print("---- Selected Cards ----")
            for card in selection:
                print(card)

            choice = input('Select cards. Enter number to add, y to confirm, c to cancel.')
            if choice == 'y':
                break
            elif choice == 'c':
                return 0
            else:
                selection.append([int(choice), self.hand.hand[int(choice)]])

        print(f'Selected cards: {selection}')
        return selection
        input()

    def __str__(self):
        return 'Pick Cards'  


class Draw:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand

    def select(self):
        # pdb.set_trace()
        drawn_card = self.deck.cards.pop(0)  # TODO: this is awful naming, fix this
        
        print(f"I drew {drawn_card}")
        self.hand.hand.append(drawn_card)

    def __str__(self):
        return 'Draw'

class Play:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand

    def select(self):
        picker = PickCards(self.deck, self.hand)
        # selection = PickCards.select()
        selection = picker.select()
        print(f'Selection: {selection}')
        input("Hand score check")
        print(self.ispokerhand(selection))
        input("PAKTC") #press any key to continue

    def ispokerhand(self):
        
        ## hand ranks:
        # royal flush
        # straight flush
        # four of a kind
        # full house
        # flush
        # straight
        # three of a kind
        # two pair
        # pair
        # high card

        # things to check:
        # - count of each rank
        # - is flush
        # - is straight

    def rank_count(self, selection):
        # two ways to do this - either you tally cards by rank, then create dict for checking 4 of 3 of etc hands
        # or, dict first, but populating the dict requires tallying all 13 ranks first
        # TODO: START HERE TOMORROW
        
        count_dict = {4:[], 3: [], 2:[], 1:[]}
        for card in selection:




    def __str__(self):
        return 'Play [WIP]'


class Discard:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand
        
    def select(self):
        choice = int(input("Discard card - which one? Enter number"))
        # discarded_cards = self.hand.hand[choice]
        discarded_cards = self.hand.hand.pop(choice)
        self.deck.discard_pile.append(discarded_cards)
        
        input(f"I discarded {discarded_cards}")

    def __str__(self):
        return 'Discard'


        
