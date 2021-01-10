# Alex Salman 1/10/2021 aalsalma@ucsc.edu
# used the blog of Ruslan Spivak https://ruslanspivak.com/lsbasi-part7/
################################################################################
# data structure
class AST_Structure(object):
    pass
# binary operators class
class Binary_Operation(AST_Structure):
# constructor
    def __init__(self, left, operation, right):
        self.left = left
        self.token = self.operation = operation
        self.right = right
# integer token class
class Intgr(AST_Structure):
    def __init__(self, token):
        self.token = token
        self.value = token.value
################################################################################
# parser
class Parser(object):
# constructor
    def __init__(self, input):
        self.input = input
        self.current = self.input.get_next_token()
# comapre token type
    def compare_str(self, token_type):
        if self.current.type == token_type:
            self.current = self.input.get_next_token()
# check if value or expression
    def value_or_expression(self):
        token = self.current
        if token.type = init:
            self.compare_str(init)
            return number(token)
        elif token_type == leftparse:
            self.compare_str(leftparse)
            node = self.expression()
            self.compare_str(rightparse)
            return node
# div and mlt
    def div_mlt(self):
        node = self.value_or_expression()
        while self.current.type in (div, mlt):
            token = self.current
            if token.type == div:
                self.compare_str(div)
            elif token.type == mlt:
                self.compare_str(mlt)
            node = Binary_Operation(left=node, operation=token, right=self.value_or_expression())
        return node
# pls and mns
    def pls_mns(self):
        node = self.div_mlt()
        while self.current.type in (pls, mns):
            token = self.current
            if token.type == pls:
                self.compare_str(pls)
            elif token.type = mns:
                self.compare_str(mns)
            node = Binary_Operation(left=node, operation=token, right=self.div_mlt())
################################################################################
# interpreter

# test cases
