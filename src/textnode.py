class TextNode():

	def __init__(self, text, text_type, url):
		self.text = text
		self.text_type = text_type
		self.url = url

	def ___eq__(self, secondary_object):
		if (self.text == secondary_object.text and
			self.text_type == secondary_object.text_type and
			self.url == secondary_object.url):
			return True
		else:
			return False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}. {self.url})"


def main():
	dummy_object = TextNode("This is a text node", "bold", "https://www.boot.dev")
	print(dummy_object)

main()
