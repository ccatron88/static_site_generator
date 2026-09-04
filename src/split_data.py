from textnode import TextNode, TextType, text_node_to_html_node
from markdown_extractions import *

def split_nodes_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    split_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_list.append(node)
            continue
        if len(node.text.split(delimeter)) % 2 != 1:
            raise ValueError("Markdown characters require an open and closing delimeter (i.e. **word**)")
        else:
            split_str = node.text.split(delimeter)
            temp_list = []
            for i in range(0, len(split_str)):
                if split_str[i] == "":
                    continue
                if i % 2 == 0:
                    temp_list.append(TextNode(split_str[i], TextType.TEXT))
                else:
                    temp_list.append(TextNode(split_str[i], text_type))
            split_list.extend(temp_list)
    return split_list

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    images_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            images_list.append(node)
            continue
        extracted_images = extract_markdown_images(node.text)
        extracted_list = []
        for i in range(0, len(extracted_images)):
            str_text = node.text.split(extracted_images, 1)
            # for item in str_text:
            #     extracted_list.append(item, TextNode.text_type)
            extracted_list.append(str_text[0], TextType.TEXT)
            extracted_list.append(extracted_images[i,0], TextType.TEXT)
            # extracted_list.append(extracted_images[i,1], TextType.IMAGE)
            # extracted_list.append(str_text[2], TextType.TEXT)
        images_list.append(extracted_list)
    return images_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    split_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_list.append(node)
            continue
        if extract_markdown_links(node):
            extracted_link = extract_markdown_links(node)
            if extracted_link:
                split_list.append(node.split(extracted_link))
        return split_list
