from textnode import TextNode, TextType, text_node_to_html_node

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
                if i % 2 == 0:
                    temp_list.append(TextNode(split_str[i], TextType.TEXT))
                else:
                    temp_list.append(TextNode(split_str[i], text_type))
            split_list.extend(temp_list)
    return split_list



    #     temp_list = node.text.split(sep=delimeter, maxsplit=2)
    #     for item in temp_list:
    #         if item[0] is delimeter:
    #             new_node = ""
    #             if delimeter == "`":
    #                 new_node = TextNode(item, TextType.CODE)
    #                 split_list.extend([new_node])
    #             elif delimeter == "**":
    #                 new_node = TextNode(item, TextType.BOLD)
    #                 split_list.extend([new_node])
    #             elif delimeter == "_":
    #                 new_node = TextNode(item, TextType.ITALIC)
    #                 split_list.extend([new_node])
    #         split_list.extend([item])
    # return split_list
            
# node = TextNode(split_str[i], TextType.TEXT)
# temp_list.append(node)

# if delimeter == "`":
#     # node = TextNode(split_str[i], TextType.CODE)
#     # temp_list.append(node)
#     temp_list.append(TextNode(split_str[i], TextType.CODE))
# elif delimeter == "**":
#     # node = TextNode(split_str[i], TextType.BOLD)
#     # temp_list.append(node)
#     temp_list.append(TextNode(split_str[i], TextType.BOLD))
# elif delimeter == "_":
#     # node = TextNode(split_str[i], TextType.ITALIC)
#     # temp_list.append(node)
#     temp_list.append(TextNode(split_str[i], TextType.ITALIC))
