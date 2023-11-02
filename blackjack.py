import random
# Variables
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
player_hand = []
dealer_hand = []
dealer_score = 0
player_score = 0
round_points = 1
pushes = 0


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


def split(x, y):
    global round_points
    if player_hand[0][0] == player_hand[1][0]:
        option = input("Would you like to split? ")
        if option.lower() in ["yes", "y"]:
            """gameplay does the rest"""
            player_split_1 = []
            player_split_2 = []
            if x == 'J' or x == "Q" or x == "K":
                x = 10
            if x == 'A':
                x = 11
            if y == 'J' or y == "K" or y == "Q":
                y = 10
            if y == 'A':
                y = 11

            if x != y:
                print("Sorry you can't split")

            player_split_1.append(player_hand[0])
            player_split_2.append(player_hand[1])
            print(player_split_1)
            print(player_split_2)
        else:
            if double():
                round_points = 2
            else:
                round_points = 1


def double():
    asking = input("Would you like to double your bet: ")
    if asking.lower() == "yes":
        return True
    else:
        return False


def hit_and_stand():
    """
    For player to input hit or stand, then do the thing that they want
    :return: Player value
    """
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value >= 21:
            break
        hit_stand = input("Would you like to (Hit or Stand): ")
        if hit_stand.title() == 'Hit':
            cardactive1 = deck[0]
            player_hand.append(cardactive1)
            deck.remove(cardactive1)
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
    global dealer_score
    if action == 'win':
        dealer_score += 1
        print("Dealer has 21, Dealer Wins Round")
    elif action == 'hit':
        cardactive1 = deck[0]
        dealer_hand.append(cardactive1)
        deck.remove(cardactive1)
    elif action == 'stand':
        pass
    else:
        pass


def score_check(player_value, dealer_value):
    global dealer_score
    global player_score
    global pushes
    print(dealer_value)
    print(player_value)

    if player_value >= 22 and dealer_value <= 21:
        dealer_score += 1
        print("Player Bust, Dealer Wins Round")
    elif dealer_value >= 22 and player_value <= 21:
        player_score += round_points
        print("Dealer Bust, Player Wins Round")
    elif player_value > 21 and dealer_value > 21:
        print("It's a push. No points.")
    elif player_value < dealer_value:
        dealer_score += 1
        print("Dealer Wins Round")
    elif dealer_value < player_value:
        player_score += round_points
        print("Player Wins Round")
    else:
        dealer_score += 1
        print("Tie, Dealer Wins")


def rounds():
    # Start of the round
    player_start()
    dealer_start()
    # Double and split
    global round_points
    if player_hand[0][0] == player_hand[1][0]:
        split(player_hand[0], player_hand[1])
    else:
        if double():
            round_points = 2
        else:
            round_points = 1
    # Asking player if they want to hit or stand
    player_value = hit_and_stand()
    # Once player stands or busts, dealer makes their moves
    dealer_value = calculate_hand_value(dealer_hand)
    move = dealer_action(dealer_value)
    dealer_move(move)
    while dealer_value < 16:
        move = dealer_action(dealer_value)
        dealer_move(move)
        dealer_value = calculate_hand_value(dealer_hand)
    # After the dealer is done, check the scores
    if dealer_value == 21:
        pass
    else:
        score_check(player_value, dealer_value)
    play_again()


def play_again():
    # If they want to play again
    play = input('Do you want to play again (yes, no): ')
    # deck reset
    if play == 'yes':
        global deck
        deck = deck_reset(deck)
        rounds()
    elif play == 'no':
        pass
    else:
        print("\nEnter a correct value, you goof! ")
        play_again()


rounds()
