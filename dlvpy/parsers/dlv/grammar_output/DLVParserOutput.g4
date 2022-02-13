parser grammar DLVParserOutput;

options {tokenVocab=DLVLexerOutput;}

output  : answer_set*;
answer_set: model #SimpleModel|
            BEGIN_BEST_MODEL? model cost #ModelWithCost |
            query_literal (COMMA query_literal)* BEGIN_GROUND_QUERY REASONING BOOLEAN (DOT | witness) #QueryGround |
            term (COMMA term)* #QueryNonGround;
model     : OPEN_BRACE (literal (COMMA literal)*)? CLOSE_BRACE;
query_literal: NEGATION_AS_FAILURE? literal;
literal   : TRUE_NEGATION? atom;
atom      : NAME (OPEN_ROUND_BRACKET term (COMMA term)* CLOSE_ROUND_BRACKET)?;
term      : STRING | INTEGER | atom | OPEN_SQUARE_BRACKET (term (COMMA term)*)? CLOSE_SQUARE_BRACKET;
witness   : BEGIN_WITNESS model;
cost      : BEGIN_COST cost_amount (COMMA cost_amount)* END_COST;
cost_amount: OPEN_SQUARE_BRACKET INTEGER COLON INTEGER CLOSE_SQUARE_BRACKET;
