import randomp1:L

#Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

#create a deck of cards
deck = [(suit,rank) for rank in ranks for suit in suits]

#shuffle the deck
random.shuffle(deck)

#print shuffled deck
print(deck)

#split the deck into two hands
midpoint = len(deck) // 2
p1_cards = deck[ : midpoint]
print(p1_cards)
p2_cards = deck[midpoint: ]
print(p2_cards)

#list.pop[] removes the item at a given postion of a list
def card_comparison(p1_cards, p2_cards):
    if ranks.index(p1_cards[1]) > ranks.index(p2_cards[1]):
        return 1
    elif ranks.index(p1_cards[1]) < ranks.index(p2_cards[1]):
        return 2
    else:
        return 0

def gameloop():
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        p1_cards = p1_deck.pop(0)
        p2_cards = p2_deck.pop(0)
        
        result = winning_card(p1_cards, p2_cards)

        if result == 1: #player 1 had the strong card
            p1_deck.append(p1_cards)
            p1_deck.append(p2_cards)
            # player 1 takes all cards
        elif result == 2: # player 2 had the strong card
            p2_deck.append(p1_cards)
            p2_deck.append(p2_cards)
            # player 2 takes all cards
        elif result == 0: #A TIE

            #players put 3 cards facing down
            p1_cards =p1_deck[0:4]
            p2_cards =p2_deck[0:4]

            p2_decks = p2_deck[4:]
            p1_decks = p1_deck[4:]

            p1_cards = p1_deck.pop(0)
            p2_cards = p2_deck.pop(0)

            result = winning_card(p1_cards, p2_cards)

            if result == 1: #player 1 won the peace
                p1_deck.append(p1_cards)
                p1_deck.append(p2_cards)
                p1_deck.extend(p2_cards)
                p1_deck.extend(p1_cards)
            elif result == 2: #player 2 won the peace
                p2_deck.append(p1_cards)
                p2_deck.append(p2_cards)
                p2_deck.extend(p2_cards)
                p2_deck.extend(p2_cards)



# Main function to run the game
def play_game():
    print("Ready for some peace!")

#Call the main functions to start the game
def( #create another loop)                   
