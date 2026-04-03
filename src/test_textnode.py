import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_default_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "some_url")
        node2 = TextNode("This is a text node2", TextType.BOLD, "some_url")
        self.assertNotEqual(node, node2)

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "some_url")
        node2 = TextNode("This is a text node", TextType.BOLD, "some_url")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
