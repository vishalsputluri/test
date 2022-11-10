import math
import unittest
from unittest import TestCase
from unittest.mock import MagicMock, Mock

class PrimeNumber(TestCase):
    
    @staticmethod
    def is_prime_number(n):
        if n <= 1:
            return False
        
        elif n == 2:
            return True
        
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        
        return True
    
    @staticmethod
    def is_prime_check(n):
        return "Prime" if PrimeNumber.is_prime_number(n) == True else "Not Prime"
    
    def test_perform_operation1(self):
        PrimeNumber.is_prime_number = MagicMock(return_value=False)
        self.assertEqual(PrimeNumber.is_prime_check(4), "Not Prime")
        
    
    def test_perform_operation2(self):
        PrimeNumber.is_prime_number = MagicMock(return_value=True)
        self.assertEqual(PrimeNumber.is_prime_check(2), "Prime")
        
    def test_perform_operation3(self):
        self.assertEqual(PrimeNumber.is_prime_check(3), "Prime")
        
    def test_perform_operation4(self):
        mock_prime_number = Mock(return_value=False)
        PrimeNumber.is_prime_number = mock_prime_number
        self.assertEqual(PrimeNumber.is_prime_check(6), "Not Prime")
    
    def test_perform_operation4(self):
        mock_prime_number = Mock(return_value=True)
        PrimeNumber.is_prime_number = mock_prime_number
        self.assertEqual(PrimeNumber.is_prime_check(7), "Prime")
        
if __name__ == '__main__':
    unittest.main()
    