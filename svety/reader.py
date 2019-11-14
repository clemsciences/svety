"""

"""
import os

from lxml import etree


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


def get_xml_root(filename, path=""):
    """

    :param filename:
    :param path:
    :return:
    """
    parser = etree.XMLParser(load_dtd=True, no_network=False)
    tree = etree.parse(os.path.join(path, filename), parser=parser)
    root = tree.getroot()
    return root


def read_entry(root, word):

    lexical_entries = root.findall('.//LexicalEntry')
    [{feat.get("att"): feat.get("val") for feat in entry.findall("feat")}  for entry in lexical_entries]
    print(lexical_entries[0].find("Lemma"))
    print(lexical_entries[0].find("Lemma").getchildren())
    # print(lexical_entries[0].getchildren().get("Lemma"))
    # print(lexical_entries[0].get("Lemma").get("FormRepresentation"))
    print(lexical_entries[0].find("Sense"))
    print(lexical_entries[0].find("Sense").getchildren())
    # print(lexical_entries[0])
    return lexical_entries
