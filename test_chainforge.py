# test_chainforge.py
"""
Tests for chainForge module.
"""

import unittest
from chainforge import chainForge

class TestchainForge(unittest.TestCase):
    """Test cases for chainForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = chainForge()
        self.assertIsInstance(instance, chainForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = chainForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
