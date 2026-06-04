import json

BOARDS = {}

def SimpleEncoderFunc(obj):
	return obj.__dict__

class Board:
	def __init__(self, name):
		self.columns = []
		self.name = name

	def asJSON(self):
		return json.JSONEncoder(default=SimpleEncoderFunc).encode(self)

class Column:
	def __init__(self, name):
		self.cards = []
		self.name = name

	def asJSON(self):
		return json.JSONEncoder(default=SimpleEncoderFunc).encode(self)

class Card():
	def __init__(self, title, description, points=0, priority = 0):
		self.title = title
		self.description = description
		self.points = points
		self.priority = priority

	def asJSON(self):
		return json.JSONEncoder(default=SimpleEncoderFunc).encode(self)

def BoardFromJSON(jsonDict):
	board = Board(jsonDict["name"])
	for column in jsonDict["columns"]:
		objColumn = Column(column["name"])
		board.columns.append(objColumn)
		for card in column["cards"]:
			objColumn.cards.append(Card(card["title"], card["description"]))
	return board

def GetBoard(id):
	try:
		return BOARDS[id]
	except KeyError:
		return {"error": "no such board"}

default_board = Board("default")
default_column = Column("to-do")
default_card = Card("first step", "add more stuff")
default_board.columns.append(default_column)
default_column.cards.append(default_card)
BOARDS[1] = default_board