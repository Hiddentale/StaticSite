class HTMLNode():
	
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		text_to_print = ""
		for key,value in self.props.items():
			text_to_print += f'{key}="{value}" '
		return text_to_print
	
	def __repr__(self) -> str:
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"
	
	def __eq__(self, other):
		if isinstance(other, HTMLNode):
			return (self.tag == other.tag) and \
				(self.value == other.value) and \
				(self.children == other.children) and \
				(self.props == other.props)
		else:
			return False
		
	def __ne__(self, other):
		return not self.__eq__(other)