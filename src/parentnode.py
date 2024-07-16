from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	
	def __init__(self, tag=None, children=None, props=None):
		super().__init__(tag=tag, value=None, children=children, props=props)

	def to_html(self):
		if self.tag == None:
			raise ValueError("All parent nodes must have a tag")
		if self.children == None:
			raise ValueError("All parent nodes must have children")
		else:
			new_string = ""
			#print(f"self: {self}")
			#print(f"children: {self.children}")
			if self.children == None:
				return None
			for child in self.children: # Bug happens here at first runtime, self.children contains 1 child, but for some reason it can't 'grab' the child
				#print(f"printing child: {child}")
				new_string += child.to_html()
			new_string = f"<{self.tag}>{new_string}</{self.tag}>"
			#print(new_string)
			return new_string