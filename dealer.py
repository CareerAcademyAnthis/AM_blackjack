dealer_value = int(input("Dealer Enter Number: "))
player_value = int(input("Player Enter Number: "))
dealer_score = 0
player_score = 0

if dealer_value > player_value:
    dealer_score += 1
    print("Dealer Wins this Round")
elif dealer_value == player_value:
    dealer_score += 1
    print("Tie, Dealer Wins Round")
else:
    player_score += 1
    print("Player Wins")

print(f"Player Score is {player_score}")
print(f"Dealer Score is {dealer_score}")