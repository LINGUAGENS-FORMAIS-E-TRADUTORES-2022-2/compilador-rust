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

        @abstractmethod
        def visitSignatureConcrete(self, signature):
              pass
        
        @abstractmethod
        def visitBodyStm(self, bodyStm):
              pass
        
        @abstractmethod
        def visitBodyorStm(self, bodyorStm):
              pass

        @abstractmethod
        def visitSemiStm(self, semiStm):
              pass
        
        @abstractmethod
        def visitassignStm(self, assignStm):
              pass

        @abstractmethod
        def visitStm2Stmm(self, tStm2Stmm):
              pass
 
        @abstractmethod
        def visitPlusExp(self, plusExp):
              pass       

        @abstractmethod
        def visitMinusExp(self, minusExp):
              pass       
        
        @abstractmethod
        def visitSlashExp(self, slashExp):
              pass       
        
        
        @abstractmethod
        def visitStarExp(self, starExp):
              pass    
        

        @abstractmethod
        def visitAndExp(self, andExp):
              pass    
        
        @abstractmethod
        def visitOrExp(self, orExp):
              pass    

        
        @abstractmethod
        def visitAssignExp(self, assignExp):
              pass    
        

        
        @abstractmethod
        def visitNeExp(self, neExp):
              pass    
        
        @abstractmethod
        def visitLtExp(self, ltExp):
              pass    
        
        
        @abstractmethod
        def visitGtExp(self, gtExp):
              pass    
        
        @abstractmethod
        def visitGeExpp(self, geExp):
              pass    
        @abstractmethod
        def visitLeExp(self, leExp):
              pass    
        
        @abstractmethod
        def visitAndAndExp(self, andandExp):
              pass    
        
        @abstractmethod
        def visitOrOrExp(self, ororExp):
              pass    
        
        @abstractmethod
        def visitNumberExp(self, numberExp):
              pass    
        
        @abstractmethod
        def visitIdExp(self, idExp):
              pass  
          
        @abstractmethod
        def visitEqExp(self, eqExp):
              pass     

        
        @abstractmethod
        def visitCaretExp(self, caretExp):
              pass  
            

        @abstractmethod
        def visitCallParams(self, callParams):
              pass  
          
        @abstractmethod
        def visitgOneParams(self, oneParams):
              pass       
        
        @abstractmethod
        def visitCallParams(self, callParams):
              pass  
          
        @abstractmethod
        def visitIntType(self, intType):
              pass       
        
        @abstractmethod
        def visitUIntType(self, uIntType):
              pass       
        
        @abstractmethod
        def visitStringType(self, stringType):
              pass       
        
        @abstractmethod
        def visitCharType(self, charType):
              pass       