# Alex Salman 1/10/2021 aalsalma@ucsc.edu
# used the blog of Ruslan Spivak https://ruslanspivak.com/lsbasi-part7/
################################################################################

################################################################################
INTEGER, pls, mns, mlt, div, leftparentheses, rightparentheses, EOF = (
'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', '(', ')', 'EOF')
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
        if token.type == INTEGER:
            self.str_compare(INTEGER)
            return Number(token)
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
                self.str_compare(pls)
            elif token.type == mns:
                self.str_compare(mns)
            node = Binary_Operation(left=node, operation=token, right=self.mlt_div())
        return node
# parse pls_mns
    def parse_pls_mns(self):
        return self.pls_mns()
################################################################################
# interpreter for tree traversal, AST
class Node(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter(Node):
# constructor
    def __init__(self, parsing_node):
        self.parsing_node = parsing_node
# check if children equels either of the arithmatic operations
    def visit_Binary_Operation(self, node):
        if node.operation.type == pls:
            return self.visit(node.left) + self.visit(node.right)
        elif node.operation.type == mns:
            return self.visit(node.left) - self.visit(node.right)
        elif node.operation.type == div:
            return self.visit(node.left) / self.visit(node.right)
        elif node.operation.type == mlt:
            return self.visit(node.left) * self.visit(node.right)
# get number value
    def visit_Number(self, node):
        return node.value

    def interpreter(self):
        ast_tree = self.parsing_node.parse_pls_mns()
        return self.visit(ast_tree)
################################################################################
# tokenizer
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()

class Tokenizer(object):
# constructor
    def __init__(self, user_input):
        self.user_input = user_input
        self.pos = 0
        self.current_char = self.user_input[self.pos]

    def syntax_error(self):
        raise Exception('You have an invalid character . . ')
# advance the pointer
    def advance(self):
        self.pos += 1
        if self.pos > len(self.user_input) - 1:
            self.current_char = None
        else:
            self.current_char = self.user_input[self.pos]

    def a_space(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.a_space()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == '+':
                self.advance()
                return Token(pls, '+')
            if self.current_char == '-':
                self.advance()
                return Token(mns, '-')
            if self.current_char == '*':
                self.advance()
                return Token(mlt, '*')
            if self.current_char == '/':
                self.advance()
                return Token(div, '/')
            if self.current_char == '(':
                self.advance()
                return Token(leftparentheses, '(')
            if self.current_char == ')':
                self.advance()
                return Token(rightparentheses, ')')
            self.error()
        return Token(EOF, None)
################################################################################
# main
def main():
    user_input = input ("Arith >> ")
    #user_input = "2 + 7 * 3 / 4"
    token = Tokenizer(user_input)
    parsing_node = Parser(token)
    interpreter = Interpreter(parsing_node)
    to_print = interpreter.interpreter()
    print(to_print)

if __name__ == '__main__':
    main()
