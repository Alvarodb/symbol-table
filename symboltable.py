# symboltable.py
# Author: José Alexander Brenes Brenes, Alvaro Delgado, Isaac Touma
# A symbol table implementation using dictionaries

"""
1 El identificador {identificador} no está declarado en este enfoque.
6 Doble declaración de identificador {identificador}.
"""
NOT_DEC = '1'
DOUBLE_DEC = '6'


class SymbolTable:

    def __init__(self):
        self._HashTable = {}
        self._scope = []

    def __repr__(self):
        return str(self._HashTable)

    def lookup(self, symbol):
        return self._lookup(symbol)

    def _lookup(self, symbol):
        if self._HashTable.get(symbol) is not None:
            return self._HashTable.get(symbol)
        for element in self._scope:
            if element.get(symbol):
                return element
        return None

    def insert(self, data_type, symbol):
        if self._lookup(symbol) is None:
            self._insert(data_type, symbol)

    def _insert(self, data_type, symbol):
        self._HashTable[symbol] = data_type