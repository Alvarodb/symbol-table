# filereader.py
# Author: José Alexander Brenes Brenes
# Description: ...

import re  # Regular Expression built-in
import symboltable

LIMITS = ' |;|\n|\t'
FUNCTION = '\w+|\(|\)|{|}'


class FileReader:
    def __init__(self, file_path):
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
        if (string == 'char' or string == 'int' or string == 'float' or string == 'string'):
            return True
        return False

    def _read(self):
        for line in self._handler:
            if not self.evaluate_function(line):
                for word in re.split(LIMITS, line):
                    if word:
                        if self._is_data_type(word):
                            symbol = re.split(LIMITS, line).pop(
                                re.split(LIMITS, line).index(word) + 1)
                            self._MainScope.insert(word, symbol)
        print(self._MainScope._HashTable)

    def evaluate_function(self, line):
        declaration = re.findall(FUNCTION,line)
        if '(' in declaration:
            #for element in declaration:
            self._MainScope.insert(declaration[:2][0],(declaration[:2][1],symboltable.SymbolTable()))
            return True
        return False
       
    

