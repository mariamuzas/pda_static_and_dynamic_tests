import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("hearts", 5)
        self.card2 = Card("spades", 3)
        self.card3 = Card("ace", 1)

        self.cards= [self.card1, self.card2]
        self.cards_with_ace = [self.card1, self.card2, self.card3]
        self.game = CardGame()

    def test_check_suit(self):
        self.assertEqual("spades", self.card2.suit)

    def test_check_for_ace_in_cards(self):
        self.assertEqual(None, self.game.check_for_ace(self.cards))

    def test_check_for_ace_in_cards_with_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.cards_with_ace))

    def test_highest_card(self):
        self.assertEqual(self.card1, self.game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual( "You have a total of 8", self.game.cards_total(self.cards))
    
