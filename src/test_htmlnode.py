import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        child_node = HTMLNode("div", "test", [], {})
        node = HTMLNode(
            "a",
            "testvalue",
            [child_node],
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        node2 = HTMLNode(
            "a",
            "testvalue",
            [child_node],
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        self.assertEqual(node, node2)

    def test_eq_defaults(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_empty_string_when_no_props(self):
        node = HTMLNode("a", "test")
        self.assertEqual("", node.props_to_html())

    def test_str_for_props(self):
        node = HTMLNode(
            "a",
            "testvalue",
            [],
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )

        self.assertEqual(
            ' href="https://www.google.com" target="_blank" ', node.props_to_html()
        )
