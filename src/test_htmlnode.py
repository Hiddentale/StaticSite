import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_url_none(self):
        node = HTMLNode("This is a html node", "bold", None)
        node2 = HTMLNode("This is a html node", "bold")
        self.assertEqual(node, node2)
    def test_text_type_diff(self):
        node = HTMLNode("This is a html node", "bold")
        node2 = HTMLNode("This is a html node", "bald")
        self.assertNotEqual(node, node2)
    def test_text_diff(self):
        node = HTMLNode("This is a html", "bold")
        node2 = HTMLNode("This is a html node", "bold")
        self.assertNotEqual(node, node2)
    def test_props_to_html(self):
        node = HTMLNode("This is a html", "bold", ["a", "b"], {"href": "https://www.google.com", "target": "_blank"})
        test_string = 'href="https://www.google.com" target="_blank" '
        html_string = node.props_to_html()
        self.assertEqual(html_string, test_string)

if __name__ == "__main__":
    unittest.main()