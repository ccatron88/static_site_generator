from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('a tag is required')
        if self.children is None:
            raise ValueError('a parent node must have children')
        
        if self.children:
            return (f"<{self.tag}>{self.to_html(self.children)}</{self.tag}>")
        return (f"<{self.tag}>{self.children}</{self.tag}>")
