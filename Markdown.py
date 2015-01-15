#!/usr/local/bin/python
# coding: utf-8
# -------------------------------------------------
# @author wangxin ScottFoH
# @update 2014-1-15
# -------------------------------------------------

import sys

print ''
if len(sys.argv) == 1:
    print("Using test.md as default.")
    filename = 'test.md'
else:
    filename = sys.argv[1]
print ''

tokens = (
    'H1','H2','H3','LSB','RSB','LB','RB',
    'LT','GT','STAR','UDL','MINUS',
    'PLUS','EXCLAM','EQ','DOT','BLANK',
    'QQ','CR','TAB','NUMBER','WORD'
    )

# Tokens
t_H1 = r'\# '
t_H2 = r'\#\# '
t_H3 = r'\#\#\# '
t_LSB = r'\['
t_RSB = r'\]'
t_LB = r'\('
t_RB = r'\)'
t_LT = r'<'
t_GT = r'>'
t_STAR = r'\*'
t_UDL = r'_'
t_MINUS = r'-'
t_PLUS = r'\+'
t_EXCLAM = r'!'
t_EQ = r'='
t_DOT = r'\.'
t_BLANK = r'[ ]'
t_QQ = r'\`'
t_CR = r'\n'
t_TAB = r'\t'
t_NUMBER = r'[0-9]+'
t_WORD = r'[a-zA-Z,:?/\\\'\"]+'



t_ignore = ""


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import re
import ply.lex as lex
lexer = lex.lex(reflags = re.UNICODE)

# Test lexer
lexer.input(open(filename).read())
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok
print ''

# ------------------------------------
# definitions of parsing rules by yacc
# ------------------------------------
precedence = (

    )
names = {}



import ply.yacc as yacc
yaccer = yacc.yacc(method = "SLR")

if __name__ == '__main__':
    result = yaccer.parse(open(filename).read(), debug = 0)
    print result

if len(sys.argv) == 3:
    out = file(sys.argv[2], 'w')
    out.write(result)
    print('Saved to file ' + sys.argv[2])
    out.close()

print ''