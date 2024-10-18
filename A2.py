import random

#Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

#create a deck of cards
deck = [(suit,rank) for rank in ranks for suit in suits]

#shuffle the deck
random.shuffle(deck)

#split the deck into two hands
midpoint = len(deck) // 2
p1_deck = deck[ : midpoint]
p2_deck = deck[midpoint: ]

#list.pop[] removes the item at a given postion of a list
def card_comparison(p1_cards, p2_cards):
    print(f"about to print p1 card: {p1_cards}, p2 card: {p2_cards}")
    if ranks.index(p1_cards[1]) > ranks.index(p2_cards[1]):
        return 1
    elif ranks.index(p1_cards[1]) < ranks.index(p2_cards[1]):
        return 2
    else:
        return 0

def game_loop(p1_deck, p2_deck):
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        
        input("press enter to play ") 
        p1_cards = p1_deck.pop(0)
        p2_cards = p2_deck.pop(0)

        
        result = card_comparison(p1_cards, p2_cards)

        if result == 1: #player 1 had the strong card
            print(f"Player 1 has the stronger card!")
            p1_deck.append(p1_cards)
            p1_deck.append(p2_cards)
            # player 1 takes all cards
        elif result == 2: # player 2 had the strong card
            print(f"player 2 has the stronger card")
            p2_deck.append(p1_cards) 
            p2_deck.append(p2_cards) 
            # player 2 takes all cards 
        elif result == 0: #A TIE
            print(f"ITS A TIE! ... this is wa...peace!")
            #players put 3 cards facing down
            print("Player 1 face down 3 cards{face down}")
            p1_fd =p1_deck[0:4]

            print("Player 2 face down 3 cards{face down}")
            p2_fd =p2_deck[0:4]
            
            print("Player 2 places down a card")
            p2_deck = p2_deck[4:]

            print("Player 1 places down a card")
            p1_deck = p1_deck[4:]

            p1_cards = p1_deck.pop(0)
            p2_cards = p2_deck.pop(0)

            result = card_comparison(p1_cards, p2_cards)

            if result == 1: #player 1 won the peace
                p1_deck.append(p1_cards)
                p1_deck.append(p2_cards)
                p1_deck.extend(p2_fd)
                p1_deck.extend(p1_fd)
                print(f"Player 1 append{p1_cards}{p2_cards} and extend{p2_fd}{p1_fd}")
            elif result == 2: #player 2 won the peace
                p2_deck.append(p1_cards)
                p2_deck.append(p2_cards)
                p2_deck.extend(p2_fd)
                p2_deck.extend(p1_fd)
                print(f"Player 2 append{p1_cards}{p2_cards} and extend{p2_fd}{p1_fd}")




#Call the main functions to start the game
game_loop(p1_deck, p2_deck)
