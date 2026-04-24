from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("all tags must have a value")
        
        return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>") if self.tag != None else (f"{self.value}")
    
    def __repr__(self):
        return (f"LeafNode({self.tag}, {self.value}, {self.props})")
