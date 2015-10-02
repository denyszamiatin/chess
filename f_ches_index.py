__author__ = 'rosto'

def ches_indexes(ver, hor):
	"""this function convert index -1
	>>> ches_indexes(1, 1)
	'a1'
	"""
	vertikal = '12345678'
	horisontal = 'abcdefgh'
	desk = [[h + v for h in horisontal] for v in vertikal]
	return desk[ver-1][hor-1]

