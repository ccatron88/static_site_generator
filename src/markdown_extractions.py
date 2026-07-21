from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    # img_tuples = []
    # img_alt_txt = re.findall(r"\[([\w+ ]+)\]", text)
    # img_url = re.findall(r"\w+\:\/\/[\/\w.]+", text)

    # img_tuples.append((img_alt_txt[0], img_url[0]))

    img_list = re.findall(r"\[(\w+ )\]\(\w+\:\/\/\w.+", text)

    return img_list
