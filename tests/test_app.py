"""Tests for the add_numbers function in app.py."""

from ..app import add_numbers

def test_add_numbers():
    """Test that add_numbers correctly returns the sum of two integers."""
    assert add_numbers(1, 2) == 3
