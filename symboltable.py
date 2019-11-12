# symbol-table.py
# Author: José Alexander Brenes Brenes
# A symbol table implementation using dictionaries

class SymbolTable:
	
	def __init__(self):
		self._HashTabel = dict()
	
	def lookup(self, symbol):
		return self._lookup(symbol)
	
	def _lookup(self, symbol):
		return symbol is in self._HashTabel #Se podría hacer con la función get() del diccionario
	
	def insert(self, symbol, data_type):
		if not self._lookup(symbol):
			self._insert(symbol, data_type)
			
	def _insert(self, symbol, data_type):
		self._HashTabel[symbol] = data_type