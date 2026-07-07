from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    split_list = []
    delimeters = ["_", "**", "`"]
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_list.extend(node)
        if node.text_type in delimeters:
