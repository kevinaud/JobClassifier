from context import classifier

class TestClass:
	def test_one(self):
		x = "this"
		assert 'h' in x

	def test_two(self):
		x = "hello"
		assert len(x) == 5
