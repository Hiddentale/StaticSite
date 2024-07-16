from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	
	def __init__(self, tag, value, props=None):
		children = None
		super().__init__(tag, value, children, props)

	#def __iter__(self):
		#return self

	def to_html(self):
		if self.value == None:
			raise ValueError("All leaf nodes must have a value")
		if self.tag == None:
			return str(self.value)
		else:
			if self.props == None:
				return f"<{self.tag}>{self.value}</{self.tag}>"
			else:
				return f"<{self.tag}{self.props[0]}={self.props[1]}>{self.value}</{self.tag}>"
