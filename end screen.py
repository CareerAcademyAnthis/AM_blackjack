#get scores from gameplay
place_holder1 = 2
place_holder2 = 6
end_game = input("do you want to end the game? ")
if end_game.lower().lstrip().rstrip() in ["yes", "y"]:
    print("you won '' amount of times  ")
    print("dealers won '' amount of times:  ")
    print("you pushed ''  amount of times")
    print("thank you for playing have a nice day")
if place_holder2 > place_holder1:
    print("you lost!!!")
elif place_holder1 > place_holder2:
    print("you won!!!!")
elif place_holder1 == place_holder2:
    print("you tie!!!!")


