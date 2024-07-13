class TextNode():

	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, secondary_object):
		if (self.text == secondary_object.text and
			self.text_type == secondary_object.text_type and
			self.url == secondary_object.url):
			return True
		else:
			return False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"
