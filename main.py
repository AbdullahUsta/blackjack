import random
from random import randint

# List of card values
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Initial hands
player_hand1 = random.choice(cards)
player_hand2 = random.choice(cards)
comp_hand1 = random.choice(cards)
comp_hand2 = random.choice(cards)

player_hand = player_hand1 + player_hand2
comp_hand = comp_hand1 + comp_hand2

# Blackjack situation
if comp_hand == 21:
    print("BlackJack, Computer wins!")
elif player_hand == 21:
    print("BlackJack, You win!")
elif comp_hand > 21 and player_hand <= 21:
    print("Computer busts! You win!")
elif player_hand > 21 and comp_hand <= 21:
    print("You bust! Computer wins!")
else:
    # Hit or stay situation
    print(f"You have {player_hand}")
    print(f"Computer has {comp_hand}")

    while player_hand < 21:
        draw_card = input("Type 'H' to hit, or any other letter to Stay: ").strip().lower()
        if draw_card == "h":
            new_card = random.choice(cards)
            player_hand += new_card
            print(f"You drew a {new_card}. Your total is now {player_hand}.")
            if player_hand > 21:
                print("You bust! Computer wins!")
                break
        else:
            break

    # If player hasn't bust, the computer draws
    if player_hand <= 21:
        while comp_hand < 17:  # Standard dealer rule to hit until reaching 17
            new_card = random.choice(cards)
            comp_hand += new_card
            if comp_hand > 21:
                print(f"Computer drew a {new_card}. Computer busts! You win!")
                break

        if comp_hand <= 21:
            print(f"Computer's total is {comp_hand}.")
            if player_hand > comp_hand:
                print(f"You win with {player_hand}!")
            elif player_hand < comp_hand:
                print(f"Computer wins with {comp_hand}!")
            else:
                print("It's a tie!")
