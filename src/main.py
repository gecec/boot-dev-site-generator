from htmlnode import HTMLNode
from textnode import TextNode


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


if __name__ == "__main__":
    main()
