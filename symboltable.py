# symboltable.py
# Author: José Alexander Brenes Brenes, Alvaro Delgado, Isaac Touma
# A symbol table implementation using dictionaries

"""
1 El identificador {identificador} no está declarado en este enfoque.
6 Doble declaración de identificador {identificador}.
"""
NOT_DEC = '1'
DOUBLE_DEC = '6'
W_RTRN_TYPE = '3'
class SymbolTable:

    def __init__(self):
        self._hash_table = {}
        self._upper_scopes = []

    def __repr__(self):
        return str(self._hash_table)

    def lookup(self, symbol):
        return self._lookup(symbol)

    def _lookup(self, symbol):
        for upper_scope in self._upper_scopes:
            if upper_scope._lookup(symbol):
                return upper_scope._lookup(symbol)
        if self._hash_table.get(symbol) is not None:
            return self._hash_table.get(symbol)
        return None

    def insert(self, data_type, symbol):
        if self._lookup(symbol) is None:
            self._insert(data_type, symbol)
        else:
            raise Exception(DOUBLE_DEC)

    def concatenate_scopes(self, upper_scope):
        self.__concatenate_scopes(upper_scope)

    def _insert(self, data_type, symbol):
        self._hash_table[symbol] = data_type
    
    def add_upper_scope(self, upper_scope):
        self._upper_scopes.append(upper_scope)

    def __concatenate_scopes(self, upper_scope):
        self._upper_scopes = self._upper_scopes + upper_scope

    