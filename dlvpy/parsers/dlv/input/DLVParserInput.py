# Generated from ..\dlv\grammar_input\DLVParserInput.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("n\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2\16\2")
        buf.write("\33\13\2\3\2\3\2\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\5\3&")
        buf.write("\n\3\3\3\3\3\3\4\3\4\5\4,\n\4\3\4\7\4/\n\4\f\4\16\4\62")
        buf.write("\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5;\n\5\f\5\16\5>\13")
        buf.write("\5\3\5\3\5\3\5\7\5C\n\5\f\5\16\5F\13\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\5\bV\n\b\3\b")
        buf.write("\3\b\5\bZ\n\b\3\t\3\t\3\t\3\t\7\t`\n\t\f\t\16\tc\13\t")
        buf.write("\3\t\3\t\3\t\5\th\n\t\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4")
        buf.write("\6\b\n\f\16\20\22\24\2\4\3\2\20\20\4\2\4\7\r\r\2n\2\31")
        buf.write("\3\2\2\2\4%\3\2\2\2\6)\3\2\2\2\b\63\3\2\2\2\nJ\3\2\2\2")
        buf.write("\fO\3\2\2\2\16Q\3\2\2\2\20[\3\2\2\2\22i\3\2\2\2\24k\3")
        buf.write("\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\33\3\2\2\2\31\27")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34")
        buf.write("\35\7\2\2\3\35\3\3\2\2\2\36&\5\6\4\2\37!\n\2\2\2 \37\3")
        buf.write("\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#&\3\2\2\2$\"\3")
        buf.write("\2\2\2%\36\3\2\2\2%\"\3\2\2\2&\'\3\2\2\2\'(\7\20\2\2(")
        buf.write("\5\3\2\2\2)+\7\17\2\2*,\5\b\5\2+*\3\2\2\2+,\3\2\2\2,\60")
        buf.write("\3\2\2\2-/\n\2\2\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\7\3\2\2\2\62\60\3\2\2\2\63\64\7\4\2\2\64")
        buf.write("\65\7\t\2\2\65\66\5\f\7\2\66<\7\t\2\2\678\5\n\6\289\7")
        buf.write("\b\2\29;\3\2\2\2:\67\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2")
        buf.write("\2\2=?\3\2\2\2><\3\2\2\2?D\5\16\b\2@A\7\b\2\2AC\7\16\2")
        buf.write("\2B@\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2F")
        buf.write("D\3\2\2\2GH\7\n\2\2HI\7\n\2\2I\t\3\2\2\2JK\7\5\2\2KL\7")
        buf.write("\t\2\2LM\5\f\7\2MN\7\n\2\2N\13\3\2\2\2OP\t\3\2\2P\r\3")
        buf.write("\2\2\2QY\7\6\2\2RU\7\t\2\2SV\5\24\13\2TV\5\20\t\2US\3")
        buf.write("\2\2\2UT\3\2\2\2VW\3\2\2\2WX\7\n\2\2XZ\3\2\2\2YR\3\2\2")
        buf.write("\2YZ\3\2\2\2Z\17\3\2\2\2[\\\7\13\2\2\\a\7\16\2\2]^\7\b")
        buf.write("\2\2^`\7\16\2\2_]\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2")
        buf.write("\2bd\3\2\2\2ca\3\2\2\2dg\7\f\2\2ef\7\b\2\2fh\5\22\n\2")
        buf.write("ge\3\2\2\2gh\3\2\2\2h\21\3\2\2\2ij\7\16\2\2j\23\3\2\2")
        buf.write("\2kl\7\7\2\2l\25\3\2\2\2\r\31\"%+\60<DUYag")
        return buf.getvalue()


