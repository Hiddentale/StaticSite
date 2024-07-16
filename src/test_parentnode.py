import unittest

from parentnode import ParentNode
from leafnode import LeafNode


def test_url_none():
    node = ParentNode("p",
        [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
    print(node.to_html())

    node1 = ParentNode("p",
                        [LeafNode(None, "Normal text")])
    print(node1.to_html())

    node2 = ParentNode("p", 
                       [ParentNode("a", 
                                   [LeafNode(None, "Normal text")])])
    print(node2.to_html())
    #node3 = ParentNode("a")
    #print(node3.to_html())
    node3 = ParentNode("p",
                        [ParentNode("z", [LeafNode(None, "Normal text")]), LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
    print(node3.to_html())

    return None

test_url_none()