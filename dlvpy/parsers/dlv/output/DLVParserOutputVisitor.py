# Generated from ..\dlv\grammar_output\DLVParserOutput.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DLVParserOutput import DLVParserOutput
else:
    from DLVParserOutput import DLVParserOutput

# This class defines a complete generic visitor for a parse tree produced by DLVParserOutput.

class DLVParserOutputVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DLVParserOutput#output.
    def visitOutput(self, ctx:DLVParserOutput.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#SimpleModel.
    def visitSimpleModel(self, ctx:DLVParserOutput.SimpleModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#ModelWithCost.
    def visitModelWithCost(self, ctx:DLVParserOutput.ModelWithCostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#QueryGround.
    def visitQueryGround(self, ctx:DLVParserOutput.QueryGroundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#QueryNonGround.
    def visitQueryNonGround(self, ctx:DLVParserOutput.QueryNonGroundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#model.
    def visitModel(self, ctx:DLVParserOutput.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#query_literal.
    def visitQuery_literal(self, ctx:DLVParserOutput.Query_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#literal.
    def visitLiteral(self, ctx:DLVParserOutput.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#atom.
    def visitAtom(self, ctx:DLVParserOutput.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#term.
    def visitTerm(self, ctx:DLVParserOutput.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#witness.
    def visitWitness(self, ctx:DLVParserOutput.WitnessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#cost.
    def visitCost(self, ctx:DLVParserOutput.CostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserOutput#cost_amount.
    def visitCost_amount(self, ctx:DLVParserOutput.Cost_amountContext):
        return self.visitChildren(ctx)



del DLVParserOutput