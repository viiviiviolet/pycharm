# importing
import random
import time

# initialize variables
bank = 0
total = 0
dealer_total = 0
dealer_revealed_total = 0
hand = []
split_hand = []
dealer_hand = []
card = ""
usedAce = False
dealend = False

# build deck
values = {
    "Ace": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}
deck = list(values)*4

def deal(deck):
    random.shuffle(deck)
    global total
    global bank
    global card
    global dealer_total
    global dealer_revealed_total
    global dealer_hand
    global dealend
    for i in range(2):
        card = deck.pop()
        hand.append(card)
        total += values[card]
    print(f'You were dealt a {hand[0]} and a {hand[1]}. Your current total is {total}')
    for i in range(2):
        card = deck.pop()
        dealer_hand.append(card)
        dealer_total += values[card]
    dealer_revealed_total += values[card]
    print(f'The dealer was dealt a face-down card and a {dealer_hand[1]}. Their current revealed total is {dealer_revealed_total}.')
    if dealer_hand[1] == "Ace":
        while True:
            insurance = input("Would you like to buy insurance? (y/n) ")
            if insurance == 'y':
                insurancebet = bet // 2
                bank -= insurancebet
                print(f'You bet {insurancebet} tokens for insurance.')
                if dealer_total == 21:
                    print(f'The Dealer had blackjack! You win the insurance bet. You have gained {bet} tokens')
                    bank += bet
                else:
                    print(f'The Dealer did not have blackjack. You have lost {insurancebet} tokens.')
            elif insurance == 'n':
                if dealer_total == 21:
                    print("The dealer had blackjack")
                    if total == 21:
                        print(f"It's a push. Your {bet} token bet has been returned to the bank")
                        bank += bank
                        dealend = True
                    else:
                        print("You have lost.")
                        dealend = True
                break

def hit(hand):
    global total
    global card
    global usedAce
    card = deck.pop()
    hand.append(card)
    total += values[card]
    if "Ace" in hand and not usedAce and total > 21:
        total -= 10
        usedAce = False

def dealerhit(hand):
    global total
    global dealer_total
    global card
    global usedAce
    card = deck.pop()
    hand.append(card)
    dealer_total += values[card]
    if "Ace" in hand and not usedAce and total > 21:
        total -= 10

def reset():
    global deck
    global total
    global dealer_total
    global dealer_revealed_total
    global hand
    global split_hand
    global dealer_hand
    global card
    global usedAce
    deck = list(values) * 4
    total = 0
    dealer_total = 0
    dealer_revealed_total = 0
    hand = []
    split_hand = []
    dealer_hand = []
    card = ""
    usedAce = False

def dealerturn():
    global bank
    global dealer_total
    global dealer_hand
    print(f'The dealer has revealed that their face-down card was a {dealer_hand[0]}. Their current total is {dealer_total}')
    if 'Ace' in dealer_hand and (values[dealer_hand[1]] == 10 or (values[dealer_hand[0]]) == 10):
        print("The dealer has Blackjack. You lost.")
    while dealer_total < 17:
        dealerhit(dealer_hand)
        print(f'The dealer drew a {card}. Their total is now {dealer_total}.')
    if dealer_total > 21:
        print(f'The dealer has bust. You win {bet*2} tokens.')
        bank += bet*2
    elif dealer_total > total:
        print(f'The dealer has won, you have lost your {bet} token bet.')
    elif dealer_total == total:
        print(f"It's a push. your {bet} token bet has been returned to the bank.")
        bank += bet
    elif dealer_total < total:
        print(f'You win! You have won {bet*2} tokens')
        bank += bet*2

def split():
    global bank
    move = hand.pop()
    split_hand.append(move)
    bank -= bet
    total = values[hand[0]]
    while True:
        action = input(f"Your current total in your first hand is {total}. Would you like to \n1. Hit\n2. Stand")
        if action == '1':
            hit(hand)
            print(f'You have been dealt a {card}')
        elif action == '2':
            break
        else:
            print("Please enter a valid input.")
        if total > 21:
            print("This hand has bust. You have lost your bet.")
            break
    total = 0
    while True:
        action = input(f"Your current total in your second hand is {total}. Would you like to \n1. Hit\n2. Stand\n")
        if action == '1':
            hit(split_hand)
            print(f'You have been dealt a {card}')
        elif action == '2':
            break
        else:
            print("Please enter a valid input.")
        if total > 21:
            print("This hand has bust. You have lost your bet.")
            break

# main
bank = 100
print('You have been given 100 tokens to start with')
while True:
    while bank > 0:
        print(f'You currently have {bank} tokens.')
        while True:
            bet = int(input('How many tokens would you like to bet? '))
            if bet > bank:
                print("You do not have enough tokens to bet that much")
            else:
                bank -= bet
                break
        print('Dealing...')
        time.sleep(1.0)
        deal(deck)
        if 'Ace' in hand and (values[hand[1]] == 10 or (values[hand[0]]) == 10):
            print(f'Blackjack! You earned {int(bet * (5 / 2))} coins')
            bank += int(bet * (5 / 2))
            break
        while not dealend:
            action = input(f"Your current total is {total}. Would you like to:\n1. Hit\n2. Stand\n3. Double Down\n4. Split\n")
            if action == '1':
                hit(hand)
                print(f'You drew a {card}. Your total is now {total}.')
            elif action == '2':
                break
            elif action == '3':
                if len(hand) != 2:
                    print('You can only double down with only two cards.')
                else:
                    hit(hand)
                    print(f'You doubled your bet and drew a {card}. Your final total is {total}.')
                    bank -= bet
                    bet *= 2
                    # WIP
                    break
            elif action == '4':
                if values[hand[0]] != values[hand[1]] or len(hand) > 2:
                    print("You can only split with doubles")
                else:
                    split()
            else:
                print("Please enter a valid input")
            if total > 21:
                print("You have busted")
                reset()
                break
        if total > 21:
            reset()
            break
        else:
            print("It is now the dealer's turn")
            dealerturn()
            reset()
            while True:
                again = input('Would you like to continue playing? (y/n) ')
                if again == 'y':
                    break
                if again == 'n':
                    print("Goodbye.")
                    time.sleep(2)
                    quit()
            break
    if bank <= 0:
        print("You have run out of tokens.")
        time.sleep(5)
        quit()




