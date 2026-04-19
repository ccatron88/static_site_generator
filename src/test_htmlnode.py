import unittest
from htmlnode import HtmlNode 

class TestHtmlNode(unittest.TestCase):

    def test_html_props(self):
        node_props = {
            "href": "https://www.google.com",
            "target": "_blank" 
        }
        node = HtmlNode("<a>", "google", None, node_props)
        self.assertIsNotNone(node.props_to_html)

    def test_to_html_props(self):
        node_props = {
            "href": "https://www.google.com",
            "target": "_blank" 
        }
        node = HtmlNode("<a>", "google", None, node_props)
        self.assertEqual(
            node.props_to_html(),
            " href='https://www.google.com' ",
        )
