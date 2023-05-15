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

        def visitMinusExp(self, minusExp):
              minusExp.exp1.accept(self)
              print(' - ', end='')
              minusExp.exp2.accept(self)

        def visitPlusExp(self, plusExp):
              plusExp.exp1.accept(self)
              print(' + ', end='')
              plusExp.exp2.accept(self)

        def visitSlashExp(self,  slashExp):
            slashExp.exp1.accept(self)
            print(' / ', end='')
            slashExp.exp2.accept(self)


        def visitStarExp(self,  starExp):
            starExp.exp1.accept(self)
            print(' * ', end='')
            starExp.exp2.accept(self)

        def visitAndExp(self, andExp):
            andExp.exp1.accept(self)
            print(' & ', end='')
            andExp.exp2.accept(self)

        def visitAndAndExp(self, andandExp):
            andandExp.exp1.accept(self)
            print(' && ', end='')
            andandExp.exp2.accept(self)


        def visitOrOrExp(self, ororExp):
            ororExp.exp1.accept(self)
            print(' || ', end='')
            ororExp.exp2.accept(self)

        def visitOrExp(self, orExp):
            orExp.exp1.accept(self)
            print(' | ', end='')
            orExp.exp2.accept(self)

        def visitCaretExp(self, caretExp):
            caretExp.exp1.accept(self)
            print(' ^ ', end='')
            caretExp.exp2.accept(self)

        def visitAssignExp(self,  assignStm):
            assignStm.exp1.accept(self)
            print(' = ', end='')
            assignStm.exp2.accept(self)

        def visitNeExp(self,  neExp):
            neExp.exp1.accept(self)
            print(' != ', end='')
            neExp.exp2.accept(self)

        def visitLtExp(self,  ltExp):
            ltExp.exp1.accept(self)
            print(' < ', end='')
            ltExp.exp2.accept(self)

        def visiGtExp(self,  gtExp):
            gtExp.exp1.accept(self)
            print(' > ', end='')
            gtExp.exp2.accept(self)

        def visitLeExp(self,  leExp):
            leExp.exp1.accept(self)
            print(' <= ', end='')
            leExp.exp2.accept(self)

        def visiGeExp(self,  geExp):
            geExp.exp1.accept(self)
            print(' >= ', end='')
            geExp.exp2.accept(self)

        def visitNumberExp(self, numberExp):
            print(numberExp.num, end='')
            