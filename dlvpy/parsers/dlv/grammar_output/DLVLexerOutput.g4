lexer grammar DLVLexerOutput;

HEADER: 'DLV ['.*?']'-> skip;
WHITESPACE      : WS-> skip;

COMMA               : ',';
COLON               : ':';
OPEN_ROUND_BRACKET  : '(';
CLOSE_ROUND_BRACKET   : ')';
OPEN_BRACE          : '{';
CLOSE_BRACE           : '}';
OPEN_SQUARE_BRACKET : '[';
CLOSE_SQUARE_BRACKET: ']';
TRUE_NEGATION: [-~];
NEGATION_AS_FAILURE: 'not';

STRING : '"'~["\r\n]*'"';
NAME  : [a-zA-Z][a-zA-Z0-9_]*;
INTEGER: '0'|[1-9][0-9]*;

BEGIN_BEST_MODEL    : 'Best model:';
BEGIN_COST          : 'Cost ([Weight:Level]): <';
END_COST            : '>';

BEGIN_GROUND_QUERY: ' is '-> mode(GROUND_QUERY);

mode GROUND_QUERY;
REASONING                   : 'bravely'|'cautiously';
BOOLEAN                     : 'false'|'true';
GROUND_QUERY_WHITESPACE     : WS-> skip;
DOT                         : '.'-> mode(DEFAULT_MODE);
BEGIN_WITNESS               : ', evidenced by'-> mode(DEFAULT_MODE);

fragment WS: [ \t\r\n\u000C];