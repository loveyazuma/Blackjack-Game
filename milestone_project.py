import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # empty list that will hold the cards
        self.value = 0  # start with a value of zero
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        #   track the aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        #   if total value is greater than 21 and the player has an ace then change the ace to a 1
        while self.value > 21 and self.aces:
            #   subtract 10 from the total value
            self.value -= 10
            #   remove one ace from the hand of the player
            self.ace -= 1

#
# test_deck = Deck()
# test_deck.shuffle()
#
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# print(test_player.value)
