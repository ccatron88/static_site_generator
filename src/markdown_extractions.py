from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    images_re = re.findall(r"\[([A-Za-z]w+)\]\(w+\)", text)
    return images_re
