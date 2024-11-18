import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    # ทดสอบ C1b1
    def test_age_below_zero(self):
        with self.assertRaises(ValueError):  # อายุ -1
            self.zoo.get_ticket_price(-1)

    # ทดสอบ C1b2 (0 <= อายุ <= 12)
    def test_age_zero(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)  # อายุ 0
    
    def test_age_twelve(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)  # อายุ 12

    # ทดสอบ C1b3 (13 <= อายุ <= 20)
    def test_age_thirteen(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)  # อายุ 13

    def test_age_twenty(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)  # อายุ 20

    # ทดสอบ C1b4 (21 <= อายุ <= 60)
    def test_age_twenty_one(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)  # อายุ 21

    def test_age_sixty(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)  # อายุ 60

    # ทดสอบ C1b5 (อายุมากกว่า 60)
    def test_age_sixty_one(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)  # อายุ 61

if __name__ == '__main__':
    unittest.main()
