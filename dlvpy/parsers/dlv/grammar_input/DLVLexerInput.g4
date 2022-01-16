lexer grammar DLVLexerInput;

WHITESPACE: WS-> skip;

SCHEMA_KEY_LABEL: 'schema';
ANCESTOR_KEY_LABEL: 'ancestor_key';
KEY_LABEL: 'key';
KEY_AUTOINCREMENT: 'autoincrement';

COMMA               : ',';
OPEN_ROUND_BRACKET  : '(';
CLOSE_ROUND_BRACKET   : ')';
OPEN_SQUARE_BRACKET : '[';
CLOSE_SQUARE_BRACKET: ']';

NAME  : [a-zA-Z][a-zA-Z0-9_]*;
STRING : '"'~["\r\n]*'"';

COMMENT_BEGIN: '%';

NEW_LINE_SYMBOL: [\r]?[\n];

fragment WS: [ \t\u000C];

ANY: .;