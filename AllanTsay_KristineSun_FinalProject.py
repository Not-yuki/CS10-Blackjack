import random

deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
playerHand = []
dealerHand = []

def deal(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total = 0
    ace_11s = 0
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total

def print_hands():
    print(f"Dealer has {dealerHand[0]} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")


def play_game():
    for _ in range(2):
        deal(dealerHand)
        deal(playerHand)

    player_in = True

    while player_in:
        print_hands()
        choice = input("1: Stay\n2: Hit\n")
        
        if choice not in ['1','2']:
            print("Please enter 1 or 2.")
        elif choice == '1':
            player_in = False
        else:
            deal(playerHand)
            if total(playerHand) >= 21:
                break

    while total(dealerHand) <= 16:
        deal(dealerHand)

    player_total = total(playerHand)
    dealer_total = total(dealerHand)

    print(f"You have {playerHand} for a total of {total(playerHand)} and Dealer has {total(dealerHand)}")

    if player_total == 21 and dealer_total == 21:
        print("Push. Tie")
    elif player_total > 21:
        print("You bust. Dealer wins")
    elif dealer_total > 21:
        print("Dealer busts. You Win!")
    elif player_total == 21:
        print("Blackjack! You Win!")
    elif dealer_total == 21:
        print("You lose")
    elif dealer_total == player_total:
        print("Push. Tie")
    elif 21 - dealer_total < 21 - player_total:
        print("Dealer wins.")
    elif 21 - dealer_total > 21 - player_total:
        print("You win")

def main():
    while True:
        playerHand.clear()
        dealerHand.clear()
        deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        play_game()
        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
