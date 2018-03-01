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
    def __init__(self, cards=None):
        if not cards:
            self.cards_on_hand = []
        self.cards_on_hand = cards

    def print_cards(self):
        for card in self.cards_on_hand:
            print(card, end=' ')
        print()


class Diller(object):
    def __init__(self, deck, max_size):
        self.deck = deck
        self.hand = []
        self.max_size = max_size

    def give_out_cards(self):
        while len(self.hand) != self.max_size:
            card = random.choice(self.deck)
            self.hand.append(card)
            self.deck.remove(card)
        return self.hand


class Win(object):
    def __init__(self, table, hand):
        self.table = table
        self.hand = hand
        self.hand_and_table = hand + table
        self.list_win_combs = []
        self.list_win_cards = []

    def chek_combination(self):
        n = 0
        while n != 7:
            f_card = self.hand_and_table[n]
            self.list_win_cards.append(f_card)
            for card in self.hand_and_table[n+1:]:
                if f_card[:-1] == card[:-1]:
                    self.list_win_cards.append(card)
            if len(self.list_win_cards) > 1:
                self.list_win_combs.append(self.list_win_cards.copy())
            self.list_win_cards.clear()
            n += 1

        if not self.list_win_combs:
            self.list_win_combs.append(self.hand)

        return self.list_win_combs


def main():
    play_deck = Deck().shuffle_deck()
    cards_player1 = Diller(play_deck, 2).give_out_cards()
    cards_player2 = Diller(play_deck, 2).give_out_cards()
    player1_hand = Hand(cards_player1)
    player1_hand.print_cards()
    player2_hand = Hand(cards_player2)
    player2_hand.print_cards()
    table_cards = Diller(play_deck, 5).give_out_cards()
    table = Hand(table_cards)
    table.print_cards()
    win_combs_player1 = Win(table_cards, cards_player1).chek_combination()
    win_combs_player2 = Win(table_cards, cards_player2).chek_combination()

    print('Best combinatons player1:')
    for combs in win_combs_player1:
        print(combs, end='')
    print()

    print('Best combinatons player2:')
    for combs in win_combs_player2:
        print(combs, end='')
    print()

if __name__ == '__main__':
    main()


