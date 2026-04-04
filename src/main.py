from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType


def main():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(node)
    html_node = HTMLNode(
        props={
            "href": "https://www.google.com",
            "target": "_blank",
        }
    )

    print(html_node)


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Unsupported text node type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        splitted = node.text.split(delimiter)
        delim_indices = [i for i, char in enumerate(node.text) if char == delimiter]
        if len(delim_indices) % 2 != 0:
            raise SyntaxError("Invalid Markdown syntax. No closing item")

        idx = 0
        idx_in_delim_indices = 1

        for str in splitted:
            end = idx + len(str)

            if idx_in_delim_indices > len(delim_indices):
                new_list.append(TextNode(str, TextType.TEXT))
            else:
                if end == (delim_indices[idx_in_delim_indices]):
                    new_list.append(TextNode(str, text_type))
                    idx_in_delim_indices = idx_in_delim_indices + 2
                else:
                    new_list.append(TextNode(str, TextType.TEXT))

            idx = end + 1

    return new_list


if __name__ == "__main__":
    main()
