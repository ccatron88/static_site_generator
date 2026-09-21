from textnode import TextNode, TextType, text_node_to_html_node
from markdown_extractions import extract_markdown_links, extract_markdown_images

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
        remaining_text = node.text

        for i in range(0, len(extracted_images)):
            extract_string = (f"![{extracted_images[i][0]}]({extracted_images[i][1]})")
            str_text = remaining_text.split(extract_string, 1)

            if str_text[0] != "":
                images_list.append(TextNode(str_text[0], TextType.TEXT))
            images_list.append(TextNode(extracted_images[i][0], TextType.IMAGE, extracted_images[i][1]))

            remaining_text = str_text[1]

        if remaining_text:
            images_list.append(TextNode(remaining_text, TextType.TEXT))
    return images_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    links_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            links_list.append(node)
            continue
        extracted_links = extract_markdown_links(node.text)
        remaining_text = node.text

        for i in range(0, len(extracted_links)):
            extract_string = (f"[{extracted_links[i][0]}]({extracted_links[i][1]})")
            str_text = remaining_text.split(extract_string, 1)

            if str_text[0] != "":
                links_list.append(TextNode(str_text[0], TextType.TEXT))
            links_list.append(TextNode(extracted_links[i][0], TextType.LINK, extracted_links[i][1]))

            remaining_text = str_text[1]

        if remaining_text:
            links_list.append(TextNode(remaining_text, TextType.TEXT))
    return links_list

def text_to_textnodes(text):
    textNodes = [TextNode(text, TextType.TEXT)]
#     delimiters_list = [
#         ("**", TextType.BOLD),
#         ("_", TextType.ITALIC),
#         ("`", TextType.CODE)
#         ]

#     for i in range(0, len(delimiters_list)):
#         textNodes = split_nodes_delimeter(textNodes, delimiters_list[i][0], delimiters_list[i][1])

#     textNodes = split_nodes_image(textNodes)
#     textNodes =split_nodes_link(textNodes)

    return textNodes
