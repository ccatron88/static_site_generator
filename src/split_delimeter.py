from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    split_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_list.extend(node)
        if node.count(delimeter) != 2:
            raise ValueError("Markdown characters require an open and closing delimeter (i.e. **word**)")
        temp_list = node.split(sep=delimeter, maxsplit=2)
        for item in temp_list:
            split_list.extend(item, item.TextType)
    return split_list
            
