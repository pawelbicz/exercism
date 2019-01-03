import string
import re


class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True


def parse(input_string):
    key = take_key(input_string)
    if key == [';']:
        return SgfTree()
    val = take_value(input_string)
    properties = {key: val}
    print(properties)
    return SgfTree(properties=properties)


def take_key(text):
    l_value_parent = []
    key = re.findall(r';\w*', text)
    if key == []:
        raise ValueError('Incorrect input')
    if key == [';']:
        return key
    print(key[0][1::])
    for i in key[0][1::]:
        if i in string.ascii_lowercase:
            raise ValueError('Lower Case detected!')
    for x in re.finditer('\[', text):
        l_value_parent.append(text[x.end()])
    if len(l_value_parent) is 0:
        raise ValueError('Incorrect input')
    print('!', key, l_value_parent)
    return key[0][1::]


def take_value(text):
    l_value_parent = []
    for x in re.finditer('\[', text):
        l_value_parent.append(text[x.end()])
    if len(l_value_parent) is 0:
        raise ValueError('Incorrect input')
    return l_value_parent

# def check_uppercase(text):
#     text_new = ''
#     for i in text:
#         if i in string.ascii_lowercase:
#             raise ValueError('Lower Case detected')
# parse('(;)')
# parse('(;Aa[b])')
parse(';A[B];B[C]')

