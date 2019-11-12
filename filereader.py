# filereader.py
# Author: José Alexander Brenes Brenes
# Description: ...

import re  # Regular Expression built-in
import symboltable

LIMITS = ' |;|\(|\)|\n|\t'

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
        

    def _read(self):
        c = 0
        for line in self._handler:
            for word in re.split(LIMITS, line):
                if word:
                    print(word)
                    
