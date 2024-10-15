import pdb
import os
import logging
import sys

log = logging.getLogger(__name__)

class Menu:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand
        self.options = [
            Play(self.deck, self.hand), 
            Discard(self.deck, self.hand),
            Util()
        ]

        

    def display_menu(self):
        # print(self.options)
        i = 0
        for option in self.options:
            print(f'{i}) {option}')
            i+=1

    def select(self, option):
        # when menu selection made, call chosen method
        if option < len(self.options):
            self.options[option].select()
        
    
class Util:
    def select(self):
        choice = input("Thanks for playing!")
        sys.exit()

    def __str__(self):
        return 'Quit Game'  

        
class PickCards:

    def __init__(self, deck, hand, mode=None):
        self.deck = deck
        self.hand = hand
        self.mode = mode

    def select(self, selection_maximum):
        selection = []
        choice = 1 # dummy start value
        
        while 1:
            os.system('clear')
            
            self.hand.fan()
            print("---- Selected Cards ----")
            for card in selection:
                print(f'{card[0]}), {card[1]}')

            choice = input(f'Select cards to {self.mode}. Enter number to add, y to confirm, c to cancel.')

            # confirm response valid
            valid_responses = ['0', '1','2','3','4','5','6', 'y', 'c']
            if choice not in valid_responses:
                input(f"Invalid entry.") 
            elif choice == 'y':
                break
            elif choice == 'c':
                return []
            else:
                # dupe check
                dupe = False
                for card in selection:
                    if self.hand.hand[int(choice)] == card[1]:
                        dupe = True
                        
                if dupe == True:
                    input("Invalid, already selected. Choose again.")
                # out-of-range error
                elif len(selection) > selection_maximum - 1:
                    input(f"Invalid, you may only select {selection_maximum} cards.") 
                else:
                    # no issues? Append to selection dict
                    selection.append([int(choice), self.hand.hand[int(choice)]])

        return selection
        input()

    def __str__(self):
        return 'Pick Cards'  


class Draw:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand

    def select(self):
        # check cards remain in deck
        if len(self.deck.cards) < 1:
            Util.select()
        
        # else, draw card
        drawn_card = self.deck.cards.pop(0)  # TODO: this is awful naming, fix this
        self.hand.hand.append(drawn_card)

    def redraw_to_handsize(self):
        # calc cards to draw
        cards_missing = self.hand.handsize - len(self.hand.hand)

        # draw cards
        if cards_missing > 0:
            for i in range(0, cards_missing):
                self.select()

    def __str__(self):
        return 'Draw'

