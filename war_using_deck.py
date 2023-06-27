import random

values = {
    "Two": 2, "Three": 3, "Four": 4, "Five": 5,  "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
}
suits = (
    "Hearts", "Diamonds", "Spades", "Clubs"
)
ranks = (
    "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"
)
    

class Card ():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        pass
    
    def __str__(self) -> str:
        return self.rank + " Of " + self.suit
        pass


class Deck():
    def __init__(self) -> None:
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create a card 
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
        pass
    def shuffle(self):
        random.shuffle(self.all_cards)
        pass
    pass

new_deck = Deck()
first_card = new_deck.all_cards[0]
print(first_card)

two_hearts = Card("Hearts", "Two")
three_clubs = Card("Clubs", "Three")
# print(two_hearts)
# print(two_hearts.suit)
# print(two_hearts.rank)

# print(values[two_hearts.rank])
# print(two_hearts.value)
# print(three_clubs.value)
# print(three_clubs.value > two_hearts.value)