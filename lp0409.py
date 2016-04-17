
def bold(s):
	def wrapped():
		return '<b>' + s() + '</b>'
	return wrapped

@bold
def hw():
	return "hello,world"

print(hw())