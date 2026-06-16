import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is not a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_link_is_None(self):
        node = TextNode("This is a link", TextType.LINK)
        self.assertIsNone(node.url)

    def test_text_type_is_different(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a italic node", TextType.ITALIC)
        self.assertNotEqual(node.text_type, node2.text_type)

if __name__ == "__main__":
    unittest.main()

#     When a user deletes a note, we'd like to flag it as deleted in the database.
