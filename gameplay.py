import random
# Variables
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
player_hand = []
dealer_hand = []


def build(values, suites):
    """
    Creates the deck for the game
    :param values: Uses the cards list
    :param suites: Uses the suites list
    :return: The deck
    """
    deck = []
    for suite in suites:
        for value in values:
            deck.append([value, suite])
    return deck


# Creating the deck
deck = build(cards, suites)
random.shuffle(deck)
print(deck)


# Define a function to calculate the hand value, considering the possibility of aces
def calculate_hand_value(hand):
    value = sum([values[str(card[0])] if card[0] in values.keys() else card[0] for card in hand])
    aces = [card for card in hand if card[0] == 'A']
    while value > 21 and aces:
        value -= 10
        aces.pop()
    return value


def deck_reset(new_deck):
    """
    Clears each hand and shuffles the cards back in to the deck
    :return: The new deck
    """
    player_hand.clear()
    dealer_hand.clear()
    new_deck.clear()
    new_deck = build(cards, suites)
    random.shuffle(new_deck)
    return new_deck


def player_start():
    """
    Give player 2 cards for start of round
    :return: The player hand (two cards)
    """
    player_hand.append(deck[0])
    del deck[0]
    player_hand.append(deck[0])
    del deck[0]
    print(player_hand)


def dealer_start():
    """
    Give the dealer 2 cards for start of round
    :return: The dealer hand (two cards)
    """
    dealer_hand.append(deck[0])
    del deck[0]
    dealer_hand.append(deck[0])
    del deck[0]
    return dealer_hand


def hit_and_stand():
    """
    For player to input hit or stand, then do the thing that they want
    :return: Player value
    """
    while True:
        hit_stand = input("Would you like to (Hit or Stand): ")
        if hit_stand.title() == 'Hit':
            cardactive1 = deck[0]
            player_hand.append(cardactive1)
            print(player_hand)
            deck.remove(cardactive1)
            player_value = calculate_hand_value(player_hand)
            print(player_value)
        elif hit_stand.title() == 'Stand':
            player_value = calculate_hand_value(player_hand)
            break
        else:
            print("Please enter a valid word\n")
    return player_value


def dealer_action(value):
    if value == 21:
        return "win"
    elif 1 <= value <= 16:
        return "hit"
    elif 17 <= value < 21:
        return "stand"
    else:
        return "bust"


def dealer_move(action):
    if action == 'win':
        print("Dealer Wins")
    elif action == 'hit':
        print("It's a Hit!")
    elif action == 'stand':
        print("It's a Stand!")
    else:
        print("It's a bust")


def score_check(player_value, dealer_value):
    dealer_score = 0
    player_score = 0

    if player_value >= 22:
        dealer_score += 1
        print("Player Bust, Dealer Wins Round")
    elif dealer_value >= 22:
        player_score += 1
        print("Dealer Bust, Player Wins Round")
    elif player_value < dealer_value:
        dealer_score += 1
        print("Dealer Wins Round")
    elif dealer_value < player_value:
        player_score += 1
        print("Player Wins Round")
    else:
        dealer_score += 1
        print("Tie, Dealer Wins")


def rounds():
    # Start of the round
    player_start()
    dealer_start()
    # Asking player if they want to hit or stand
    hit_and_stand()
    # Once player stands or busts, dealer makes their moves
    move = dealer_action(21)
    dealer_move(move)
    # After the dealer is done, check the scores
    score_check(21, 21)


def play_again():
    # If they want to play again
    play = input('do you wan to play (yes, no): ')
    # deck reset
    if play == 'yes':
        global deck
        deck = deck_reset(deck)
        rounds()


rounds()
