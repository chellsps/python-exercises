```import random
from card import Card



class Deck:

    def __init__(self):
        self.suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

        self.deck = self.traditionCards()
    

    def traditionCards(self):
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
        values = [str(i) for i in range(1,11)] + ["Jack", "Queen", "King"]
        deck = []
        for suit in suits:
            for value in values:
                newCard = Card(value, suit)
                deck.append(newCard)
        return deck

    def shuffle_deck(self):
        alreadyUsedCards = []
        shuffledDeck = []
        for randNumber in random.sample(range(0,52),52):
            if randNumber not in alreadyUsedCards and randNumber != 53:
                selectedCard = self.deck[randNumber]
                shuffledDeck.append(selectedCard)
                alreadyUsedCards.append(randNumber)
            else:
                pass
        self.deck = shuffledDeck

    def remove_card(self, value, suit):
        removableCardValue = value
        removableCardSuit = suit
        index = 0
        for card in self.deck:
            if card.value == removableCardValue and card.suit == removableCardSuit:
                self.deck.pop(index)
            else:
                index += 1


# deck1 = Deck()

# # deck1.shuffle_deck()
# # deck1.remove_card(value = "Jack", suit = "Clubs")

# for card in deck1.deck:
#     print(card)
# print(len(deck1.deck))

```


[7:35] 
[5:17] 
player.py
```class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def calculate_player_hand(self):
        hand_value = 0
        specials = ["King", "Queen", "Jack"]
        for card in self.hand:
            if card.value in specials:
                hand_value += 10
            else:
                hand_value += int(card.value)
        return hand_value
        # if hand_value > 21:
        #     return hand_value
        # elif hand_value < 21:
        #     return hand_value
        # else:
        #     return hand_value

```


[5:17] 
blackjack.py
```from random import shuffle
from deck import Deck
from card import Card
from player import Player



class Blackjack:

    def __init__(self, player):
        self.player = player
        self.dealer = Player("Dealer")
        self.deck = Deck().deck

    def welcome_message(self):
        print("""
            WELCOME TO BLACKJACK!! 
               Created by Sasha

                  GOOD LUCK, {}!!
            """.format(self.player.name)
            )
        

    def deal_card(self, player):
        if player.name == "Dealer":
            self.dealer.hand.append(self.deck.pop(0))
        else:
            self.player.hand.append(self.deck.pop(0))

    def display_cards(self, howto = "blank"):
        if howto == "Final":

            dealerString = ""
            for card in self.dealer.hand:
                dealerString  += str(card.value) + " "
            print("Dealers Hand: ", dealerString)

            playerString = ""
            for card in self.player.hand:
                playerString += str(card.value) + " "
            print("{}'s Hand: ", playerString)
        else:
            dealerString = "Unknown "
            for card in self.dealer.hand[1:]:
                dealerString  += str(card.value) + " "
            print("Dealers Hand: ", dealerString)
            playerString = ""
            for card in self.player.hand:
                playerString += str(card.value) + " "
            print("{}'s Hand: ", playerString)

    def ask_player_decision(self):
        decision = ""
        while decision != "h" and decision != "s":
            decision = input('''
                What would you like to do? To hit, type "h". To stay, type "s"
                \n'''
                )
        if decision == "h":
            return True
        else:
            return False

    def dealer_plays(self):
        while self.dealer.calculate_player_hand() < 17:
            print("Dealer Hits")
            self.deal_card(self.dealer)
        return self.dealer.calculate_player_hand()
            




def main():
    playerName = input("Please insert Player Name: ")
    newPlayer = Player(str(playerName))
    bji = Blackjack(newPlayer)
    bji.welcome_message()
    shuffle(bji.deck)


    # DEAL OPENING HANDS TO EACH PLAYER
    bji.deal_card(bji.player)    
    bji.deal_card(bji.dealer)
    bji.deal_card(bji.player)
    bji.deal_card(bji.dealer)
    bji.display_cards()
    stayVariable = False
    
    while bji.player.calculate_player_hand() < 21 and stayVariable == False:
        playerChoice = bji.ask_player_decision()
        if playerChoice == True:
            bji.deal_card(bji.player)
            bji.display_cards()
        else:
            stayVariable = True

    if bji.player.calculate_player_hand() > 21:
        print("You have busted!!! Try Again next time!")
    else:
        dealerResult = bji.dealer_plays()
        if dealerResult == 21 and bji.player.calculate_player_hand() == 21:
            print("TIE!")
            bji.display_cards("Final")
        elif dealerResult > bji.player.calculate_player_hand() and dealerResult <= 21:
            print("YOU LOSE")
            bji.display_cards("Final")
        elif dealerResult < bji.player.calculate_player_hand():
            print("YOU WIN")
            bji.display_cards("Final")




if __name__ == "__main__":
    main()
```