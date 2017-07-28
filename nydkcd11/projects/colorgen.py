import random
colors = [
	'#231f20',
	'#003366',
	'#b49759',
	'#00aeef',
	'#f58025',
	'#91381e',
	'#c41230',
	'#ec008c',
	'#729849',
	'#fed450',
	'#94829c',
	'#cbc42d',
	'#7d90aa',
	'#8bcfba',
	'#f5b419',
]
colors_2 = [
	'rgba(35,31,32, 0.3)',
	'rgba(0,47,95, 0.3)',
	'rgba(180,151,90, 0.3)',
	'rgba(0,174,239, 0.3)',
	'rgba(245,128,37, 0.3)',
	'rgba(145,56,31, 0.3)',
	'rgba(196,18,48, 0.3)',
	'rgba(236,0,140, 0.3)',
	'rgba(115,152,73, 0.3)',
	'rgba(255,210,79, 0.3)',
]
def hexgen():
	return colors[random.randint(0, len(colors)-1)]
def rgbagen():
	return colors_2[random.randint(0,len(colors_2)-1)]
