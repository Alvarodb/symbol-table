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
        if '(' in declaration: # if the line is a method declaration
            key = declaration[:2][1]
            values = (declaration[:2][0],symboltable.SymbolTable())
            self._MainScope.insert(values,key)
            declaration.pop(0) #cochino
            declaration.pop(0) #vomitada perro
            for index, element in enumerate(declaration):
                if self._is_data_type(element):
                    symbol = declaration[index + 1]
                    self._MainScope._HashTable[key][1].insert(element,symbol)   
                print(self._MainScope._HashTable[key][1]._HashTable)    
            return True
        return False
       
    

