# test_coinray.py
"""
Tests for CoinRay module.
"""

import unittest
from coinray import CoinRay

class TestCoinRay(unittest.TestCase):
    """Test cases for CoinRay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinRay()
        self.assertIsInstance(instance, CoinRay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinRay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
