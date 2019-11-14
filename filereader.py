# filereader.py
# Author: José Alexander Brenes Brenes, Alvaro Delgado Brenes, Isaac Touma Rodriguez
# Description: ...

import re  # Regular Expression built-in
import symboltable

LIMITS = ' |;|\n|\t'
FUNCTION = '\w+|\(|\)|{|}'
PARENTHESES = '('


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
        """
            Method that evaluates if the line read is equivalent to a funtion declaration
        """
        declaration = re.findall(FUNCTION,line)   #find all matches using FUNCTION RE 
        if PARENTHESES in declaration:  # if the line is a method declaration must include '('
            key = declaration[:2][1]    #function name
            values = (declaration[:2][0],symboltable.SymbolTable()) # (return type, SymbolTable of the function scope) 
            self._MainScope.insert(values,key)
            declaration.pop(0) #pop first and second element in declaration which correspond to return type and function name(already assigned)
            declaration.pop(0) 
            for index, element in enumerate(declaration): #next step is inserting the parameters of the function in the SymbolTable of the scope
                if self._is_data_type(element):
                    symbol = declaration[index + 1]
                    self._MainScope._HashTable[key][1].insert(element,symbol)     
            return True
        return False
    
    

