from abc import abstractmethod
from abc import ABC

class FuncDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitFuncDeclConcrete(self)
    
class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class PlusExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.PlusExp(self)
    
class MinusExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.MinusExp(self)


class SlashExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.SlashExp(self)
    
class StarExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.StarExp(self)
    
class AndExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.AndExp(self)
    
class CaretExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.CaretExp(self)
    
class OrExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.OrExp(self)
    
class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.AssignEx(self)
    
class NeExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.NeExp(self)
    
class LtExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.LtExp(self)
    
class GtExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept (self, visitor):
        return visitor.GtExp(self)

class GeExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept (self, visitor):
        return visitor.GeExp(self)

class LeExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept (self, visitor):
        return visitor.LeExp(self)
    
class AndAndExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp1 = exp2
    def accept (self, visitor):
        return visitor.AndAndExp(self)

class OrOrExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accpet (self, visitor):
        return visitor.OrOrExp (self)

class NumberExp (Exp):
    def __init__ (self, num):
        self.num = num
    def accpet (self, visitor):
        return visitor.NumberExp (self)
    
class IdExp (Exp):
    def __init__ (self, id):
        self.id = id
    def accpet (self, visitor):
        return visitor.IdExp (self)
    
class CallExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp1 = exp2
    def accept (self, visitor):
        return visitor.CallExp(self)
    
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class OneParams(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitgOneParams(self)

class MoreParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitMoreParams(self)

    
