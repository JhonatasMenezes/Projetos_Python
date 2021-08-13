import random

class Card:    
    suit_names = ['Paus', 'Ouros', 'Copas', 'Espadas']
    rank_names = [None, 'Ás', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'Valete', 'Dama', 'Rei']
                            
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s de %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])    
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2                
        
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
        
    def add_card(self, card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuflle(self.cards)
    
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    
class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label    

    

    
card = Deck.pop_card(8)
print(card)