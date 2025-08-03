# test_machinetalk.py
"""
Tests for MachineTalk module.
"""

import unittest
from machinetalk import MachineTalk

class TestMachineTalk(unittest.TestCase):
    """Test cases for MachineTalk class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MachineTalk()
        self.assertIsInstance(instance, MachineTalk)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MachineTalk()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
