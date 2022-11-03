import sys
from spi import Lexer, Parser, Interpreter

text = open(sys.argv[1], 'r').read()

lexer = Lexer(text)
parser = Parser(lexer)
interpreter = Interpreter(parser)
result = interpreter.interpret()

for k, v in sorted(interpreter.GLOBAL_SCOPE.items()):
        print('{} = {}'.format(k, v))
