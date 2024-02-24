#!/usr/bin/python3
"""unittest for Base class"""


import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ class to test Base class"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py])
        self.assertEqual(result.total_errors, 0, "Found code style erros (and warnings).")
