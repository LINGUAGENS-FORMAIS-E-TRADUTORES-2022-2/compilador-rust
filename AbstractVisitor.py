from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):
       
        @abstractmethod
        def visitFuncDeclConcrete(self, funcDecl):
              pass
        
        @abstractmethod
        def visitDecDeclvar(self, declvar):
              pass
        
        @abstractmethod
        def visitiSinglParams(self, singlParams):
              pass
        
        @abstractmethod
        def visitCompoundStm(self, compoundStm):
              pass
        
        
        @abstractmethod
        def visitSingleStm(self, singleStm):
              pass
               
        @abstractmethod
        def visitCompoundStm(self, compoundStm):
              pass
                     

