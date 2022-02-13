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
        buf.write("\u0087\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\7\2\30\n\2\f\2")
        buf.write("\16\2\33\13\2\3\3\3\3\5\3\37\n\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\7\3\'\n\3\f\3\16\3*\13\3\3\3\3\3\3\3\3\3\3\3\5\3\61")
        buf.write("\n\3\3\3\3\3\3\3\7\3\66\n\3\f\3\16\39\13\3\5\3;\n\3\3")
        buf.write("\4\3\4\3\4\3\4\7\4A\n\4\f\4\16\4D\13\4\5\4F\n\4\3\4\3")
        buf.write("\4\3\5\5\5K\n\5\3\5\3\5\3\6\5\6P\n\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\7\7Y\n\7\f\7\16\7\\\13\7\3\7\3\7\5\7`\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bi\n\b\f\b\16\bl\13\b\5\b")
        buf.write("n\n\b\3\b\5\bq\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7\nz\n")
        buf.write("\n\f\n\16\n}\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2\u0090\2\31\3")
        buf.write("\2\2\2\4:\3\2\2\2\6<\3\2\2\2\bJ\3\2\2\2\nO\3\2\2\2\fS")
        buf.write("\3\2\2\2\16p\3\2\2\2\20r\3\2\2\2\22u\3\2\2\2\24\u0080")
        buf.write("\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\33\3\2\2\2\31")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33\31\3\2\2\2\34")
        buf.write(";\5\6\4\2\35\37\7\22\2\2\36\35\3\2\2\2\36\37\3\2\2\2\37")
        buf.write(" \3\2\2\2 !\5\6\4\2!\"\5\22\n\2\";\3\2\2\2#(\5\b\5\2$")
        buf.write("%\7\5\2\2%\'\5\b\5\2&$\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()")
        buf.write("\3\2\2\2)+\3\2\2\2*(\3\2\2\2+,\7\25\2\2,-\7\26\2\2-\60")
        buf.write("\7\27\2\2.\61\7\31\2\2/\61\5\20\t\2\60.\3\2\2\2\60/\3")
        buf.write("\2\2\2\61;\3\2\2\2\62\67\5\16\b\2\63\64\7\5\2\2\64\66")
        buf.write("\5\16\b\2\65\63\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678")
        buf.write("\3\2\2\28;\3\2\2\29\67\3\2\2\2:\34\3\2\2\2:\36\3\2\2\2")
        buf.write(":#\3\2\2\2:\62\3\2\2\2;\5\3\2\2\2<E\7\t\2\2=B\5\n\6\2")
        buf.write(">?\7\5\2\2?A\5\n\6\2@>\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3")
        buf.write("\2\2\2CF\3\2\2\2DB\3\2\2\2E=\3\2\2\2EF\3\2\2\2FG\3\2\2")
        buf.write("\2GH\7\n\2\2H\7\3\2\2\2IK\7\16\2\2JI\3\2\2\2JK\3\2\2\2")
        buf.write("KL\3\2\2\2LM\5\n\6\2M\t\3\2\2\2NP\7\r\2\2ON\3\2\2\2OP")
        buf.write("\3\2\2\2PQ\3\2\2\2QR\5\f\7\2R\13\3\2\2\2S_\7\20\2\2TU")
        buf.write("\7\7\2\2UZ\5\16\b\2VW\7\5\2\2WY\5\16\b\2XV\3\2\2\2Y\\")
        buf.write("\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\Z\3\2\2\2]^\7")
        buf.write("\b\2\2^`\3\2\2\2_T\3\2\2\2_`\3\2\2\2`\r\3\2\2\2aq\7\17")
        buf.write("\2\2bq\7\21\2\2cq\5\f\7\2dm\7\13\2\2ej\5\16\b\2fg\7\5")
        buf.write("\2\2gi\5\16\b\2hf\3\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2")
        buf.write("\2kn\3\2\2\2lj\3\2\2\2me\3\2\2\2mn\3\2\2\2no\3\2\2\2o")
        buf.write("q\7\f\2\2pa\3\2\2\2pb\3\2\2\2pc\3\2\2\2pd\3\2\2\2q\17")
        buf.write("\3\2\2\2rs\7\32\2\2st\5\6\4\2t\21\3\2\2\2uv\7\23\2\2v")
        buf.write("{\5\24\13\2wx\7\5\2\2xz\5\24\13\2yw\3\2\2\2z}\3\2\2\2")
        buf.write("{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\24\2\2")
        buf.write("\177\23\3\2\2\2\u0080\u0081\7\13\2\2\u0081\u0082\7\21")
        buf.write("\2\2\u0082\u0083\7\6\2\2\u0083\u0084\7\21\2\2\u0084\u0085")
        buf.write("\7\f\2\2\u0085\25\3\2\2\2\22\31\36(\60\67:BEJOZ_jmp{")
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DLVParserOutput.OPEN_BRACE) | (1 << DLVParserOutput.OPEN_SQUARE_BRACKET) | (1 << DLVParserOutput.TRUE_NEGATION) | (1 << DLVParserOutput.NEGATION_AS_FAILURE) | (1 << DLVParserOutput.STRING) | (1 << DLVParserOutput.NAME) | (1 << DLVParserOutput.INTEGER) | (1 << DLVParserOutput.BEGIN_BEST_MODEL))) != 0):
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


    class QueryNonGroundContext(Answer_setContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DLVParserOutput.Answer_setContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryNonGround" ):
                listener.enterQueryNonGround(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryNonGround" ):
                listener.exitQueryNonGround(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryNonGround" ):
                return visitor.visitQueryNonGround(self)
            else:
                return visitor.visitChildren(self)


    class QueryGroundContext(Answer_setContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a DLVParserOutput.Answer_setContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def query_literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLVParserOutput.Query_literalContext)
            else:
                return self.getTypedRuleContext(DLVParserOutput.Query_literalContext,i)

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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DLVParserOutput.COMMA)
            else:
                return self.getToken(DLVParserOutput.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryGround" ):
                listener.enterQueryGround(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryGround" ):
                listener.exitQueryGround(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryGround" ):
                return visitor.visitQueryGround(self)
            else:
                return visitor.visitChildren(self)



    def answer_set(self):

        localctx = DLVParserOutput.Answer_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_answer_set)
        self._la = 0 # Token type
        try:
            self.state = 56
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
                localctx = DLVParserOutput.QueryGroundContext(self, localctx)
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

            elif la_ == 4:
                localctx = DLVParserOutput.QueryNonGroundContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.term()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DLVParserOutput.COMMA:
                    self.state = 49
                    self.match(DLVParserOutput.COMMA)
                    self.state = 50
                    self.term()
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
            self.state = 58
            self.match(DLVParserOutput.OPEN_BRACE)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserOutput.TRUE_NEGATION or _la==DLVParserOutput.NAME:
                self.state = 59
                self.literal()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DLVParserOutput.COMMA:
                    self.state = 60
                    self.match(DLVParserOutput.COMMA)
                    self.state = 61
                    self.literal()
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 69
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
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserOutput.NEGATION_AS_FAILURE:
                self.state = 71
                self.match(DLVParserOutput.NEGATION_AS_FAILURE)


            self.state = 74
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
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserOutput.TRUE_NEGATION:
                self.state = 76
                self.match(DLVParserOutput.TRUE_NEGATION)


            self.state = 79
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
            self.state = 81
            self.match(DLVParserOutput.NAME)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLVParserOutput.OPEN_ROUND_BRACKET:
                self.state = 82
                self.match(DLVParserOutput.OPEN_ROUND_BRACKET)
                self.state = 83
                self.term()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==DLVParserOutput.COMMA:
                    self.state = 84
                    self.match(DLVParserOutput.COMMA)
                    self.state = 85
                    self.term()
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 91
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
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DLVParserOutput.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(DLVParserOutput.STRING)
                pass
            elif token in [DLVParserOutput.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(DLVParserOutput.INTEGER)
                pass
            elif token in [DLVParserOutput.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.atom()
                pass
            elif token in [DLVParserOutput.OPEN_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.match(DLVParserOutput.OPEN_SQUARE_BRACKET)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DLVParserOutput.OPEN_SQUARE_BRACKET) | (1 << DLVParserOutput.STRING) | (1 << DLVParserOutput.NAME) | (1 << DLVParserOutput.INTEGER))) != 0):
                    self.state = 99
                    self.term()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==DLVParserOutput.COMMA:
                        self.state = 100
                        self.match(DLVParserOutput.COMMA)
                        self.state = 101
                        self.term()
                        self.state = 106
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 109
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
            self.state = 112
            self.match(DLVParserOutput.BEGIN_WITNESS)
            self.state = 113
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
            self.state = 115
            self.match(DLVParserOutput.BEGIN_COST)
            self.state = 116
            self.cost_amount()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DLVParserOutput.COMMA:
                self.state = 117
                self.match(DLVParserOutput.COMMA)
                self.state = 118
                self.cost_amount()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
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
            self.state = 126
            self.match(DLVParserOutput.OPEN_SQUARE_BRACKET)
            self.state = 127
            self.match(DLVParserOutput.INTEGER)
            self.state = 128
            self.match(DLVParserOutput.COLON)
            self.state = 129
            self.match(DLVParserOutput.INTEGER)
            self.state = 130
            self.match(DLVParserOutput.CLOSE_SQUARE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





