import htmlnode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('a tag is required')
        if self.children is None:
            raise ValueError('a parent node must have children')
        
