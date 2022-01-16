# Generated from ..\dlv\grammar_input\DLVLexerInput.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("r\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\7\fZ\n\f\f\f\16")
        buf.write("\f]\13\f\3\r\3\r\7\ra\n\r\f\r\16\rd\13\r\3\r\3\r\3\16")
        buf.write("\3\16\3\17\5\17k\n\17\3\17\3\17\3\20\3\20\3\21\3\21\2")
        buf.write("\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\2!\21\3\2\b\4\2C\\c|\6\2\62;C")
        buf.write("\\aac|\5\2\f\f\17\17$$\3\2\17\17\3\2\f\f\5\2\13\13\16")
        buf.write("\16\"\"\2s\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5\'\3")
        buf.write("\2\2\2\7.\3\2\2\2\t;\3\2\2\2\13?\3\2\2\2\rM\3\2\2\2\17")
        buf.write("O\3\2\2\2\21Q\3\2\2\2\23S\3\2\2\2\25U\3\2\2\2\27W\3\2")
        buf.write("\2\2\31^\3\2\2\2\33g\3\2\2\2\35j\3\2\2\2\37n\3\2\2\2!")
        buf.write("p\3\2\2\2#$\5\37\20\2$%\3\2\2\2%&\b\2\2\2&\4\3\2\2\2\'")
        buf.write("(\7u\2\2()\7e\2\2)*\7j\2\2*+\7g\2\2+,\7o\2\2,-\7c\2\2")
        buf.write("-\6\3\2\2\2./\7c\2\2/\60\7p\2\2\60\61\7e\2\2\61\62\7g")
        buf.write("\2\2\62\63\7u\2\2\63\64\7v\2\2\64\65\7q\2\2\65\66\7t\2")
        buf.write("\2\66\67\7a\2\2\678\7m\2\289\7g\2\29:\7{\2\2:\b\3\2\2")
        buf.write("\2;<\7m\2\2<=\7g\2\2=>\7{\2\2>\n\3\2\2\2?@\7c\2\2@A\7")
        buf.write("w\2\2AB\7v\2\2BC\7q\2\2CD\7k\2\2DE\7p\2\2EF\7e\2\2FG\7")
        buf.write("t\2\2GH\7g\2\2HI\7o\2\2IJ\7g\2\2JK\7p\2\2KL\7v\2\2L\f")
        buf.write("\3\2\2\2MN\7.\2\2N\16\3\2\2\2OP\7*\2\2P\20\3\2\2\2QR\7")
        buf.write("+\2\2R\22\3\2\2\2ST\7]\2\2T\24\3\2\2\2UV\7_\2\2V\26\3")
        buf.write("\2\2\2W[\t\2\2\2XZ\t\3\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2")
        buf.write("\2[\\\3\2\2\2\\\30\3\2\2\2][\3\2\2\2^b\7$\2\2_a\n\4\2")
        buf.write("\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2d")
        buf.write("b\3\2\2\2ef\7$\2\2f\32\3\2\2\2gh\7\'\2\2h\34\3\2\2\2i")
        buf.write("k\t\5\2\2ji\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\t\6\2\2m\36")
        buf.write("\3\2\2\2no\t\7\2\2o \3\2\2\2pq\13\2\2\2q\"\3\2\2\2\6\2")
        buf.write("[bj\3\b\2\2")
        return buf.getvalue()


class DLVLexerInput(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WHITESPACE = 1
    SCHEMA_KEY_LABEL = 2
    ANCESTOR_KEY_LABEL = 3
    KEY_LABEL = 4
    KEY_AUTOINCREMENT = 5
    COMMA = 6
    OPEN_ROUND_BRACKET = 7
    CLOSE_ROUND_BRACKET = 8
    OPEN_SQUARE_BRACKET = 9
    CLOSE_SQUARE_BRACKET = 10
    NAME = 11
    STRING = 12
    COMMENT_BEGIN = 13
    NEW_LINE_SYMBOL = 14
    ANY = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'schema'", "'ancestor_key'", "'key'", "'autoincrement'", "','", 
            "'('", "')'", "'['", "']'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "WHITESPACE", "SCHEMA_KEY_LABEL", "ANCESTOR_KEY_LABEL", "KEY_LABEL", 
            "KEY_AUTOINCREMENT", "COMMA", "OPEN_ROUND_BRACKET", "CLOSE_ROUND_BRACKET", 
            "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", "NAME", "STRING", 
            "COMMENT_BEGIN", "NEW_LINE_SYMBOL", "ANY" ]

    ruleNames = [ "WHITESPACE", "SCHEMA_KEY_LABEL", "ANCESTOR_KEY_LABEL", 
                  "KEY_LABEL", "KEY_AUTOINCREMENT", "COMMA", "OPEN_ROUND_BRACKET", 
                  "CLOSE_ROUND_BRACKET", "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", 
                  "NAME", "STRING", "COMMENT_BEGIN", "NEW_LINE_SYMBOL", 
                  "WS", "ANY" ]

    grammarFileName = "DLVLexerInput.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


