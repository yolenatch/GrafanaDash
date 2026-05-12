# test_grafanadash.py
"""
Tests for GrafanaDash module.
"""

import unittest
from grafanadash import GrafanaDash

class TestGrafanaDash(unittest.TestCase):
    """Test cases for GrafanaDash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GrafanaDash()
        self.assertIsInstance(instance, GrafanaDash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GrafanaDash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
