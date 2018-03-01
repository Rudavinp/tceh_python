import random


SUITS = ('D', 'C', 'S', 'H')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')


class Deck(object):
    def __init__(self):
        self.deck_cards = []
        for v in VALUES:
            for s in SUITS:
                self.deck_cards.append(v + s)

    def shuffle_deck(self):
        random.shuffle(self.deck_cards)
        return self.deck_cards

    def give_out_cards(self, hand, max_size):
        while len(hand) != max_size:
            card = random.choice(self.deck_cards)
            hand.append(card)
            self.deck_cards.remove(card)
        return hand


class Hand(object):
    def __init__(self, max_cards):
        self.max_cards = max_cards
        self.cards_on_hand = []

    def print_cards(self):
        for card in self.cards_on_hand:
            print(card, end=' ')


deck = Deck()
print(deck.shuffle_deck())
hand = Hand(5)
deck.give_out_cards(hand.cards_on_hand, hand.max_cards)
hand.print_cards()
