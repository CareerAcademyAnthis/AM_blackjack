import random
import ui
# Variables
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suites = ["♥", "♦", "♣", "♠"]
values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
player_hand = []
dealer_hand = []
player_split_1 = []
player_split_2 = []
dealer_score = 0
player_score = 0
round_points = 1
pushes = 0


print("★☆☆☆☆☆BLACK-JACK☆☆☆☆☆★")
print("rules: \n"
      "★. Dealer will stand on all 17s\n"
      "★. Guests may only split once\n"
      "★. Guests may only split with equal cards\n"
      "★. Guests can double down on any two cards\n"
      "★. If player gets more than 21 busts\n"
      "★. if player and dealer push dealer wins\n"
      "★. ages 14 and above to play\n"
      "★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆")
name = input("name: ")
while True:
    try:
        age = int(input("age: "))
        break
    except ValueError:
        print("That is not an age. Try again")
if age <= 13:
    quit()


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
    player_split_1.clear()
    player_split_2.clear()
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
    #if player_hand[0][0] == player_hand[1][0]:
       #option = input("Would you like to split? ")
        #if option.lower() in ["yes", "y"]:
    """gameplay does the rest"""
            #player_split_1 = []
            #player_split_2 = []
    if x == 'J' or x == "Q" or x == "K":
        x = 10
    if x == 'A':
        x = 11
    if y == 'J' or y == "K" or y == "Q":
        y = 10
    if y == 'A':
        y = 11

    if x != y:
        print("Sorry, you can't split")

    player_split_1.append(player_hand[0])
    player_split_2.append(player_hand[1])
    print(player_split_1)
    print(player_split_2)
            #return player_split_1, player_split_2


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
    hit_counter = 0
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value >= 21:
            break
        hit_stand = input("Would you like to (Hit or Stand): ")
        if hit_stand.title() == 'Hit':
            hit_counter += 1
            cardactive1 = deck[0]
            player_hand.append(cardactive1)
            deck.remove(cardactive1)
            if hit_counter == 1:
                ui.player_hand_1hit(player_hand)
            elif hit_counter == 2:
                ui.player_hand_2hit(player_hand)
            elif hit_counter == 3:
                ui.player_hand_3hit(player_hand)
            elif hit_counter == 4:
                ui.player_hand_4hit(player_hand)
            elif hit_counter == 5:
                ui.player_hand_5hit(player_hand)
            elif hit_counter == 6:
                ui.player_hand_6hit(player_hand)
        elif hit_stand.title() == 'Stand':
            player_value = calculate_hand_value(player_hand)
            break
        else:
            print("Please enter a valid word\n")
    return player_value


def hit_and_stand_split_version(hand):
    """
    For player to input hit or stand, then do the thing that they want
    :return: Player value
    """
    hit_counter = 0
    while True:
        player_value = calculate_hand_value(hand)
        if player_value >= 21:
            break
        hit_stand = input("Would you like to (Hit or Stand): ")
        if hit_stand.title() == 'Hit':
            hit_counter += 1
            cardactive1 = deck[0]
            hand.append(cardactive1)
            deck.remove(cardactive1)
            if hit_counter == 1:
                ui.player_hand_1hit(hand)
            elif hit_counter == 2:
                ui.player_hand_2hit(hand)
            elif hit_counter == 3:
                ui.player_hand_3hit(hand)
            elif hit_counter == 4:
                ui.player_hand_4hit(hand)
            elif hit_counter == 5:
                ui.player_hand_5hit(hand)
            elif hit_counter == 6:
                ui.player_hand_6hit(hand)
        elif hit_stand.title() == 'Stand':
            player_value = calculate_hand_value(hand)
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
        ui.starting_dealer_hand(True, dealer_hand)
    else:
        pass


def score_check(player_value, dealer_value):
    global dealer_score
    global player_score
    global pushes
    print(f'Dealer hand is {dealer_value}.')
    print(f'Your hand is {player_value}.')

    if player_value >= 22 and dealer_value <= 21:
        dealer_score += 1
        print("You Busted, Dealer Wins Round")
    elif dealer_value >= 22 and player_value <= 21:
        player_score += round_points
        print("Dealer Bust, Player Wins Round")
    elif player_value > 21 and dealer_value > 21:
        pushes += 1
        print("It's a push. No points.")
    elif player_value < dealer_value:
        dealer_score += 1
        print("Dealer Wins Round")
    elif dealer_value < player_value:
        player_score += round_points
        print("Player Wins Round")
    else:
        dealer_score += 1
        print("Tie, Dealer Wins!")

