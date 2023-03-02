import ply.lex as lex

reservadas = {
  'as' : 'AS',
  'async' : 'ASYNC',
  'await' : 'AWAIT',
  'break' : 'BREAK',
  'const' : 'CONST',
  'continue' : 'CONTINUE',
  'crate' : 'CRATE',
  'dyn' : 'DYN',
  'else' : 'ELSE',
  'enum' : 'ENUM',
  'extern' : 'EXTERN',
  'false' : 'FALSE',
  'fn' : 'FN',
  'for' : 'FOR',
  'if' : 'IF',
  'impl' : 'IMPL',
  'in' : 'IN',
  'let' : 'LET',
  'loop' : 'LOOP',
  'match' : 'MATCH',
  'mod' : 'MOD',
  'move' : 'MOVE',
  'mut' : 'MUT',
  'pub' : 'PUB',
  'ref' : 'REF',
  'return' : 'RETURN',
  'Self' : 'SELFUPERCASE',
  'self' : 'SELFLOWERCASE',
  'static' : 'STATIC',
  'struct' : 'STRUCT',
  'super' : 'SUPER',
  'trait' : 'TRAIT',
  'true' : 'TRUE',
  'type' : 'TYPE',
  'union' : 'UNION',
  'unsafe' : 'UNSAFE',
  'use' : 'USE',
  'where' : 'WHERE',
  'while' : 'WHILE'
}


tokens = [ 
  'PLUS',
  'MINUS',
  'STAR',
  'SLASH',
  'PERCENT',
  'CARET',
  'NOT',
  'AND',
  'OR',
  'ANDAND',
  'OROR',
  'SHL',
  'SHR',
  'PLUSEQ',
  'MINUSEQ',
  'STAREQ',
  'SLASHEQ',
  'PERCENTEQ',
  'CARETEQ',
  'ANDEQ',
  'OREQ',
  'SHLEQ',
  'SHREQ',
  'EQ',
  'EQEQ',
  'NE',
  'GT',
  'LT',
  'GE',
  'LE',
  'AT',
  'UNDERSCORE',
  'DOT',
  'DOTDOT',
  'DOTDOTDOT',
  'DOTDOTEQ',
  'COMMA',
  'SEMI',
  'COLON',
  'PATHSEP',
  'RARROW',
  'FATARROW',
  'POUND',
  'DOLLAR',
  'QUESTION',
  'TILDE'
] + list(reservadas.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_PERCENT = r'%'
t_CARET = r'\^'
t_NOT = r'!'
t_AND = r'&'
t_OR = r'\|'
t_ANDAND = r'&&'
t_OROR = r'\|\|'
t_SHL = r'<<'
t_SHR = r'>>'
t_PLUSEQ = r'\+='
t_MINUSEQ = r'-='
t_STAREQ = r'\*='
t_SLASHEQ = r'/='
t_PERCENTEQ = r'%='
t_CARETEQ = r'^='
t_ANDEQ = r'&='
t_OREQ = r'\|='
t_SHLEQ = r'<<='
t_SHREQ = r'>>='
t_EQ = r'='
t_EQEQ = r'=='
t_NE = r'!='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_AT = r'@'
t_UNDERSCORE = r'_'
t_DOT = r'.'
t_DOTDOT = r'..'
t_DOTDOTDOT = r'...'
t_DOTDOTEQ = r'..='
t_COMMA = r','
t_SEMI = r';'
t_COLON = r':'
t_PATHSEP = r'::'
t_RARROW = r'->'
t_FATARROW = r'=>'
t_POUND = r'\#'
t_QUESTION = r'\?'
t_TILDE = r'~'
t_DOLLAR = r'\$'




def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reservadas.get(t.value,'ID')
   return t

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

def t_LINE_COMENT(t):
  r'//.*'
  t.lexer.skip(1)

t_ignore = ' \t'

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)

lexer = lex.lex()
lexer.input('''
as
async
await
break
const
continue
crate
dyn
else
enum
extern
false
fn
for
if
impl
in
let
loop
match
mod
move
mut
pub
ref
return
Self
self
static
struct
super
trait
true
type
union
unsafe
use
where
while
...
// Isso aqui é um comentário
// outro comentário
else // Esse é um comentário depois de uma palavra reservada
else //Esse é um comentário 328472 depois de uma palavra reservada sem o espaço e com numeros
''')
for tok in lexer:
  print(tok.type, tok.value, tok.lineno, tok.lexpos)