class DLVParserInput ( Parser ):

    grammarFileName = "DLVParserInput.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'schema'", "'ancestor_key'", 
                     "'key'", "'autoincrement'", "','", "'('", "')'", "'['", 
                     "']'", "<INVALID>", "<INVALID>", "'%'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "SCHEMA_KEY_LABEL", "ANCESTOR_KEY_LABEL", 
                      "KEY_LABEL", "KEY_AUTOINCREMENT", "COMMA", "OPEN_ROUND_BRACKET", 
                      "CLOSE_ROUND_BRACKET", "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", 
                      "NAME", "STRING", "COMMENT_BEGIN", "NEW_LINE_SYMBOL", 
                      "ANY" ]

    RULE_codeinput = 0
    RULE_line = 1
    RULE_comment = 2
    RULE_schema = 3
    RULE_ancestor_key = 4
    RULE_name = 5
    RULE_key = 6
    RULE_key_properties = 7
    RULE_key_concat = 8
    RULE_key_autoincrement = 9

    ruleNames =  [ "codeinput", "line", "comment", "schema", "ancestor_key", 
                   "name", "key", "key_properties", "key_concat", "key_autoincrement" ]

    EOF = Token.EOF
    WHITESPACE=1
    SCHEMA_KEY_LABEL=2
    ANCESTOR_KEY_LABEL=3
    KEY_LABEL=4
    KEY_AUTOINCREMENT=5
    COMMA=6
    OPEN_ROUND_BRACKET=7
    CLOSE_ROUND_BRACKET=8
    OPEN_SQUARE_BRACKET=9
    CLOSE_SQUARE_BRACKET=10
    NAME=11
    STRING=12
    COMMENT_BEGIN=13
    NEW_LINE_SYMBOL=14
    ANY=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CodeinputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DLVParserInput.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserInput.LineContext)
            else:
                return self.getTypedRuleContext(DLVParserInput.LineContext,i)


        def getRuleIndex(self):
            return DLVParserInput.RULE_codeinput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeinput" ):
                listener.enterCodeinput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeinput" ):
                listener.exitCodeinput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCodeinput" ):
                return visitor.visitCodeinput(self)
            else:
                return visitor.visitChildren(self)




    def codeinput(self):

        localctx = DLVParserInput.CodeinputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_codeinput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DLVParserInput.WHITESPACE) | (1 << DLVParserInput.SCHEMA_KEY_LABEL) | (1 << DLVParserInput.ANCESTOR_KEY_LABEL) | (1 << DLVParserInput.KEY_LABEL) | (1 << DLVParserInput.KEY_AUTOINCREMENT) | (1 << DLVParserInput.COMMA) | (1 << DLVParserInput.OPEN_ROUND_BRACKET) | (1 << DLVParserInput.CLOSE_ROUND_BRACKET) | (1 << DLVParserInput.OPEN_SQUARE_BRACKET) | (1 << DLVParserInput.CLOSE_SQUARE_BRACKET) | (1 << DLVParserInput.NAME) | (1 << DLVParserInput.STRING) | (1 << DLVParserInput.COMMENT_BEGIN) | (1 << DLVParserInput.NEW_LINE_SYMBOL) | (1 << DLVParserInput.ANY))) != 0):
                self.state = 20
                self.line()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(DLVParserInput.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW_LINE_SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserInput.NEW_LINE_SYMBOL)
            else:
                return self.getToken(DLVParserInput.NEW_LINE_SYMBOL, i)

        def comment(self):
            return self.getTypedRuleContext(DLVParserInput.CommentContext,0)


        def getRuleIndex(self):
            return DLVParserInput.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = DLVParserInput.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 28
                self.comment()
                pass

            elif la_ == 2:
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DLVParserInput.WHITESPACE) | (1 << DLVParserInput.SCHEMA_KEY_LABEL) | (1 << DLVParserInput.ANCESTOR_KEY_LABEL) | (1 << DLVParserInput.KEY_LABEL) | (1 << DLVParserInput.KEY_AUTOINCREMENT) | (1 << DLVParserInput.COMMA) | (1 << DLVParserInput.OPEN_ROUND_BRACKET) | (1 << DLVParserInput.CLOSE_ROUND_BRACKET) | (1 << DLVParserInput.OPEN_SQUARE_BRACKET) | (1 << DLVParserInput.CLOSE_SQUARE_BRACKET) | (1 << DLVParserInput.NAME) | (1 << DLVParserInput.STRING) | (1 << DLVParserInput.COMMENT_BEGIN) | (1 << DLVParserInput.ANY))) != 0):
                    self.state = 29
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==DLVParserInput.NEW_LINE_SYMBOL:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


            self.state = 37
            self.match(DLVParserInput.NEW_LINE_SYMBOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT_BEGIN(self):
            return self.getToken(DLVParserInput.COMMENT_BEGIN, 0)

        def schema(self):
            return self.getTypedRuleContext(DLVParserInput.SchemaContext,0)


        def NEW_LINE_SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserInput.NEW_LINE_SYMBOL)
            else:
                return self.getToken(DLVParserInput.NEW_LINE_SYMBOL, i)

        def getRuleIndex(self):
            return DLVParserInput.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = DLVParserInput.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(DLVParserInput.COMMENT_BEGIN)
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 40
                self.schema()


            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DLVParserInput.WHITESPACE) | (1 << DLVParserInput.SCHEMA_KEY_LABEL) | (1 << DLVParserInput.ANCESTOR_KEY_LABEL) | (1 << DLVParserInput.KEY_LABEL) | (1 << DLVParserInput.KEY_AUTOINCREMENT) | (1 << DLVParserInput.COMMA) | (1 << DLVParserInput.OPEN_ROUND_BRACKET) | (1 << DLVParserInput.CLOSE_ROUND_BRACKET) | (1 << DLVParserInput.OPEN_SQUARE_BRACKET) | (1 << DLVParserInput.CLOSE_SQUARE_BRACKET) | (1 << DLVParserInput.NAME) | (1 << DLVParserInput.STRING) | (1 << DLVParserInput.COMMENT_BEGIN) | (1 << DLVParserInput.ANY))) != 0):
                self.state = 43
                _la = self._input.LA(1)
                if _la <= 0 or _la==DLVParserInput.NEW_LINE_SYMBOL:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCHEMA_KEY_LABEL(self):
            return self.getToken(DLVParserInput.SCHEMA_KEY_LABEL, 0)

        def OPEN_ROUND_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserInput.OPEN_ROUND_BRACKET)
            else:
                return self.getToken(DLVParserInput.OPEN_ROUND_BRACKET, i)

        def name(self):
            return self.getTypedRuleContext(DLVParserInput.NameContext,0)


        def key(self):
            return self.getTypedRuleContext(DLVParserInput.KeyContext,0)


        def CLOSE_ROUND_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserInput.CLOSE_ROUND_BRACKET)
            else:
                return self.getToken(DLVParserInput.CLOSE_ROUND_BRACKET, i)

        def ancestor_key(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserInput.Ancestor_keyContext)
            else:
                return self.getTypedRuleContext(DLVParserInput.Ancestor_keyContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserInput.COMMA)
            else:
                return self.getToken(DLVParserInput.COMMA, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserInput.STRING)
            else:
                return self.getToken(DLVParserInput.STRING, i)

        def getRuleIndex(self):
            return DLVParserInput.RULE_schema

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchema" ):
                listener.enterSchema(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchema" ):
                listener.exitSchema(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchema" ):
                return visitor.visitSchema(self)
            else:
                return visitor.visitChildren(self)




    def schema(self):

        localctx = DLVParserInput.SchemaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_schema)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(DLVParserInput.SCHEMA_KEY_LABEL)
            self.state = 50
            self.match(DLVParserInput.OPEN_ROUND_BRACKET)
            self.state = 51
            self.name()
            self.state = 52
            self.match(DLVParserInput.OPEN_ROUND_BRACKET)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DLVParserInput.ANCESTOR_KEY_LABEL:
                self.state = 53
                self.ancestor_key()
                self.state = 54
                self.match(DLVParserInput.COMMA)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.key()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DLVParserInput.COMMA:
                self.state = 62
                self.match(DLVParserInput.COMMA)
                self.state = 63
                self.match(DLVParserInput.STRING)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(DLVParserInput.CLOSE_ROUND_BRACKET)
            self.state = 70
            self.match(DLVParserInput.CLOSE_ROUND_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ancestor_keyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANCESTOR_KEY_LABEL(self):
            return self.getToken(DLVParserInput.ANCESTOR_KEY_LABEL, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(DLVParserInput.OPEN_ROUND_BRACKET, 0)

        def name(self):
            return self.getTypedRuleContext(DLVParserInput.NameContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(DLVParserInput.CLOSE_ROUND_BRACKET, 0)

        def getRuleIndex(self):
            return DLVParserInput.RULE_ancestor_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAncestor_key" ):
                listener.enterAncestor_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAncestor_key" ):
                listener.exitAncestor_key(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAncestor_key" ):
                return visitor.visitAncestor_key(self)
            else:
                return visitor.visitChildren(self)




    def ancestor_key(self):

        localctx = DLVParserInput.Ancestor_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ancestor_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(DLVParserInput.ANCESTOR_KEY_LABEL)
            self.state = 73
            self.match(DLVParserInput.OPEN_ROUND_BRACKET)
            self.state = 74
            self.name()
            self.state = 75
            self.match(DLVParserInput.CLOSE_ROUND_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DLVParserInput.NAME, 0)

        def SCHEMA_KEY_LABEL(self):
            return self.getToken(DLVParserInput.SCHEMA_KEY_LABEL, 0)

        def ANCESTOR_KEY_LABEL(self):
            return self.getToken(DLVParserInput.ANCESTOR_KEY_LABEL, 0)

        def KEY_LABEL(self):
            return self.getToken(DLVParserInput.KEY_LABEL, 0)

        def KEY_AUTOINCREMENT(self):
            return self.getToken(DLVParserInput.KEY_AUTOINCREMENT, 0)

        def getRuleIndex(self):
            return DLVParserInput.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = DLVParserInput.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DLVParserInput.SCHEMA_KEY_LABEL) | (1 << DLVParserInput.ANCESTOR_KEY_LABEL) | (1 << DLVParserInput.KEY_LABEL) | (1 << DLVParserInput.KEY_AUTOINCREMENT) | (1 << DLVParserInput.NAME))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_LABEL(self):
            return self.getToken(DLVParserInput.KEY_LABEL, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(DLVParserInput.OPEN_ROUND_BRACKET, 0)

        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(DLVParserInput.CLOSE_ROUND_BRACKET, 0)

        def key_autoincrement(self):
            return self.getTypedRuleContext(DLVParserInput.Key_autoincrementContext,0)


        def key_properties(self):
            return self.getTypedRuleContext(DLVParserInput.Key_propertiesContext,0)


        def getRuleIndex(self):
            return DLVParserInput.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = DLVParserInput.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(DLVParserInput.KEY_LABEL)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserInput.OPEN_ROUND_BRACKET:
                self.state = 80
                self.match(DLVParserInput.OPEN_ROUND_BRACKET)
                self.state = 83
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DLVParserInput.KEY_AUTOINCREMENT]:
                    self.state = 81
                    self.key_autoincrement()
                    pass
                elif token in [DLVParserInput.OPEN_SQUARE_BRACKET]:
                    self.state = 82
                    self.key_properties()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 85
                self.match(DLVParserInput.CLOSE_ROUND_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_propertiesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(DLVParserInput.OPEN_SQUARE_BRACKET, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserInput.STRING)
            else:
                return self.getToken(DLVParserInput.STRING, i)

        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(DLVParserInput.CLOSE_SQUARE_BRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserInput.COMMA)
            else:
                return self.getToken(DLVParserInput.COMMA, i)

        def key_concat(self):
            return self.getTypedRuleContext(DLVParserInput.Key_concatContext,0)


        def getRuleIndex(self):
            return DLVParserInput.RULE_key_properties

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey_properties" ):
                listener.enterKey_properties(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey_properties" ):
                listener.exitKey_properties(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_properties" ):
                return visitor.visitKey_properties(self)
            else:
                return visitor.visitChildren(self)




    def key_properties(self):

        localctx = DLVParserInput.Key_propertiesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_key_properties)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(DLVParserInput.OPEN_SQUARE_BRACKET)
            self.state = 90
            self.match(DLVParserInput.STRING)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DLVParserInput.COMMA:
                self.state = 91
                self.match(DLVParserInput.COMMA)
                self.state = 92
                self.match(DLVParserInput.STRING)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(DLVParserInput.CLOSE_SQUARE_BRACKET)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserInput.COMMA:
                self.state = 99
                self.match(DLVParserInput.COMMA)
                self.state = 100
                self.key_concat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_concatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DLVParserInput.STRING, 0)

        def getRuleIndex(self):
            return DLVParserInput.RULE_key_concat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey_concat" ):
                listener.enterKey_concat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey_concat" ):
                listener.exitKey_concat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_concat" ):
                return visitor.visitKey_concat(self)
            else:
                return visitor.visitChildren(self)




    def key_concat(self):

        localctx = DLVParserInput.Key_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_key_concat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(DLVParserInput.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_autoincrementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_AUTOINCREMENT(self):
            return self.getToken(DLVParserInput.KEY_AUTOINCREMENT, 0)

        def getRuleIndex(self):
            return DLVParserInput.RULE_key_autoincrement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey_autoincrement" ):
                listener.enterKey_autoincrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey_autoincrement" ):
                listener.exitKey_autoincrement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_autoincrement" ):
                return visitor.visitKey_autoincrement(self)
            else:
                return visitor.visitChildren(self)




    def key_autoincrement(self):

        localctx = DLVParserInput.Key_autoincrementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_key_autoincrement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(DLVParserInput.KEY_AUTOINCREMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





