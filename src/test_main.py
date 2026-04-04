import unittest

from main import split_nodes_delimiter, text_node_to_html_node
from textnode import TextNode, TextType


class TestMain(unittest.TestCase):
    def test_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_to_html_node_bold(self):
        node = TextNode("Bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text node")

    def test_to_html_node_italic(self):
        node = TextNode("Italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text node")

    def test_to_html_node_code(self):
        node = TextNode("Code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text node")

    def test_to_html_node_link(self):
        node = TextNode("Link text node", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text node")
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props["href"], "https://google.com")

    def test_to_html_node_image(self):
        node = TextNode("Image text node", TextType.IMAGE, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertIsNotNone(html_node.props)
        self.assertEqual(html_node.props["src"], node.url)
        self.assertEqual(html_node.props["alt"], node.text)

    def test_to_html_node_unknown(self):
        node = TextNode("Unknown text node", None)
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)

        self.assertEqual(str(cm.exception), "Unsupported text node type: None")

    def test_split_nodes_code_single(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertIsNotNone(new_nodes)
        self.assertEqual(len(new_nodes), 3)

        print(new_nodes)
        code_node = new_nodes[1]
        self.assertEqual(code_node.text_type, TextType.CODE)

    def test_split_nodes_code_multiple(self):
        node = TextNode(
            "This is text with a `code block` word and another `python code block`",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertIsNotNone(new_nodes)
        self.assertEqual(len(new_nodes), 5)

        code_node = new_nodes[1]
        self.assertEqual(code_node.text_type, TextType.CODE)

        second_code_node = new_nodes[3]
        self.assertEqual(second_code_node.text_type, TextType.CODE)

    def test_split_nodes_no_matching_close_delimiter(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(SyntaxError) as cm:
            split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(str(cm.exception), "Invalid Markdown syntax. No closing item")

    # def test_split_nodes_multiple_nodes
