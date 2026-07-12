from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimeter(old_nodes: list[TextNode], delimeter: str, text_type: TextType) -> list[TextNode]:
    split_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            split_list.extend(node)
        if node.text.count(delimeter) != 2:
            raise ValueError("Markdown characters require an open and closing delimeter (i.e. **word**)")
        temp_list = node.text.split(sep=delimeter, maxsplit=2)
        for item in temp_list:
            if item[0] is delimeter:
                new_node = ""
                if delimeter == "`":
                    new_node = TextNode(item, TextType.CODE)
                elif delimeter == "**":
                    new_node = TextNode(item, TextType.BOLD)
                elif delimeter == "_":
                    new_node = TextNode(item, TextType.ITALIC)
                split_list.extend(new_node, new_node.TextType)
    return split_list
            
