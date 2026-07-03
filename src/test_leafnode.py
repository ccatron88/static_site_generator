import unittest
from leafnode import *
from textnode import TextNode, TextType, text_node_to_html_node

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT.value)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "<text>")
        self.assertEqual(html_node.value, "This is a text node")
