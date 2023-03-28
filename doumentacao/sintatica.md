program → funcdecl | 
          funcdecl program |
          declvar | decvar program

declvar →   let assign ';' |
            let mut assign ';'

funcdecl → signature body

signature → fn ID ""("" sigParams ")"

sigparams → ID ':'  tipo | 
            ID ':'  tipo "," sigparams

body → "{" stms "}"

bodyorstm → stm | body

stms → stm  | 
       stm  stms

stm → exp ";" |
      WHILE exp bodyorstm| 
      IF exp bodyorstm |
      IF exp bodyorstm ELSE stm |
      FOR ID 'in' stm2 body |
      FOR ID 'in' ID body |
      return exp ";" |
      
stm2 → '(' exp..exp ')'|
       '(' exp..exp ')'.rev()


call → ID "(" params ")"

exp → exp "+" exp |
      exp "-" exp |
      exp "*" exp |
      exp "^" exp |
      exp "/" exp |
      exp "%" exp |
      exp "&" exp |
      exp "|" exp |
      exp ">=" exp |
      exp ">" exp |
      exp "<=" exp |
      exp "<" exp |
      exp "as" exp |
      exp "is" exp |
      exp "is!" exp |
      exp "==" exp |
      exp "!=" exp |
      exp "&&" exp |
      exp "||" exp |
      exp "??" exp |
      exp "expr1 ? expr2 : expr3" exp |
      exp ".. ?.." |
      exp "=" exp |
      exp "*=" exp |
      exp "/=" exp |
      exp "+=" exp | 
      exp "-=" exp |
      exp "&=" exp |
      exp "^=" exp |
      call | 
      assign | 
      NUM | 
      ID

call → ID "("params")" | 
       ID "(" ")"

params → exp"," params | 
         exp

assign → ID "=" exp

tipo → 'i32' | 'u32' | 'f32' | 'String' | 'char'