class Play:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand

    def select(self):
        picker = PickCards(self.deck, self.hand, "play")
        selection = picker.select(5)
        if not selection:
            input("I played 0 cards...")
            return

        # check poker hand
        print(self.ispokerhand(selection))
        input("Continue...")

        # redraw played cards
        discarded_cards = Discard.discard_played_cards(self, selection)
        input(f"Re-drawing {discarded_cards} cards...")

    def ispokerhand(self, selection):
        
        # call your rank count, flush check, straight check results
        rank_tally, X_of_a_kind = self._rank_count(selection)
        flush = self._flush_check(selection)
        straight, selection_sorted = self._straight_check(selection)

        high_card = selection_sorted[-1]
        
        # check status against each hand
        # royal flush
        if straight == True and flush == True and rank_tally["A"] > 0 and rank_tally ["K"] > 0:
            return "Royal Flush"

        # straight flush
        elif straight == True and flush == True:
            return "Straight Flush, {high_card} high"
        
        # four of a kind
        elif X_of_a_kind["4"]:
            X = X_of_a_kind["4"][0]
            return f"Four of a Kind: {X}s"
        # full house
        elif X_of_a_kind["3"] and X_of_a_kind["2"]:
            X1 = X_of_a_kind["3"][0]
            X2 = X_of_a_kind["2"][0]
            return f"Full House: {X1}s and {X2}s"
        # flush
        elif flush == True:
            return "Flush, {high_card} high"
        # straight
        elif straight == True:
            return "Straight, {high_card} high"
        # three of a kind
        elif X_of_a_kind["3"]:
            X = X_of_a_kind["3"][0]
            return f"Three of a Kind: {X}s"
        # two pair
        elif len(X_of_a_kind["2"]) > 1:
            X1 = X_of_a_kind["2"][0]
            X2 = X_of_a_kind["2"][1]
            return f"Two Pair: {X1}s and {X2}s"
        # pair
        elif (X_of_a_kind["2"]):
            X = X_of_a_kind["2"][0]
            return f"Pair: {X}s"
        # high card
        else:
            return f"High Card: {high_card}"

    def _rank_count(self, selection):        
        rank_tally = {
            "A": 0,
            "K": 0,
            "Q": 0,
            "J": 0,
            "10": 0,
            "9": 0,
            "8": 0,
            "7": 0,
            "6": 0,
            "5": 0,
            "4": 0,
            "3": 0,
            "2": 0,
        }

        # pdb.set_trace()
        for card_in_hand in selection:
            rank_tally[str(card_in_hand[1].rank)] += 1

        X_of_a_kind = {'4': [], '3': [], '2': []}
        for rank in rank_tally:
            if rank_tally[rank] == 4:
                X_of_a_kind['4'].append(rank)
            elif rank_tally[rank] == 3:
                X_of_a_kind['3'].append(rank)
            elif rank_tally[rank] == 2:
                X_of_a_kind['2'].append(rank)
        return rank_tally, X_of_a_kind

    def _flush_check(self, selection):
        if len(selection) < 4:
            return False
        else:
            suit = None
            for card_in_hand in selection:
                if suit is None:
                    suit = str(card_in_hand[1].suit)
                elif suit != str(card_in_hand[1].suit):
                    return False
            return True





    def _straight_check(self, selection):
        numbered_cards = [2,3,4,5,6,7,8,9,10]
        face_and_ace = ['J','Q','K','A']
        numbers = []
        not_numbers = []

        # unpack
        for card_in_hand in selection:
            this_card = card_in_hand[1].rank
            if this_card not in face_and_ace:
                numbers.append(int(this_card))
            else:
                not_numbers.append(this_card)

        # sorting
        sorted_numbers = sorted(numbers)

        # check each non-number card, append in ascending order
        sorted_not_numbers = []
        for mark in face_and_ace:
            for card in not_numbers:
                if card == mark:
                    sorted_not_numbers.append(card)

        # pdb.set_trace()
        selection_sorted = sorted_numbers + sorted_not_numbers
        if len(selection) < 4:
            return False, selection_sorted

        all_cards = numbered_cards + face_and_ace

        straight_counter = 0

        for i, card in enumerate(selection_sorted):
            if straight_counter == 0:
                straight_counter += 1
            else:
                # find correct card in all_cards 
                for j, mark in enumerate(all_cards):
                    if mark == card:
                        # found index? Exit loop
                        break

                if all_cards[j-1] == selection_sorted[i-1]:
                    straight_counter += 1
                else:
                    straight_counter = 0

        if straight_counter == 5:
            return True, selection_sorted
        else:
            return False, selection_sorted


    def __str__(self):
        return 'Play'


class Discard:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand
        
    def select(self):
        picker = PickCards(self.deck, self.hand, "discard")
        # selection = PickCards.select()
        selection = picker.select(7)
        discarded_cards = self.discard_played_cards(selection)

        # choice = int(input("Discard card - which one? Enter number"))
        # discarded_cards = self.hand.hand[choice]
        # discarded_cards = self.hand.hand.pop(choice)
        # self.deck.discard_pile.append(discarded_cards)
        
        input(f"\nI discarded {discarded_cards} cards.")

    def discard_played_cards(self, selection):
        discarded_count = 0
        # pdb.set_trace()
        for card in selection:
            # find card in hand
            for i, card_in_hand in enumerate(self.hand.hand):
                # discard card
                if card[1] == card_in_hand:
                    discarded_card = self.hand.hand.pop(i)
                    print(f"Discarding {discarded_card}")
                    discarded_count += 1

        return discarded_count

    def __str__(self):
        return 'Discard'


        
