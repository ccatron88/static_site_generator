from enum import Enum

class TextType(Enum):
    TEXT = 'text'
    BOLD_TEXT = '**Bold text**'
    ITALIC_TEXT = '_Italic text_'
    CODE_TEXT = '`Code text`'
    LINK = '[anchor text](url)'
    IMAGE = '![alt text](url)'

class TextNode:
    def __init__(self, text, text_type, url = None): 
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __hash__(self):
        return hash((self.text, self.text_type, self.url))    

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return NotImplemented
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"{self.text} {self.text_type.value} {self.url}"
