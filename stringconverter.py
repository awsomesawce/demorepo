#!/usr/bin/env python
# Use ``%run`` to run from inside a jupyter console.
# This is similar to how IDLE runs a script, as it keeps the variables
# inside the IPython session for further examination.

"""A string converter that converts a string into various other formats"""

from collections import UserString
from typing import AnyStr, Text

from stringlistprinter import print_string_list

class StringConverter(UserString):
    
    '''A custom string class with extra conversion and encoding methods'''
    
    def convert_to_binary(self):
        '''Converts self to a list of binary numbers using the bin() method'''
        l = [bin(ord(letter)) for letter in self.data]
        return l

    # IMPORTANT: Can I recurse methods here?

    def convert_to_ordinal(self):
        l = []
        for letter in self.data:
            l.append(ord(letter))
        return l

    def conv_to_ord(self):
        '''Convert string to list of ordinals using list comprehension.'''
        l = [ord(x) for x in self.data]
        return l

    def conv_to_markdown(self):
        '''Take the string and convert the markdown to html'''
        raise NotImplementedError('This function is not implemented yet')

    def _print_self(self):
        '''Simply prints self'''
        print(self)

    def _print_dir(self):
        '''Prints dir(self)'''
        print(dir(self))


class NewString(str):
    '''Most basic string class'''
    pass

if __name__ == '__main__':
    # TODO: Cleanup
    
    print(f'Running {__file__}')
    sc = StringConverter('my new string\n')
    #print(sc.convert_to_binary())
    ns = NewString("hi there")
    print(dir(ns))
    #sc.conv_to_markdown() # Not implemented yet.
    
