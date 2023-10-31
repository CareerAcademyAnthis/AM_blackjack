player_bust = True
dealer_bust = False


def dealer_action(card1, card2):
    value = card1 + card2
    if value == 21:
        return "Win"
    elif 1 <= value <= 14:
        return "Hit"
    elif 17 <= value < 21:
        return "Stand"
    else:
        dealer_bust = True
        return "Bust"


if player_bust == True and dealer_bust == True:
    print("It's a push. No points")

while True:
    cards1 = int(input("What is card 1? "))
    cards2 = int(input("What is card 2? "))
    print(dealer_action(cards1, cards2))
