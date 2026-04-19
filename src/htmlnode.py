
class HtmlNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_props_string = ''
        if self.props is None or self.props is '':
            return ''
        for (key, value) in self.props:
            string += f" {key}='{value}' "
        return html_props_string
    
    def __repr__(self):
        node = HtmlNode(self.tag, self.value, self.children, self.props)
        print(f"{node.tag},\n{node.value},\n{node.children},\n{node.props}")
