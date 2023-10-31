def check_tie(dealer_value, player_value):
    if dealer_value == player_value:
        return "win"


dealer_score = 0
# 2 in the parenthesis will be replaced with the actual values of the hands
if check_tie(2,2) == "win":
    dealer_score += 1
    print(dealer_score)