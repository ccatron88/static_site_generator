from textnode import TextNode, TextType

print('hello world')

def main():
    text_node = TextNode("On the Nature of Daylight", TextType.LINK, "https://en.wikipedia.org/wiki/On_the_Nature_of_Daylight")
    print(text_node)

main()
