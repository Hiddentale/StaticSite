import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_url_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_text_type_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bald")
        self.assertNotEqual(node, node2)
    def test_text_diff(self):
        node = TextNode("This is a text", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
