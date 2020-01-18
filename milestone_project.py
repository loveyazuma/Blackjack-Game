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
        while self.value > 21 and self.aces:  # self.aces is the same as self.aces > 0
            #   subtract 10 from the total value
            self.value -= 10
            #   remove one ace from the hand of the player
            self.ace -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Please, input an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry you cannot exceed', chips.total)
            else:
                break


def hit(deck, hand):
    #   takes a single card
    single_card = deck.deal()
    #   Adds it to the player's hand
    hand.add_card(single_card)
    #   adjusts for ace
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def player_busts(player, dealer, chips):
    print('BUST PLAYER')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('PLAYER WINS')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('DEALER WINS')
    chips.lose_bet()


def dealer_wins(player, dealer, chips):
    print('DEALER WINS')
    chips.win_bet()


def push(player, dealer):
    print('Dealer and Player tie!!! PUSH')


def show_some(player, dealer):
    print("\n Dealer'd Hand:")
    print(" <card hidden> ")
    print('', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n')


def show_all(player, dealer):
    print("\n Dealer'd Hand:", *dealer.cards, sep='\n')
    print("\n Dealer'd Hand = ", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


#   --------------------------- PLAY GAME------------------------------
while True:
    print('WELCOME TO BLACKJACK')
    #   Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #   Set up the Player's Chips
    player_chips = Chips()

    #   Prompt the player for their bet
    take_bet(player_chips)

    #   Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # prompt the player to hit or stand
        hit_or_stand(deck, player_hand)

        # Show the cards
        show_some(player_hand, dealer_hand)

        #   If player's exceed 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        #   If the player has not busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            #   Show all cards
            show_all(player_hand, dealer_hand)

            #   Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print('\n Player total chips are {}'.format(player_chips.total))

        #   Ask to play again
        new_game = input('Would you like to play another hand? y/n')

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print('Thank you for playing')
            break

