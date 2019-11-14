# fileAnalizer.py
# Author: José Alexander Brenes Brenes, Alvaro Delgado Brenes, Isaac Touma
# Description: ...

import re  # Regular Expression built-in
import symboltable

PATTERN = '\w+|\(|\)|{|}'
BRACKET = '}'

class FileAnalizer:
	def __init__(self, file_path):
		self._line = 1
		self._error_string = ''
		self._MainScope = symboltable.SymbolTable()
		self._open_file(file_path)

	def _open_file(self, file_path):
		try:
			self._handler = open(file_path, 'r')
		except IOError as open_file_exception:
			print(open_file_exception)
			exit()

	def read(self):
		return self._read()

	def _is_data_type(self, string):
		if string == 'char' or string == 'int' or string == 'float' or string == 'string':
			return True
		return False

	def _is_structure(self, string):
		if string == 'if' or string == 'while':
			return True
		return False

	def _evaluate_parameters(self, data_type, function, file_queue):
		function_scope = symboltable.SymbolTable()
		# Guarda el _MainScope como enfoque superior
		function_scope._scope.insert(self._MainScope)
	
	def _list_analizer(self, list):
		data_type = ''
		while list:
			match = list.pop(0)
			if self._is_data_type(match[1]):
				data_type = match[1]
			elif self._is_structure(match[1]):
				pass  # Isaac
			elif list:
				if self._is_function(list[0][1]):
					list.pop(0)
					self.evaluate_function(match[1], data_type,list)
				elif data_type:
					self._insert(match[1], data_type)
			elif data_type:
				self._insert(match, data_type)
			elif not self._is_do_not_care(match):
				self._lookup(match)

	def _lookup(self, symbol, current_scope=None):
		if current_scope is None:
			current_scope = self._MainScope
		if current_scope.lookup(symbol) is None:
			return False
		return True

	def _insert(self, symbol, data_type, table=None):
		if table is None:
			table = self._MainScope
		table.insert(data_type, symbol)

	def analize(self):
		self._analize()

	def _analize(self):
		self._list_analizer(self._read())

	def _read(self):
		list = []
		for line in self._handler:
			for word in re.findall(PATTERN, line):
				list.append((self._line, word))
			self._line += 1
		return list

	def _is_function(self, next):
		if next == '(':
			return True
		return False

	def _error_switch(self, error_id, name):
		switcher = {
			'1': f'Error - Line {self._line}: \'{name}\' has not been declared in the current scope\n',
			'6': f'Error - Line {self._line}: Double declaration of \'{name}\'\n'
		}
		self._error_string += switcher.get(error_id, 'Unknown error')

	def _is_do_not_care(self, match):
		if match == '{' or match == '}' or match == '(' or match == ')':
			return True
		return False

	def evaluate_function(self, name, datatype, list):
		key = name
		hashTable = symboltable.SymbolTable()
		values = (datatype, hashTable)
		self._MainScope.insert(values, key)
		while list:
			variable = list.pop(0)[1]
			if variable is not BRACKET:
				if self._is_data_type(variable):
					datatype = variable
				elif not self._is_data_type(variable) and not self._is_do_not_care(variable) and not self._is_structure(variable):
					hashTable.insert(datatype, variable)
				elif self._is_structure(variable):
					break
					# isaac con hastable math list
				else:
					break
