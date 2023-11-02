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

cards1 = int(input("What is card 1? "))
cards2 = int(input("What is card 2? "))
print(dealer_action(cards1, cards2))

dealer_value = int(input("Dealer Enter Card Number: "))
player_value = int(input("Player Enter Card Number: "))
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

print(f"Dealer - {dealer_score}")
print(f"Player - {player_score}")
