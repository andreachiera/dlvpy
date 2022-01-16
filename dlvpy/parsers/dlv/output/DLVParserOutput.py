# Generated from ..\dlv\grammar_output\DLVParserOutput.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\u0081\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2")
        buf.write("\16\2\33\13\2\3\3\3\3\5\3\37\n\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\7\3\'\n\3\f\3\16\3*\13\3\3\3\3\3\3\3\3\3\3\3\5\3\61")
        buf.write("\n\3\5\3\63\n\3\5\3\65\n\3\3\4\3\4\3\4\3\4\7\4;\n\4\f")
        buf.write("\4\16\4>\13\4\5\4@\n\4\3\4\3\4\3\5\5\5E\n\5\3\5\3\5\3")
        buf.write("\6\5\6J\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7S\n\7\f\7\16")
        buf.write("\7V\13\7\3\7\3\7\5\7Z\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\7\bc\n\b\f\b\16\bf\13\b\5\bh\n\b\3\b\5\bk\n\b\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\7\nt\n\n\f\n\16\nw\13\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16")
        buf.write("\20\22\24\2\2\2\u0089\2\31\3\2\2\2\4\64\3\2\2\2\6\66\3")
        buf.write("\2\2\2\bD\3\2\2\2\nI\3\2\2\2\fM\3\2\2\2\16j\3\2\2\2\20")
        buf.write("l\3\2\2\2\22o\3\2\2\2\24z\3\2\2\2\26\30\5\4\3\2\27\26")
        buf.write("\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32")
        buf.write("\3\3\2\2\2\33\31\3\2\2\2\34\65\5\6\4\2\35\37\7\22\2\2")
        buf.write("\36\35\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\5\6\4\2!\"")
        buf.write("\5\22\n\2\"\65\3\2\2\2#(\5\b\5\2$%\7\5\2\2%\'\5\b\5\2")
        buf.write("&$\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\62\3\2\2\2")
        buf.write("*(\3\2\2\2+,\7\25\2\2,-\7\26\2\2-\60\7\27\2\2.\61\7\31")
        buf.write("\2\2/\61\5\20\t\2\60.\3\2\2\2\60/\3\2\2\2\61\63\3\2\2")
        buf.write("\2\62+\3\2\2\2\62\63\3\2\2\2\63\65\3\2\2\2\64\34\3\2\2")
        buf.write("\2\64\36\3\2\2\2\64#\3\2\2\2\65\5\3\2\2\2\66?\7\t\2\2")
        buf.write("\67<\5\n\6\289\7\5\2\29;\5\n\6\2:8\3\2\2\2;>\3\2\2\2<")
        buf.write(":\3\2\2\2<=\3\2\2\2=@\3\2\2\2><\3\2\2\2?\67\3\2\2\2?@")
        buf.write("\3\2\2\2@A\3\2\2\2AB\7\n\2\2B\7\3\2\2\2CE\7\16\2\2DC\3")
        buf.write("\2\2\2DE\3\2\2\2EF\3\2\2\2FG\5\n\6\2G\t\3\2\2\2HJ\7\r")
        buf.write("\2\2IH\3\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\5\f\7\2L\13\3\2\2")
        buf.write("\2MY\7\20\2\2NO\7\7\2\2OT\5\16\b\2PQ\7\5\2\2QS\5\16\b")
        buf.write("\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2V")
        buf.write("T\3\2\2\2WX\7\b\2\2XZ\3\2\2\2YN\3\2\2\2YZ\3\2\2\2Z\r\3")
        buf.write("\2\2\2[k\7\17\2\2\\k\7\21\2\2]k\5\f\7\2^g\7\13\2\2_d\5")
        buf.write("\16\b\2`a\7\5\2\2ac\5\16\b\2b`\3\2\2\2cf\3\2\2\2db\3\2")
        buf.write("\2\2de\3\2\2\2eh\3\2\2\2fd\3\2\2\2g_\3\2\2\2gh\3\2\2\2")
        buf.write("hi\3\2\2\2ik\7\f\2\2j[\3\2\2\2j\\\3\2\2\2j]\3\2\2\2j^")
        buf.write("\3\2\2\2k\17\3\2\2\2lm\7\32\2\2mn\5\6\4\2n\21\3\2\2\2")
        buf.write("op\7\23\2\2pu\5\24\13\2qr\7\5\2\2rt\5\24\13\2sq\3\2\2")
        buf.write("\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2x")
        buf.write("y\7\24\2\2y\23\3\2\2\2z{\7\13\2\2{|\7\21\2\2|}\7\6\2\2")
        buf.write("}~\7\21\2\2~\177\7\f\2\2\177\25\3\2\2\2\22\31\36(\60\62")
        buf.write("\64<?DITYdgju")
        return buf.getvalue()


