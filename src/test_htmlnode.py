import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "test")
        self.assertEqual("test", node.to_html())

    def test_leaf_to_html_raise_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        children = []
        for i in range(5):
            leaf = LeafNode("li", i)
            children.append(leaf)

        parent = ParentNode("ul", children)

        self.assertEqual(
            parent.to_html(),
            "<ul><li>0</li><li>1</li><li>2</li><li>3</li><li>4</li></ul>",
        )

    def test_to_html_raise_no_tag(self):
        parent = ParentNode(None, [])

        with self.assertRaises(ValueError) as cm:
            parent.to_html()

        self.assertEqual(str(cm.exception), "Tag is not set")

    def test_to_html_raise_no_children(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            parent.to_html()

        self.assertEqual(str(cm.exception), "Children are not set")
