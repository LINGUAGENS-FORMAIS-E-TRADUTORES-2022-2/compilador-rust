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
    
class Declvar(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DecDeclvar(Declvar):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitDecDeclvar(self)
    


class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SinglParams(SigParams):
    def __init__(self, type, id):
        self.type = type
        self.id = id
    def accept(self, visitor):
        return visitor.visitSinglParams(self)
    
class CompoundParams(SigParams):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class WhileStm(Stm):
    def __init__(self, exp, bodyorstm):
        self.exp = exp
        self.bodyorstm = bodyorstm
    def accept(self, visitor):
        return visitor.visitWhileStm(self)
    
class IfStm(Stm):
    def __init__(self, exp, bodyorstm):
        self.exp = exp
        self.bodyorstm = bodyorstm
    def accept(self, visitor):
        return visitor.visitIfStm(self)

class If2Stm(Stm):
    def __init__(self, exp, bodyorstm, stm):
        self.exp = exp
        self.bodyorstm = bodyorstm
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitIf2Stm(self)

class ForStm(Stm):
    def __init__(self,stm2, body):
        self.stm2 = stm2
        self.body = body
    def accept(self, visitor):
        return visitor.visitForStm(self)
    
class For2Stm(Stm):
    def __init__(self, body):
        self.body = body
    def accept(self, visitor):
        return visitor.visitFor2Stm(self)
    
class ReturnStm(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitreturnStm(self)
    
class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleStm(Stms):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitSingleStm(self)

class CompoundStm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitCompoundStm(self)
    

    

class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SignatureConcrete(Signature):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitSignatureConcrete(self)
    

class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BodyStm(Body):
    def __init__(self, stms):
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitBodyStm(self)

class BodyorStm(Body):
    def __init__(self, stms):
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitBodyorStm(self)
    
class SemiStm(Body):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSemiStm(self)
    
class AssignStm(Body):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitAssignStm(self)

class Stm2Stm(Body):
    def __init__(self, exp1, exp2):
        self.exp = exp1
        self.exp = exp2
    def accept(self, visitor):
        return visitor.visitStm2Stm(self)

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class PlusExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitPlusExp(self)
    
class MinusExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMinusExp(self)


class SlashExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitSlashExp(self)
    
class StarExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitStarExp(self)
    
class AndExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAndExp(self)
    
class CaretExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitCaretExp(self)
    
class OrExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitOrExp(self)
    
class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAssignExp(self)
    

class PercentExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitPercentExp(self)

class NeExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitNeExp(self)
    
class LtExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitLtExp(self)
    
class GtExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept (self, visitor):
        return visitor.visitGtExp(self)

class GeExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept (self, visitor):
        return visitor.visitGeExp(self)

class LeExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept (self, visitor):
        return visitor.visitLeExp(self)
    
class AndAndExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp1 = exp2
    def accept (self, visitor):
        return visitor.visitAndAndExp(self)

class OrOrExp (Exp):
    def __init__ (self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accpet (self, visitor):
        return visitor.visitOrOrExp (self)

class NumberExp (Exp):
    def __init__ (self, num):
        self.num = num
    def accpet (self, visitor):
        return visitor.visitNumberExp (self)
    
class IdExp (Exp):
    def __init__ (self, id):
        self.id = id
    def accpet (self, visitor):
        return visitor.visitIdExp (self)
    
    
class CallExp (Exp):
    def __init__ (self, call):
        self.call = call
    def accpet (self, visitor):
        return visitor.visitCallExp (self)
    
class EqExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitEqExp(self)
    

    
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallParams (Exp):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def accept (self, visitor):
        return visitor.visitCallParams(self)
    
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
    
class Tipo (metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class IntType(Tipo):
    def __init__(self, intTipo):
        self.exp = intTipo
    def accept(self, visitor):
        return visitor.visitIntType(self)
    
class UIntType(Tipo):
    def __init__(self, uIntTipo):
        self.exp = uIntTipo
    def accept(self, visitor):
        return visitor.visitUIntType(self)

class FloatType(Tipo):
    def __init__(self, floatTipo):
        self.exp = floatTipo
    def accept(self, visitor):
        return visitor.visitFloatType(self)
    
class StringType(Tipo):
    def __init__(self, stringTipo):
        self.exp = stringTipo
    def accept(self, visitor):
        return visitor.visitStringType(self)
    
class CharType(Tipo):
    def __init__(self, charTipo):
        self.exp = charTipo
    def accept(self, visitor):
        return visitor.visitCharType(self)
    
