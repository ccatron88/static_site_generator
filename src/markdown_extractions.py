from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    img_list = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', text)

    return img_list

def extract_markdown_links(text):
    links_list = re.findall(r'\[([^\]]*)\]\(([^\)]+)\)', text)

    return links_list
