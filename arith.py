# Alex Salman 1/10/2021 aalsalma@ucsc.edu

# data structure - used the structure of https://ruslanspivak.com/lsbasi-part7/
class AST_Structure(object):
    pass
# binary operators class
class Binary_Operation(AST_Structure):
    def __init__(self, left, operation, right):
        self.left = left
        self.token = self.operation = operation
        self.right = right
# integer token class
class Integer(AST_Structure):
    def __init__(self, token):
        self.token = token
        self.value = token.value


# parser

# interpreter

# test cases
