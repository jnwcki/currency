import unittest
from currency import eur_to_usd, usd_to_eur, list_eur_to_usd, list_usd_to_eur, Money


class ConTest(unittest.TestCase):

    def test_check_if_eur_convert_to_usd(self):
        self.assertEqual(eur_to_usd(0.9), 1)

    def test_check_if_usd_convert_to_eur(self):
        self.assertEqual(usd_to_eur(1), .9)

    def test_does_list_of_eur_convert_to_usd(self):
        self.assertEqual(list_eur_to_usd([.9]), [1])

    def test_longer_list_of_eur_convert_to_usd(self):
        self.assertEqual(list_eur_to_usd([.9, 90, 1.8]), [1, 100, 2])

    def test_list_of_usd_convert_to_eur(self):
        self.assertEqual(list_usd_to_eur([1, 2, 100]), [.9, 1.80, 90])

# Test the Money class for correct conversions

class MoneyConTest(unittest.TestCase):
    def test_check_if_eur_convert_to_usd(self):
        self.assertEqual(Money().eur_to_usd(.9), 1)

    def test_check_if_usd_convert_to_eur(self):
        self.assertEqual(Money().usd_to_eur(1), .9)

    def test_does_list_of_eur_convert_to_usd(self):
        self.assertEqual(Money().list_eur_to_usd([.9]), [1])

    def test_longer_list_of_eur_convert_to_usd(self):
        self.assertEqual(Money().list_eur_to_usd([.9, 90, 1.8]), [1, 100, 2])

    def test_list_of_usd_convert_to_eur(self):
        self.assertEqual(Money().list_usd_to_eur([1, 2, 100]), [.9, 1.80, 90])

