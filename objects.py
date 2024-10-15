import pdb
import random
from ui import Draw
from ascii_engine import ascii_printer

class Card:
    def __init__(self, rank=None, suit=None):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank}, {self.suit}'

class Hand:
    def __init__(self):
        self.hand = []
        self.handsize = 5

    def fan(self):
        
        i = 0
        print("---- Hand ----")
        for card in self.hand:
            print(f'{i}) {card}')
            i += 1
        ascii_printer(self.hand)

class Deck:
    def __init__(self):
        self.cards = []
        self._populate_deck()
        self.discard_pile = []

    def _populate_deck(self):
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
        random.shuffle(self.cards)

