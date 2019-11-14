"""

"""
import os
import unittest

from lxml import etree

from svety import PACKDIR
from svety import reader
from svety import retriever


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


class TestMain(unittest.TestCase):
    """

    """
    def setUp(self) -> None:
        self.filename = "hellqvist.xml"
        self.path = PACKDIR

    def test_retrieve_text(self):
        result = retriever.retrieve_dictionary()
        self.assertTrue(result)
        self.assertIn(self.filename, os.listdir(os.getcwd()))

    def test_root(self):
        root = reader.get_xml_root(self.filename, self.path)
        self.assertEqual(type(root), etree._Element)

    def test_lookup_word(self):
        root = reader.get_xml_root(self.filename, self.path)
        word = reader.read_entry(root, "enkom")
        self.assertEqual(word["faksimilID"], '0208')