def score_check_split(player_value_1, player_value_2, dealer_value):
    global dealer_score
    global player_score
    global pushes
    print(f'Dealer hand is {dealer_value}.')
    print(f'Your frist hand is {player_value_1}.')
    print(f'Your second hand is {player_value_2}.')

    if player_value_1 >= 22 and dealer_value <= 21:
        dealer_score += 1
        print("You Busted, Dealer Wins Round!")
    elif dealer_value >= 22 and player_value_1 <= 21:
        player_score += round_points
        print("Dealer Busted, You Won the Round!")
    elif player_value_1 > 21 and dealer_value > 21:
        pushes += 1
        print("It's a push. No points.")
    elif player_value_1 < dealer_value:
        dealer_score += 1
        print("Dealer Wins Round!")
    elif dealer_value < player_value_1:
        player_score += round_points
        print("You Won the Round!")
    else:
        dealer_score += 1
        print("Tie, Dealer Wins!")

    if player_value_2 >= 22 and dealer_value <= 21:
        dealer_score += 1
        print("You Busted, Dealer Wins Round!")
    elif dealer_value >= 22 and player_value_2 <= 21:
        player_score += round_points
        print("Dealer Bust, You Won the Round!")
    elif player_value_2 > 21 and dealer_value > 21:
        print("It's a push. No points.")
    elif player_value_2 < dealer_value:
        dealer_score += 1
        print("Dealer Wins Round!")
    elif dealer_value < player_value_2:
        player_score += round_points
        print("You Won the Round!")
    else:
        dealer_score += 1
        print("Tie, Dealer Wins!")

def rounds():
    spliting = False
    face_down = False
    # Start of the round
    dealer_start()
    ui.starting_dealer_hand(face_down, dealer_hand)
    player_start()
    ui.starting_player_hand(player_hand)
    # Double and split
    global round_points
    x = player_hand[0][0]
    y = player_hand[1][0]
    if x == 'J' or x == "Q" or x == "K":
        x = 10
    if x == 'A':
        x = 11
    if y == 'J' or y == "K" or y == "Q":
        y = 10
    if y == 'A':
        y = 11
    if x == y:
        split_input = input("Would you like to Split? (yes or no): ")
        if split_input.lower() in ['yes', 'y']:
            spliting = True
            split(player_hand[0][0], player_hand[1][0])
            ui.split_cards(player_split_1, player_split_2) # get return value later
            cardactive1 = deck[0]
            player_split_1.append(cardactive1)
            deck.remove(cardactive1)
            cardactive1 = deck[0]
            player_split_2.append(cardactive1)
            deck.remove(cardactive1)
            ui.starting_player_hand(player_split_1)
            player_value_1 = hit_and_stand_split_version(player_split_1)
            ui.starting_player_hand(player_split_2)
            player_value_2 = hit_and_stand_split_version(player_split_2)
        else:
            if double():
                round_points = 2
            else:
                round_points = 1
            # Asking player if they want to hit or stand
            player_value = hit_and_stand()
    else:
        if double():
            round_points = 2
        else:
            round_points = 1
        # Asking player if they want to hit or stand
        player_value = hit_and_stand()
    # Once player stands or busts, dealer makes their moves
    ui.starting_dealer_hand(True, dealer_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    move = dealer_action(dealer_value)
    dealer_move(move)
    dealer_hits = 0
    while dealer_value <= 16:
        dealer_value = calculate_hand_value(dealer_hand)
        dealer_hits += 1
        move = dealer_action(dealer_value)
        dealer_move(move)
        if dealer_hits == 1:
            ui.dealer_hand_1hit(dealer_hand)
        elif dealer_hits == 2:
            ui.dealer_hand_2hit(dealer_hand)
        elif dealer_hits == 3:
            ui.dealer_hand_3hit(dealer_hand)
        elif dealer_hits == 4:
            ui.dealer_hand_4hit(dealer_hand)
    # After the dealer is done, check the scores
    if dealer_value == 21:
        pass
    else:
        if spliting:
            score_check_split(player_value_1, player_value_2, dealer_value)
        else:
            score_check(player_value, dealer_value)
    play_again()


def play_again():
    # If they want to play again
    play = input('Do you want to play again? (yes, no): ')
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
ui.end_game(player_score, dealer_score, pushes)
