def build(values, suites):
    deck = []
    for suite in suites:
        for value in values:
            deck.append([value, suite])
    return deck


def starting_player_hand(player_hand):
    print("╔═════════════╗ ╔═════════════╗\n"
          f"║ {player_hand[0][0]}           ║ ║ {player_hand[1][0]}           ║\n"
          "║             ║ ║             ║\n"
          "║             ║ ║             ║\n"
          f"║      {player_hand[0][1]}      ║ ║      {player_hand[1][1]}      ║\n"
          "║             ║ ║             ║\n"
          "║             ║ ║             ║\n"
          f"║           {player_hand[0][0]} ║ ║           {player_hand[1][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝")


def player_hand_1hit(player_hand):
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║ {player_hand[0][0]}           ║ ║ {player_hand[1][0]}           ║ ║ {player_hand[2][0]}           ║\n"
          "║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║\n"
          f"║      {player_hand[0][1]}      ║ ║      {player_hand[1][1]}      ║ ║      {player_hand[2][1]}      ║\n"
          "║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║\n"
          f"║           {player_hand[0][0]} ║ ║           {player_hand[1][0]} ║ ║           {player_hand[2][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def player_hand_2hit(player_hand):
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║ {player_hand[0][0]}           ║ ║ {player_hand[1][0]}           ║ ║ {player_hand[2][0]}           ║ ║ {player_hand[3][0]}           ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║      {player_hand[0][1]}      ║ ║      {player_hand[1][1]}      ║ ║      {player_hand[2][1]}      ║ ║      {player_hand[3][1]}      ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║           {player_hand[0][0]} ║ ║           {player_hand[1][0]} ║ ║           {player_hand[2][0]} ║ ║           {player_hand[3][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def player_hand_3hit(player_hand):
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║ {player_hand[0][0]}           ║ ║ {player_hand[1][0]}           ║ ║ {player_hand[2][0]}           ║ ║ {player_hand[3][0]}           ║ ║ {player_hand[4][0]}           ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║      {player_hand[0][1]}      ║ ║      {player_hand[1][1]}      ║ ║      {player_hand[2][1]}      ║ ║      {player_hand[3][1]}      ║ ║      {player_hand[4][1]}      ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║           {player_hand[0][0]} ║ ║           {player_hand[1][0]} ║ ║           {player_hand[2][0]} ║ ║           {player_hand[3][0]} ║ ║           {player_hand[4][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def player_hand_4hit(player_hand):
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║ {player_hand[0][0]}           ║ ║ {player_hand[1][0]}           ║ ║ {player_hand[2][0]}           ║ ║ {player_hand[3][0]}           ║ ║ {player_hand[4][0]}           ║ ║ {player_hand[5][0]}           ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║      {player_hand[0][1]}      ║ ║      {player_hand[1][1]}      ║ ║      {player_hand[2][1]}      ║ ║      {player_hand[3][1]}      ║ ║      {player_hand[4][1]}      ║ ║      {player_hand[5][1]}      ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║           {player_hand[0][0]} ║ ║           {player_hand[1][0]} ║ ║           {player_hand[2][0]} ║ ║           {player_hand[3][0]} ║ ║           {player_hand[4][0]} ║ ║           {player_hand[5][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def player_hand_5hit(player_hand):
    print(
        "╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
        f"║ {player_hand[0][0]}           ║ ║ {player_hand[1][0]}           ║ ║ {player_hand[2][0]}           ║ ║ {player_hand[3][0]}           ║ ║ {player_hand[4][0]}           ║ ║ {player_hand[5][0]}           ║ ║ {player_hand[6][0]}           ║\n"
        "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
        "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
        f"║      {player_hand[0][1]}      ║ ║      {player_hand[1][1]}      ║ ║      {player_hand[2][1]}      ║ ║      {player_hand[3][1]}      ║ ║      {player_hand[4][1]}      ║ ║      {player_hand[5][1]}      ║ ║      {player_hand[6][1]}      ║\n"
        "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
        "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
        f"║           {player_hand[0][0]} ║ ║           {player_hand[1][0]} ║ ║           {player_hand[2][0]} ║ ║           {player_hand[3][0]} ║ ║           {player_hand[4][0]} ║ ║           {player_hand[5][0]} ║ ║ {player_hand[6][0]}           ║\n"
        "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def player_hand_6hit(player_hand):
    print(
        "╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
        f"║ {player_hand[0][0]}           ║ ║ {player_hand[1][0]}           ║ ║ {player_hand[2][0]}           ║ ║ {player_hand[3][0]}           ║ ║ {player_hand[4][0]}           ║ ║ {player_hand[5][0]}           ║ ║ {player_hand[6][0]}           ║ ║ {player_hand[7][0]}           ║\n"
        "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
        "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
        f"║      {player_hand[0][1]}      ║ ║      {player_hand[1][1]}      ║ ║      {player_hand[2][1]}      ║ ║      {player_hand[3][1]}      ║ ║      {player_hand[4][1]}      ║ ║      {player_hand[5][1]}      ║ ║      {player_hand[6][1]}      ║ ║      {player_hand[7][1]}      ║\n"
        "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
        "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
        f"║           {player_hand[0][0]} ║ ║           {player_hand[1][0]} ║ ║           {player_hand[2][0]} ║ ║           {player_hand[3][0]} ║ ║           {player_hand[4][0]} ║ ║           {player_hand[5][0]} ║ ║ {player_hand[6][0]}           ║ ║ {player_hand[7][0]}           ║\n"
        "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def starting_dealer_hand(face_up_down):
    """takes input of true or false to reveal first card or not"""
    if face_up_down:
        print("╔═════════════╗ ╔═════════════╗\n"
              f"║  {dealer_hand[0][0]}          ║ ║ {dealer_hand[1][0]}           ║\n"
              "║             ║ ║             ║\n"
              "║             ║ ║             ║\n"
              f"║      {dealer_hand[0][1]}      ║ ║      {dealer_hand[1][1]}      ║\n"
              "║             ║ ║             ║\n"
              "║             ║ ║             ║\n"
              f"║           {dealer_hand[0][0]} ║ ║           {dealer_hand[1][0]} ║\n"
              "╚═════════════╝ ╚═════════════╝")
    elif not face_up_down:
        print("╔═════════════╗ ╔═════════════╗\n"
              f"║★★★★★★★★★★║ ║ {dealer_hand[1][0]}           ║\n"
              "║★★★★★★★★★★║ ║             ║\n"
              "║★★★★★★★★★★║ ║             ║\n"
              f"║CareerAcademy║ ║      {dealer_hand[1][1]}      ║\n"
              "║★★★★★★★★★★║ ║             ║\n"
              "║★★★★★★★★★★║ ║             ║\n"
              f"║★★★★★★★★★★║ ║           {dealer_hand[1][0]} ║\n"
              "╚═════════════╝ ╚═════════════╝")


def dealer_hand_1hit():
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║  {dealer_hand[0][0]}          ║ ║ {dealer_hand[1][0]}           ║ ║ {dealer_hand[2][0]}           ║\n"
          "║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║\n"
          f"║      {dealer_hand[0][1]}      ║ ║      {dealer_hand[1][1]}      ║ ║      {dealer_hand[2][1]}      ║\n"
          "║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║\n"
          f"║          {dealer_hand[0][0]}  ║ ║           {dealer_hand[1][0]} ║ ║           {dealer_hand[2][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def dealer_hand_2hit():
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║  {dealer_hand[0][0]}          ║ ║ {dealer_hand[1][0]}           ║ ║ {dealer_hand[2][0]}           ║ ║ {dealer_hand[3][0]}           ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║      {dealer_hand[1][1]}      ║ ║      {dealer_hand[1][1]}      ║ ║      {dealer_hand[2][1]}      ║ ║      {dealer_hand[3][1]}      ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║           {dealer_hand[0][0]} ║ ║           {dealer_hand[1][0]} ║ ║           {dealer_hand[2][0]} ║ ║           {dealer_hand[3][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def dealer_hand_3hit():
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║  {dealer_hand[0][0]}          ║ ║ {dealer_hand[1][0]}           ║ ║ {dealer_hand[2][0]}           ║ ║ {dealer_hand[3][0]}           ║ ║ {dealer_hand[4][0]}           ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║      {dealer_hand[0][1]}      ║ ║      {dealer_hand[1][1]}      ║ ║      {dealer_hand[2][1]}      ║ ║      {dealer_hand[3][1]}      ║ ║      {dealer_hand[4][1]}      ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║           {dealer_hand[0][0]} ║ ║           {dealer_hand[1][0]} ║ ║           {dealer_hand[2][0]} ║ ║           {dealer_hand[3][0]} ║ ║           {dealer_hand[4][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def dealer_hand_4hit():
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║ {dealer_hand[0][0]}           ║ ║ {dealer_hand[1][0]}           ║ ║ {dealer_hand[2][0]}           ║ ║ {dealer_hand[3][0]}           ║ ║ {player_hand[4][0]}           ║ ║ {player_hand[5][0]}           ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║      {dealer_hand[0][1]}      ║ ║      {dealer_hand[1][1]}      ║ ║      {dealer_hand[2][1]}      ║ ║      {dealer_hand[3][1]}      ║ ║      {player_hand[4][1]}      ║ ║      {player_hand[5][1]}      ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║           {dealer_hand[0][0]} ║ ║           {dealer_hand[1][0]} ║ ║           {dealer_hand[2][0]} ║ ║           {dealer_hand[3][0]} ║ ║           {player_hand[4][0]} ║ ║           {player_hand[5][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def split_cards(first_hand, other_hand):
    """add space to separate later"""
    print("╔═════════════╗ ╔═════════════╗ ╔═════════════╗ ╔═════════════╗\n"
          f"║ {first_hand[0][0]}           ║ ║ {first_hand[1][0]}           ║ ║ {other_hand[0][0]}           ║ ║ {other_hand[1][0]}           ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║      {first_hand[0][1]}      ║ ║      {first_hand[1][1]}      ║ ║      {other_hand[0][1]}      ║ ║      {other_hand[1][1]}      ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          "║             ║ ║             ║ ║             ║ ║             ║\n"
          f"║           {first_hand[0][0]} ║ ║           {first_hand[1][0]} ║ ║           {other_hand[0][0]} ║ ║           {other_hand[1][0]} ║\n"
          "╚═════════════╝ ╚═════════════╝ ╚═════════════╝ ╚═════════════╝")


def split_input(player_hand):
    if player_hand[0][0] == player_hand[1][0]:
        split_y_n = input("Do you want to split ('y' or 'yes' split): ")
        return split_y_n.lower()


def end_game(times_won, dealer_wins, push_amount):
    end_input = input("Do you want to end the game (type 'y' or 'yes' to end): ")
    if end_input.lower().lstrip().rstrip() in ["yes", "y"]:
        print(f"You won {times_won} round(s)")
        print(f"Dealers won {dealer_wins} round(s)")
        print(f"You pushed {push_amount} time(s)")
        if times_won < dealer_wins:
            print("you lost!!!")
        elif times_won > dealer_wins:
            print("You beat the dealer!!!!")
        elif times_won == dealer_wins:
            print("you tie!!!!")
        print("Thanks for playing have a nice day!")
        quit()


