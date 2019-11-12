# symboltable.py
# Author: José Alexander Brenes Brenes
# A symbol table implementation using dictionaries


class SymbolTable:

    # Se podría recibir por parámetro el enfoque
    # en el que se encuentra, si no
    # recibe nada entonces es 0
    def __init__(self):
        self._HashTable = {}
        self._scope = 0

    def lookup(self, symbol):
        return self._lookup(symbol)

    def _lookup(self, symbol):
        return self._HashTable.get(symbol)

    def insert(self, data_type, symbol=None):
		try:
			if symbol is None:
				self._add_scope(self._scope + 1, data_type)
				self._scope += 1
			elif not self._lookup(symbol):
				self._insert(data_type, symbol)
			else:
				raise Exception(f"Error - Line 'line': Double definition of 'variable'")

    def _insert(self, data_type, symbol):
        self._HashTable[symbol] = data_type

    def _add_scope(self, data_type, symbol):
        self._insert(data_type, SymbolTable())
