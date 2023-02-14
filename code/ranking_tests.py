import unittest
from ranking import poker_ranking

class TestRankings(unittest.TestCase):
    """
    Test class inheriting from unittest.TestCase.
    Each method is a test case for each of the possible poker hands.
    Methods:
        test_invalid_hand(self): a test that provides an invalid hand as input to the poker ranking function.
        test_royal_flush(self): a test that provides a royal flush as input to the poker ranking function.
        test_straight_flush(self): a test that provides a straight flush as input to the poker ranking function.
        test_four_of_a_kind(self): a test that provides a four-of-a-kind as input to the poker ranking function.
        test_full_house(self): a test that provides a full house as input to the poker ranking function.
        test_flush(self): a test that provides a flush as input to the poker ranking function.
        test_straight(self): a test that provides a straight as input to the poker ranking function.
        test_three_of_a_kind(self): a test that provides a three-of-a-kind as input to the poker ranking function.
        test_two_pair(self): a test that provides two pairs as input to the poker ranking function.
        test_pair(self): a test that provides one pair as input to the poker ranking function.
        test_high_card(self): a test that provides a high card as input to the poker ranking function.
    """
    def test_invalid_hand(self):
        query = "ABCD 12E"
        result = poker_ranking(query)
        self.assertEqual(result, 'invalid hand: hand should be of the format `VS VS VS VS VS` where V and S are valid values and suits, and cards are distinct', 
                         "The response should be invalid hand: hand should be of the format `VS VS VS VS VS` where V and S are valid values and suits, and cards are distinct")
        
    def test_royal_flush(self):
        query = "10H KH JH QH AH"
        result = poker_ranking(query)
        self.assertEqual(result, 'royal flush: hearts', "The ranking should be royal flush: hearts")
    
    def test_straight_flush(self):
        query = "JH 7H 8H 9H 10H"
        result = poker_ranking(query)
        self.assertEqual(result, 'straight flush: Jack-high hearts', "The ranking should be straight flush: Jack-high hearts")
        
    def test_four_of_a_kind(self):
        query = "AH AS 5H AC AD"
        result = poker_ranking(query)
        self.assertEqual(result, 'four of a kind: Ace', "The ranking should be four of a kind: Ace")
        
    def test_full_house(self):
        query = "2H 4D 4S 2C 4H"
        result = poker_ranking(query)
        self.assertEqual(result, 'full house: 4 over 2', "The ranking should be full house: 4 over 2")
        
    def test_flush(self):
        query = 'AH 10H 2H QH 9H'
        result = poker_ranking(query)
        self.assertEqual(result, 'flush: hearts', "The ranking should be flush: hearts")
        
    def test_straight(self):
        query = '2C AS 3S 5D 4S'
        result = poker_ranking(query)
        self.assertEqual(result, 'straight: 5-high', "The ranking should be straight: 5-high")
        
    def test_three_of_a_kind(self):
        query = '6C 6S 6H 2D 3S'
        result = poker_ranking(query)
        self.assertEqual(result, 'three of a kind: 6', "The ranking should be three of a kind: 6")
        
    def test_two_pair(self):
        query = '2C 2S 5H 5D 4S'
        result = poker_ranking(query)
        self.assertEqual(result, 'two pair: 5 and 2', "The ranking should be two pair: 5 and 2")
        
    def test_pair(self):
        query = 'QC QS 6H 5D 4S'
        result = poker_ranking(query)
        self.assertEqual(result, 'one pair: Queen', "The ranking should be one pair: Queen")
        
    def test_high_card(self):
        query = "2H 3D 5S 9C KD"
        result = poker_ranking(query)
        self.assertEqual(result, "high card: King", "The ranking should be high card: King")

if __name__ == '__main__':
    unittest.main()
