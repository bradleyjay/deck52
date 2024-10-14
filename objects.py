import pdb
import random
from ui import Draw

class Card:
    def __init__(self, rank=None, suit=None):
        self.rank = rank
        self.suit = suit

    # def print(self):
    def __str__(self):
        # print(self.rank, self.suit)
        return f'{self.rank}, {self.suit}'

class Hand:
    def __init__(self):
        self.hand = []
        # self.deck = deck
        self.handsize = 7
        # self.draw_starting_hand()

    def draw_starting_hand(self):
        for i in range(0, self.handsize):
            Draw.select(self)

    def fan(self):
        
        i = 0
        print("---- Hand ----")
        for card in self.hand:

            # print(card.rank, card.suit)
            print(f'{i}) {card}')
            i += 1
            # print(str(card))
            # card.print()
        # else:
        #     print("self.hand empty")

class Deck:
    def __init__(self):
        self.cards = []
        self._populate_deck()
        self.discard_pile = []

    def _populate_deck(self):
        # pdb.set_trace()
        for suit in ['hearts', 'clubs','spades','diamonds']:
            for rank in range(2,11): # range is non-inclusive
                
                self.cards.append(Card(rank, suit))
                # self.cards.append(['test'])
            for rank in ['J', 'Q', 'K', 'A']:
                self.cards.append(Card(rank, suit))
        self.shuffle()
        print("populated!")
    def print(self):
        if self.cards:
            for card in self.cards:
                print(card.rank, card.suit)
        else:
            print("self.cards empty.")

    def fan(self):
        print("---- Deck List ----")
        for card in self.cards:
            print(card)

    def show_discard(self):
        print("---- Discard Pile ----")
        for card in self.discard_pile:
            print(card)

    def shuffle(self):
        # generate list of random numbers 0-51
        # set index of each card to that index
        # return deck
        random.shuffle(self.cards)

