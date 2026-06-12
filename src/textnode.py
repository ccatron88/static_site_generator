from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None): 
        self.text = text
        self.text_type = text_type
        self.url = url

    def __hash__(self):
        return hash((self.text, self.text_type, self.url))    

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text 
            and self.text_type == other.text_type 
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def text_node_to_html_node(text_node: TextNode) -> LeafNode:
        if not isinstance(text_node, TextNode):
            raise TypeError("text_node is not type TextNode")
        return LeafNode(text_node.tag, text_node.value, text_node.props).to_html()
