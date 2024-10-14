import pdb
import os
import logging

log = logging.getLogger(__name__)

class Menu:
    def __init__(self, deck, hand):
        self.deck = deck
        self.hand = hand
        self.options = [
            # Draw(self.deck, self.hand),
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

    def __init__(self, deck, hand, mode=None):
        self.deck = deck
        self.hand = hand
        self.mode = mode

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
                print(f'{card[0]}), {card[1]}')

            choice = input(f'Select cards to {self.mode}. Enter number to add, y to confirm, c to cancel.')
            if choice == 'y':
                break
            elif choice == 'c':
                return 0
            else:
                selection.append([int(choice), self.hand.hand[int(choice)]])

        # print(f'Selected cards: {selection}')
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
        
        # print(f"I drew {drawn_card}")
        self.hand.hand.append(drawn_card)

    def redraw_to_handsize(self):
        cards_missing = self.hand.handsize - len(self.hand.hand)
        if cards_missing > 0:
            # pdb.set_trace()
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
        # selection = PickCards.select()
        selection = picker.select()
        # print(f'Selection: {selection}')

        # check poker hand
        print(self.ispokerhand(selection))
        input("Continue...")

        # redraw played cards
        discarded_cards = Discard.discard_played_cards(self, selection)
        input(f"Re-drawing {discarded_cards} cards...")
        # for i in range(0,discarded_cards):
        #     Draw.select(self)

    def ispokerhand(self, selection):
        
        # call your rank count, flush check, straight check results, then start going though hands...
        rank_tally, X_of_a_kind = self._rank_count(selection)
        flush = self._flush_check(selection)
        straight, selection_sorted = self._straight_check(selection)

        high_card = selection_sorted[-1]
        
        ## hand ranks:
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
        # two ways to do this - either you tally cards by rank, then create dict for checking 4 of 3 of etc hands
        # or, dict first, but populating the dict requires tallying all 13 ranks first
        
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
            # pdb.set_trace()
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

            # print(f"card: {card}, straight_counter: {straight_counter}")
            # input()
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
        selection = picker.select()
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


        
