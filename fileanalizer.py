# fileAnalizer.py
# Author: José Alexander Brenes Brenes, Alvaro Delgado Brenes, Isaac Touma
# Description: ...

import sys
import re  # Regular Expression built-in
import symboltable

PATTERN = '\w+|\(|\)|{|}'
BRACKET = '}'


class FileAnalizer:
    def __init__(self, file_path):
        self._line = 1
        self._error_string = ''
        self._main_scope = symboltable.SymbolTable()
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

    def _list_analizer(self, list):
        data_type = ''
        while list:
            match = list.pop(0)
            if self._is_data_type(match[1]):
                data_type = match[1]
            elif self._is_structure(match[1]):
                self.create_structure(self._main_scope, match, list)
            elif list:
                if self._is_function(list[0][1]):
                    list.pop(0)
                    self.evaluate_function(match[1], data_type, list)
                elif data_type:
                    self._insert(match[0], match[1], data_type)
                elif not self._is_do_not_care(match[1]):
                    if not self._lookup(match[1]):
                        self._error_switch(symboltable.NOT_DEC, match[1], match[0])
            elif data_type:
                self._insert(match[0], match[1], data_type)
            elif not self._is_do_not_care(match[1]):
                self._lookup(match[1])
        print(self._error_string)
        print(self._main_scope)
        return not self._error_string

    def _lookup(self, symbol, current_scope=None):
        if current_scope is None:
            current_scope = self._main_scope
        if current_scope.lookup(symbol) is None:
            return False
        return True

    def _insert(self, line, symbol, data_type, table=None):
        if table is None:
            table = self._main_scope
        try:
            table.insert(data_type, symbol)
        except Exception as exception:
            self._error_switch(str(exception), symbol, line)

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

    def _error_switch(self, error_id, name, line):
        switcher = {
            '1': f'Error - Line {line}: \'{name}\' has not been declared in the current scope\n',
            '6': f'Error - Line {line}: Double declaration of \'{name}\'\n'
        }
        self._error_string += switcher.get(error_id, 'Unknown error')

    def _is_do_not_care(self, match):
        if match == '{' or match == '}' or match == '(' or match == ')' or match.isdigit():
            return True
        return False

    def evaluate_function(self, name, datatype, list):
        hash_table = symboltable.SymbolTable()
        hash_table.add_upper_scope(self._main_scope)
        values = (datatype, hash_table)
        self._main_scope.insert(values, name)
        while list:
            valor = list.pop(0)
            variable = valor[1]
            if variable is not BRACKET:
                if self._is_data_type(variable):
                    datatype = variable
                elif not self._is_data_type(variable) and not self._is_do_not_care(variable) and not self._is_structure(variable):
                    # A usar:
                    self._insert(valor[0], variable, datatype, hash_table)
                    # Álvaro : hash_table.insert(datatype, variable)
                elif self._is_structure(variable):
                    self.create_structure(hash_table, valor, list)
            else:
                break

    def create_structure(self, hash_table, match, list):
        hash_t = symboltable.SymbolTable()
        hash_t.add_upper_scope(hash_table)
        hash_t.concatenate_scopes(hash_table._upper_scopes)
        valor = list.pop(0)
        while valor[1] is not '}':
            if not self._is_do_not_care(valor[1]):
                # self._main_scope.lookup(valor[1]) is not None:
                if not self._lookup(valor[1], hash_t):
                    self._error_switch(
                        symboltable.NOT_DEC, valor[1], valor[0])
                else:
                    if self._is_data_type(valor[1]):
                        sig_valor = list.pop(0)
                        # A usar:
                        self._insert(
                            sig_valor[0], sig_valor[1], valor[1], hash_t)
                        # Isaac: hash_t.insert((sig_valor[1], valor[1]))
                    elif self._is_structure(valor[1]):
                        self.create_structure(hash_t, valor, list)
            valor = list.pop(0)
        hash_table.insert((match[1]), (match[0], hash_t))
