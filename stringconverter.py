#!/usr/bin/env python

"""A string converter that converts a string into various other formats"""

from collections import UserString
from stringlistprinter import print_string_list

class StringConverter(UserString):
    
    '''A custom string class with extra conversion and encoding methods'''
    
    def convert_to_binary(self):
        '''Converts self to a list of binary numbers using the bin() method'''
        l = []
        for letter in self.data:
            l.append(bin(ord(letter)))
        return l

    def print_self(self):
        '''Simply prints self'''
        print(self)

    def print_dir(self):
        '''Prints dir(self)'''
        print(dir(self))

if __name__ == '__main__':
    sc = StringConverter('my new string\n')
    sc_binary_list = sc.convert_to_binary()
    print_string_list(sc_binary_list)
    sc2 = StringConverter('hi')
    sc2_binary_list = sc2.convert_to_binary()
    
