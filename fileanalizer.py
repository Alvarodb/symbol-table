# fileAnalizer.py
# Author: José Alexander Brenes Brenes, Alvaro Delgado Brenes, Isaac Touma
# Description: ...

import sys
import re  # Regular Expression built-in
import symboltable
PATTERN = '\d+\.?\d+|\".*?\"|\'.*?\'|\"?\w+\"?|\(|\)|{|}'
BRACKET = '}'
RETURN = 'return'


class FileAnalizer:
    def __init__(self, file_path):
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
                    data_type = ''
                elif data_type:
                    self._insert(match[0], match[1], data_type)
                    data_type = ''
                elif not self._is_do_not_care(match[1]):
                    if not self._lookup(match[1]):
                        self._error_switch(
                            symboltable.NOT_DEC, match[1], match[0])
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
        line_counter = 1
        for line in self._handler:
            for word in re.findall(PATTERN, line):
                list.append((line_counter, word))
            line_counter += 1
        return list

    def _is_function(self, next):
        if next == '(':
            return True
        return False

    def _error_switch(self, error_id, name, line):
        switcher = {
            '1': f'Error - Line {line}: \'{name}\' has not been declared in the current scope\n',
            '2': f'Error - Line {line}: Return value does not match the function type of {name}',
            '6': f'Error - Line {line}: Double declaration of \'{name}\'\n'
        }
        self._error_string += switcher.get(error_id, 'Unknown error')

    def _is_do_not_care(self, match):
        if match == '{' or match == '}' or match == '(' or match == ')' or self._is_constant(match):
            return True
        return False

    def _is_constant(self, value):
        # Float or Integer value
        if self._data_type(value) == 'float' or self._data_type(value) == 'int':
            return True
        temp = re.findall('^\'.\'', value)  # Char value
        if temp:
            return True
        temp = re.findall('\".*?\"', value)  # String value
        if temp:
            return True
        return False

    def evaluate_function(self, name, data_type, list):
        function_type = data_type
        hash_table = symboltable.SymbolTable()
        hash_table.add_upper_scope(self._main_scope)
        values = (data_type, hash_table)
        self._main_scope.insert(values, name)
        while list:
            valor = list.pop(0)
            variable = valor[1]
            if variable == RETURN:
                self._check_return_func(
                    hash_table, list.pop(0)[1], valor[0], function_type, name)
            if variable is not BRACKET:
                if self._is_data_type(variable):
                    data_type = variable
                elif data_type and not self._is_data_type(variable) and not self._is_do_not_care(variable) and not self._is_structure(variable):
                    # A usar:
                    self._insert(valor[0], variable, data_type, hash_table)
                    data_type = ''
                    # Álvaro : hash_table.insert(datatype, variable)
                elif self._is_structure(variable):
                    return_ = self.create_structure(hash_table, valor, list)
                    if return_ is not None:
                        self._check_return_func(
                            hash_table, return_[1], return_[0], function_type, name)
                    # PENDIENTE
            else:
                break

    def create_structure(self, hash_table, match, list):
        hash_t = symboltable.SymbolTable()
        hash_t.add_upper_scope(hash_table)
        hash_t.concatenate_scopes(hash_table._upper_scopes)
        hash_table.insert((match[1]), (match[0], hash_t))
        data_type = ''
        to_return = None
        while list:
            match = list.pop(0)
            if match[1] == RETURN:
                return list.pop(0)
            if match[1] == BRACKET:
                break
            if self._is_data_type(match[1]):
                data_type = match[1]
            elif self._is_structure(match[1]):
                to_return = self.create_structure(hash_t, match, list)
                data_type = ''
            elif data_type:
                self._insert(match[0], match[1], data_type, hash_t)
                data_type = ''
            elif not self._is_do_not_care(match[1]):
                if not self._lookup(match[1], hash_t):
                    self._error_switch(
                        symboltable.NOT_DEC, match[1], match[0])
        return to_return

    def _check_return_func(self, hash_t, to_return, line, function_returns, function):
        return_tuple = hash_t._lookup(to_return)
        if return_tuple is not None:
            if return_tuple != function_returns:
                self._error_switch(str(symboltable.W_RTRN_TYPE),
                                   function, line)  # Exception
        else:
            # Returns a constant or a not defined value
            if function_returns != self._data_type(to_return):
                if self._data_type(to_return) is None:
                    self._error_switch(str(symboltable.NOT_DEC),
                                    to_return, line)  # Exception    
                self._error_switch(str(symboltable.W_RTRN_TYPE),
                                function, line)  # Exception

    def _data_type(self, to_return):
        data_type = re.findall('\".*?\"', to_return)
        if data_type:
            return 'string'
        data_type = re.findall('^\'.\'', to_return)
        if data_type:
            return 'char'
        data_type = re.findall('^[0-9]*$', to_return)
        if data_type:
            return 'int'
        data_type = re.findall('^\d*\.?\d*$', to_return)
        if data_type:
            return 'float'
        return None
