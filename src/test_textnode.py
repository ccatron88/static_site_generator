import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from split_delimeter import split_nodes_delimeter
from markdown_extractions import extract_markdown_images


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

class TestSplitDelimeter(unittest.TestCase):
    def test_split_case(self):
        nodes = [TextNode("This is **bold text** to test.", TextType.TEXT)]
        split_node = split_nodes_delimeter(nodes, "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" to test.", TextType.TEXT),
        ])

    def test_delimeter_at_beginning(self):
        node = [TextNode("_beginning italic_ sentence to test.", TextType.TEXT)]
        split_node = split_nodes_delimeter(node, '_', TextType.ITALIC)
        self.assertEqual(split_node, [
            TextNode('', TextType.TEXT),
            TextNode('beginning italic', TextType.ITALIC),
            TextNode(' sentence to test.', TextType.TEXT),
        ])

    def test_two_delimited_sections(self):
        node = [TextNode("Sentence with **two sections** that are _delimeted_ to test.", TextType.TEXT)]
        split_node = split_nodes_delimeter(node, '**', TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("Sentence with ", TextType.TEXT),
            TextNode("two sections", TextType.BOLD),
            TextNode(" that are _delimeted_ to test.", TextType.TEXT),
        ])

class TestRegexExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    # def test_extract_two_markdown_images(self):
    #     matches = extract_markdown_images(
    #         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![rick roll](https://i.imgur.com/abzjjcJKZ.png)"
    #     )
    #     self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("rick roll", "https://i.imgur.com/abzjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()
