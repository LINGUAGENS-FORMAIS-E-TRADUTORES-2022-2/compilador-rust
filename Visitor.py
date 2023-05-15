from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *

tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor():
        def visitFuncDeclConcrete(self, funcDeclConcrete):
             funcDeclConcrete.signature.accept(self)
             funcDeclConcrete.body.accept(self)



