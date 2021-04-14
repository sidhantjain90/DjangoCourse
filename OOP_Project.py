#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("New ordered deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling the deck")
        shuffle(self.allcards)

    def split(self):
        print("Splitting the deck in half")
        return (self.allcards[:26], self.allcards[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        print("Player {} created".format(self.name))

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def Check_Card(self):
        """
        Return True if Player still has cards left
        """
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!


# 1. Take a deck of Cards
d = Deck()

# 2. Shuffle them
d.shuffle()

# 3. Split in half
half1, half2 = d.split()

# 4. Create Players
comp = Player("P1", Hand(half1))   # Computer
user = Player("P2", Hand(half2))   # User

total_rounds = 0
war_count = 0

#Loop until one of the two runs out of cards
while user.Check_Card() and comp.Check_Card():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings")
    print(user.name +"has the count: "+str(len(user.hand.cards)))
    print(comp.name +"has the count: "+str(len(comp.hand.cards)))
    print("play a card!")
    print("\n")


    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()


    table_cards.append(c_card)
    table_cards.append(p_card)

    # Check for War
    if c_card[1] == p_card[1]:   #Comp card ranking vs user card ranking
        war_count += 1

        print("War!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game Over, number of rounds: "+str(total_rounds))
print("a war happened " + str(war_count)+ " times")

print("Does computer has cards? {}".format(str(comp.Check_Card())))

print("Does user has cards? {}".format(str(user.Check_Card())))