class DLVParserOutput ( Parser ):

    grammarFileName = "DLVParserOutput.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "','", "':'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "<INVALID>", 
                     "'not'", "<INVALID>", "<INVALID>", "<INVALID>", "'Best model:'", 
                     "'Cost ([Weight:Level]): <'", "'>'", "' is '", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'", "', evidenced by'" ]

    symbolicNames = [ "<INVALID>", "HEADER", "WHITESPACE", "COMMA", "COLON", 
                      "OPEN_ROUND_BRACKET", "CLOSE_ROUND_BRACKET", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", 
                      "TRUE_NEGATION", "NEGATION_AS_FAILURE", "STRING", 
                      "NAME", "INTEGER", "BEGIN_BEST_MODEL", "BEGIN_COST", 
                      "END_COST", "BEGIN_GROUND_QUERY", "REASONING", "BOOLEAN", 
                      "GROUND_QUERY_WHITESPACE", "DOT", "BEGIN_WITNESS" ]

    RULE_output = 0
    RULE_answer_set = 1
    RULE_model = 2
    RULE_query_literal = 3
    RULE_literal = 4
    RULE_atom = 5
    RULE_term = 6
    RULE_witness = 7
    RULE_cost = 8
    RULE_cost_amount = 9

    ruleNames =  [ "output", "answer_set", "model", "query_literal", "literal", 
                   "atom", "term", "witness", "cost", "cost_amount" ]

    EOF = Token.EOF
    HEADER=1
    WHITESPACE=2
    COMMA=3
    COLON=4
    OPEN_ROUND_BRACKET=5
    CLOSE_ROUND_BRACKET=6
    OPEN_BRACE=7
    CLOSE_BRACE=8
    OPEN_SQUARE_BRACKET=9
    CLOSE_SQUARE_BRACKET=10
    TRUE_NEGATION=11
    NEGATION_AS_FAILURE=12
    STRING=13
    NAME=14
    INTEGER=15
    BEGIN_BEST_MODEL=16
    BEGIN_COST=17
    END_COST=18
    BEGIN_GROUND_QUERY=19
    REASONING=20
    BOOLEAN=21
    GROUND_QUERY_WHITESPACE=22
    DOT=23
    BEGIN_WITNESS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def answer_set(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserOutput.Answer_setContext)
            else:
                return self.getTypedRuleContext(DLVParserOutput.Answer_setContext,i)


        def getRuleIndex(self):
            return DLVParserOutput.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = DLVParserOutput.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DLVParserOutput.OPEN_BRACE) | (1 << DLVParserOutput.TRUE_NEGATION) | (1 << DLVParserOutput.NEGATION_AS_FAILURE) | (1 << DLVParserOutput.NAME) | (1 << DLVParserOutput.BEGIN_BEST_MODEL))) != 0):
                self.state = 20
                self.answer_set()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Answer_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DLVParserOutput.RULE_answer_set

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleModelContext(Answer_setContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DLVParserOutput.Answer_setContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def model(self):
            return self.getTypedRuleContext(DLVParserOutput.ModelContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleModel" ):
                listener.enterSimpleModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleModel" ):
                listener.exitSimpleModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleModel" ):
                return visitor.visitSimpleModel(self)
            else:
                return visitor.visitChildren(self)


    class ModelWithCostContext(Answer_setContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DLVParserOutput.Answer_setContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def model(self):
            return self.getTypedRuleContext(DLVParserOutput.ModelContext,0)

        def cost(self):
            return self.getTypedRuleContext(DLVParserOutput.CostContext,0)

        def BEGIN_BEST_MODEL(self):
            return self.getToken(DLVParserOutput.BEGIN_BEST_MODEL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelWithCost" ):
                listener.enterModelWithCost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelWithCost" ):
                listener.exitModelWithCost(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelWithCost" ):
                return visitor.visitModelWithCost(self)
            else:
                return visitor.visitChildren(self)


    class QueryContext(Answer_setContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DLVParserOutput.Answer_setContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def query_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserOutput.Query_literalContext)
            else:
                return self.getTypedRuleContext(DLVParserOutput.Query_literalContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserOutput.COMMA)
            else:
                return self.getToken(DLVParserOutput.COMMA, i)
        def BEGIN_GROUND_QUERY(self):
            return self.getToken(DLVParserOutput.BEGIN_GROUND_QUERY, 0)
        def REASONING(self):
            return self.getToken(DLVParserOutput.REASONING, 0)
        def BOOLEAN(self):
            return self.getToken(DLVParserOutput.BOOLEAN, 0)
        def DOT(self):
            return self.getToken(DLVParserOutput.DOT, 0)
        def witness(self):
            return self.getTypedRuleContext(DLVParserOutput.WitnessContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)



    def answer_set(self):

        localctx = DLVParserOutput.Answer_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_answer_set)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = DLVParserOutput.SimpleModelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.model()
                pass

            elif la_ == 2:
                localctx = DLVParserOutput.ModelWithCostContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DLVParserOutput.BEGIN_BEST_MODEL:
                    self.state = 27
                    self.match(DLVParserOutput.BEGIN_BEST_MODEL)


                self.state = 30
                self.model()
                self.state = 31
                self.cost()
                pass

            elif la_ == 3:
                localctx = DLVParserOutput.QueryContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.query_literal()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DLVParserOutput.COMMA:
                    self.state = 34
                    self.match(DLVParserOutput.COMMA)
                    self.state = 35
                    self.query_literal()
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==DLVParserOutput.BEGIN_GROUND_QUERY:
                    self.state = 41
                    self.match(DLVParserOutput.BEGIN_GROUND_QUERY)
                    self.state = 42
                    self.match(DLVParserOutput.REASONING)
                    self.state = 43
                    self.match(DLVParserOutput.BOOLEAN)
                    self.state = 46
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [DLVParserOutput.DOT]:
                        self.state = 44
                        self.match(DLVParserOutput.DOT)
                        pass
                    elif token in [DLVParserOutput.BEGIN_WITNESS]:
                        self.state = 45
                        self.witness()
                        pass
                    else:
                        raise NoViableAltException(self)



                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(DLVParserOutput.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(DLVParserOutput.CLOSE_BRACE, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserOutput.LiteralContext)
            else:
                return self.getTypedRuleContext(DLVParserOutput.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserOutput.COMMA)
            else:
                return self.getToken(DLVParserOutput.COMMA, i)

        def getRuleIndex(self):
            return DLVParserOutput.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel" ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = DLVParserOutput.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(DLVParserOutput.OPEN_BRACE)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserOutput.TRUE_NEGATION or _la==DLVParserOutput.NAME:
                self.state = 53
                self.literal()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DLVParserOutput.COMMA:
                    self.state = 54
                    self.match(DLVParserOutput.COMMA)
                    self.state = 55
                    self.literal()
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 63
            self.match(DLVParserOutput.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(DLVParserOutput.LiteralContext,0)


        def NEGATION_AS_FAILURE(self):
            return self.getToken(DLVParserOutput.NEGATION_AS_FAILURE, 0)

        def getRuleIndex(self):
            return DLVParserOutput.RULE_query_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_literal" ):
                listener.enterQuery_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_literal" ):
                listener.exitQuery_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery_literal" ):
                return visitor.visitQuery_literal(self)
            else:
                return visitor.visitChildren(self)




    def query_literal(self):

        localctx = DLVParserOutput.Query_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_query_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserOutput.NEGATION_AS_FAILURE:
                self.state = 65
                self.match(DLVParserOutput.NEGATION_AS_FAILURE)


            self.state = 68
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(DLVParserOutput.AtomContext,0)


        def TRUE_NEGATION(self):
            return self.getToken(DLVParserOutput.TRUE_NEGATION, 0)

        def getRuleIndex(self):
            return DLVParserOutput.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = DLVParserOutput.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserOutput.TRUE_NEGATION:
                self.state = 70
                self.match(DLVParserOutput.TRUE_NEGATION)


            self.state = 73
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(DLVParserOutput.NAME, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(DLVParserOutput.OPEN_ROUND_BRACKET, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserOutput.TermContext)
            else:
                return self.getTypedRuleContext(DLVParserOutput.TermContext,i)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(DLVParserOutput.CLOSE_ROUND_BRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserOutput.COMMA)
            else:
                return self.getToken(DLVParserOutput.COMMA, i)

        def getRuleIndex(self):
            return DLVParserOutput.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = DLVParserOutput.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(DLVParserOutput.NAME)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserOutput.OPEN_ROUND_BRACKET:
                self.state = 76
                self.match(DLVParserOutput.OPEN_ROUND_BRACKET)
                self.state = 77
                self.term()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DLVParserOutput.COMMA:
                    self.state = 78
                    self.match(DLVParserOutput.COMMA)
                    self.state = 79
                    self.term()
                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 85
                self.match(DLVParserOutput.CLOSE_ROUND_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DLVParserOutput.STRING, 0)

        def INTEGER(self):
            return self.getToken(DLVParserOutput.INTEGER, 0)

        def atom(self):
            return self.getTypedRuleContext(DLVParserOutput.AtomContext,0)


        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(DLVParserOutput.OPEN_SQUARE_BRACKET, 0)

        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(DLVParserOutput.CLOSE_SQUARE_BRACKET, 0)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserOutput.TermContext)
            else:
                return self.getTypedRuleContext(DLVParserOutput.TermContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserOutput.COMMA)
            else:
                return self.getToken(DLVParserOutput.COMMA, i)

        def getRuleIndex(self):
            return DLVParserOutput.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = DLVParserOutput.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DLVParserOutput.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(DLVParserOutput.STRING)
                pass
            elif token in [DLVParserOutput.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(DLVParserOutput.INTEGER)
                pass
            elif token in [DLVParserOutput.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.atom()
                pass
            elif token in [DLVParserOutput.OPEN_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.match(DLVParserOutput.OPEN_SQUARE_BRACKET)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DLVParserOutput.OPEN_SQUARE_BRACKET) | (1 << DLVParserOutput.STRING) | (1 << DLVParserOutput.NAME) | (1 << DLVParserOutput.INTEGER))) != 0):
                    self.state = 93
                    self.term()
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==DLVParserOutput.COMMA:
                        self.state = 94
                        self.match(DLVParserOutput.COMMA)
                        self.state = 95
                        self.term()
                        self.state = 100
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 103
                self.match(DLVParserOutput.CLOSE_SQUARE_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WitnessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_WITNESS(self):
            return self.getToken(DLVParserOutput.BEGIN_WITNESS, 0)

        def model(self):
            return self.getTypedRuleContext(DLVParserOutput.ModelContext,0)


        def getRuleIndex(self):
            return DLVParserOutput.RULE_witness

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWitness" ):
                listener.enterWitness(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWitness" ):
                listener.exitWitness(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWitness" ):
                return visitor.visitWitness(self)
            else:
                return visitor.visitChildren(self)




    def witness(self):

        localctx = DLVParserOutput.WitnessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_witness)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(DLVParserOutput.BEGIN_WITNESS)
            self.state = 107
            self.model()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CostContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_COST(self):
            return self.getToken(DLVParserOutput.BEGIN_COST, 0)

        def cost_amount(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserOutput.Cost_amountContext)
            else:
                return self.getTypedRuleContext(DLVParserOutput.Cost_amountContext,i)


        def END_COST(self):
            return self.getToken(DLVParserOutput.END_COST, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserOutput.COMMA)
            else:
                return self.getToken(DLVParserOutput.COMMA, i)

        def getRuleIndex(self):
            return DLVParserOutput.RULE_cost

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCost" ):
                listener.enterCost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCost" ):
                listener.exitCost(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCost" ):
                return visitor.visitCost(self)
            else:
                return visitor.visitChildren(self)




    def cost(self):

        localctx = DLVParserOutput.CostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cost)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(DLVParserOutput.BEGIN_COST)
            self.state = 110
            self.cost_amount()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DLVParserOutput.COMMA:
                self.state = 111
                self.match(DLVParserOutput.COMMA)
                self.state = 112
                self.cost_amount()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(DLVParserOutput.END_COST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cost_amountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(DLVParserOutput.OPEN_SQUARE_BRACKET, 0)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserOutput.INTEGER)
            else:
                return self.getToken(DLVParserOutput.INTEGER, i)

        def COLON(self):
            return self.getToken(DLVParserOutput.COLON, 0)

        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(DLVParserOutput.CLOSE_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return DLVParserOutput.RULE_cost_amount

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCost_amount" ):
                listener.enterCost_amount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCost_amount" ):
                listener.exitCost_amount(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCost_amount" ):
                return visitor.visitCost_amount(self)
            else:
                return visitor.visitChildren(self)




    def cost_amount(self):

        localctx = DLVParserOutput.Cost_amountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cost_amount)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(DLVParserOutput.OPEN_SQUARE_BRACKET)
            self.state = 121
            self.match(DLVParserOutput.INTEGER)
            self.state = 122
            self.match(DLVParserOutput.COLON)
            self.state = 123
            self.match(DLVParserOutput.INTEGER)
            self.state = 124
            self.match(DLVParserOutput.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





