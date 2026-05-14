from htmlnode import *
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('a tag is required')
        if self.children is None:
            raise ValueError('a parent node must have children')
        
        full_string = ''
        # child_string = ''
        if self.children:
            for child in self.children:
                child_string += f"<{child.tag} {child.props}>{child.value}</{child.tag}>"
            full_string += f"<{self.tag} {self.props}>{child_string}</{self.tag}>"
            return full_string
        
