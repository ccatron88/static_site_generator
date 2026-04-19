import unittest
from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):

    def test_html_props(self):
        node = HTMLNode("a", "google", None, {"class": "link"})
        
        self.assertEqual(
            node.tag,
            "a"
        )

        self.assertEqual(
            node.value,
            "google"
        )

        self.assertEqual(
            node.children,
            None
        )

        self.assertEqual(
            node.props,
            {'class': 'link'}
        )

    def test_to_html_props(self):
        node_props = {
            "href": "https://www.google.com",
            "target": "_blank" 
        }
        node = HTMLNode("a", "google", None, node_props)
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_html_repr(self):
        node = HTMLNode("a", "harry potter", None, {"class": "redirect", "href": "https://harrypotter.com"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(a, harry potter, children: None, {'class': 'redirect', 'href': 'https://harrypotter.com'})"
        )
