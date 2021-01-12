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
class Number(AST_Structure):
    def __init__(self, token):
        self.token = token
        self.value = token.value
################################################################################
# parser
class Parser(object):
# constructor
    def __init__(self, lexer):
        self.lexer = lexer
        self.current = self.lexer.get_next_token()
# error catcher
    def syntax_error(self):
        raise Exception('You have a syntax error . . ')
# comapre token type
    def str_compare(self, token_type):
        if self.current.type == token_type:
            self.current = self.lexer.get_next_token()
        else:
            self.syntax_error()
# check if value or expression
    def value_or_expression(self):
        token = self.current
        if token.type = INTEGER:
            self.str_compare(INTEGER)
            return number(token)
        elif token_type == leftparentheses:
            self.str_compare(leftparentheses)
            node = self.expression()
            self.str_compare(rightparentheses)
            return node
# div and mlt
    def mlt_div(self):
        node = self.value_or_expression()
        while self.current.type in (mlt, div):
            token = self.current
            if token.type == mlt:
                self.str_compare(mlt)
            elif token.type == div:
                self.str_compare(div)
            node = Binary_Operation(left=node, operation=token, right=self.value_or_expression())
        return node
# pls and mns
    def pls_mns(self):
        node = self.mlt_div()
        while self.current.type in (pls, mns):
            token = self.current
            if token.type == pls:
                self.compare_str(pls)
            elif token.type = mns:
                self.compare_str(mns)
            node = Binary_Operation(left=node, operation=token, right=self.mlt_div())
        return node
# parse pls_mns
    def parse_pls_mns(self):
        return self.pls_mns()
################################################################################
# interpreter for tree traversal, AST
class Interpreter(object):
# constructor
    def __init__(self, parse_pls_mns):
        self.parsing_node = parsing_node
# check if children equels either of the arithmatic operations
    def interpret_Binary_Operation(self, node):
        if node.operation.type == pls:
            return self.node.left + self.node.right
        elif node.operation.type == mns:
            return self.node.left - self.node.right
        elif node.operation.type == div:
            return self.node.left / self.node.right
        elif node.operation.type == mlt:
            return self.node.left * self.node.right
# get number value
    def number_value(self, node):
        return node.value

    def interpreter(self):
        ast_tree = self.parsing_node.parse_pls_mns()
        return = ast_tree

################################################################################
# main
def main():
    # user_input = input ("Arith >> ")
    user_input = "2 + 7 * 3"
    token = Lexer(user_input)
    parsing_node = Parser(token)
    interpreter = Interpreter(parsing_node)
    res = interpreter.interpreter()
    print(res)

if __name__ == '__main__':
    main()
# test cases
