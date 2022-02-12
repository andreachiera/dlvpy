from antlr4 import InputStream, CommonTokenStream

from dlvpy.utilities.mapper import DLVMapper
from .DLVLexerOutput import DLVLexerOutput
from .DLVParserOutput import DLVParserOutput
from .DLVParserOutputVisitor import DLVParserOutputVisitor

# This class defines a complete generic visitor for a parse tree produced by DLVParserOutput.

class DLVParserOutputVisitorImpl(DLVParserOutputVisitor):

    # Visit a parse tree produced by DLVParserOutput#output.
    def visitOutput(self, ctx: DLVParserOutput.OutputContext):
        answer_sets = []

        if ctx is not None and ctx.answer_set() is not None:
            for answer_set_ctx in ctx.answer_set():
                if not hasattr(answer_set_ctx, "accept"):
                    continue
                answer_set = answer_set_ctx.accept(self)
                if answer_set is None:
                    continue
                answer_sets.append(answer_set)

        return answer_sets

    # Visit a parse tree produced by DLVParserOutput#SimpleModel.
    def visitSimpleModel(self, ctx: DLVParserOutput.SimpleModelContext):
        if ctx is None or ctx.model() is None:
            return None
        model = self.visitModel(ctx.model())
        if model is None:
            return None
        return {
            "model": model
        }

    # Visit a parse tree produced by DLVParserOutput#Query.
    def visitQuery(self, ctx: DLVParserOutput.QueryContext):
        if ctx is None or ctx.query_literal() is None:
            return None

        literals = [self.visitQuery_literal(query_literal_ctx) for query_literal_ctx in ctx.query_literal()]

        query = {
            "query": {
                "literals": literals
            }
        }

        if ctx.BEGIN_GROUND_QUERY() is None:
            return query
        reasoning = ctx.REASONING().getText()
        result = ctx.BOOLEAN().getText()
        query["reasoning"] =  {
            "type": reasoning,
            "value": None if result is None else True if result == 'true' else False
        }

        if ctx.witness() is not None:
            witness = self.visitWitness(ctx.witness())
            if witness is not None:
                query["query"]["witness"] = witness

        return query

    # Visit a parse tree produced by DLVParserOutput#ModelWithCost.
    def visitModelWithCost(self, ctx: DLVParserOutput.ModelWithCostContext):
        if ctx is None:
            return None

        model = self.visitModel(ctx.model())
        cost = self.visitCost(ctx.cost())
        if model is None or cost is None:
            return None

        return {
            "model_with_cost": {
                "best_model": True if ctx.BEGIN_BEST_MODEL() is not None else False,
                "model": model,
                "cost": cost
            }
        }

    # Visit a parse tree produced by DLVParserOutput#model.
    def visitModel(self, ctx: DLVParserOutput.ModelContext):
        if ctx is None or ctx.literal() is None:
            return None

        literals = []
        for literal_ctx in ctx.literal():
            if literal_ctx is None:
                continue
            literal = self.visitLiteral(literal_ctx)
            if literal is None:
                continue
            literals.append(literal)

        return literals

    # Visit a parse tree produced by DLVParserOutput#query_literal.
    def visitQuery_literal(self, ctx: DLVParserOutput.Query_literalContext):
        if ctx is None or ctx.literal() is None:
            return None
        query_literal = self.visitLiteral(ctx.literal())
        if ctx.NEGATION_AS_FAILURE() is not None:
            query_literal["DLVPY_NEGATION_AS_FAILURE"] = True;
        return query_literal


    # Visit a parse tree produced by DLVParserOutput#literal.
    def visitLiteral(self, ctx: DLVParserOutput.LiteralContext):
        if ctx is None or ctx.atom() is None:
            return None
        atom = self.visitAtom(ctx.atom())
        if atom is None:
            return None
        result = {
            "atom": atom
        }
        if ctx.TRUE_NEGATION() is not None:
            result["DLVPY_TRUE_NEGATION"] = True
        return result

    # Visit a parse tree produced by DLVParserOutput#atom.
    def visitAtom(self, ctx: DLVParserOutput.AtomContext):
        if ctx is None or ctx.NAME() is None:
            return None
        atom = {
            "name": ctx.NAME().getText(),
            "terms": []
        }
        if ctx.term() is None:
            return atom

        for term_ctx in ctx.term():
            atom["terms"].append(self.visitTerm(term_ctx))

        return atom

    # Visit a parse tree produced by DLVParserOutput#term.
    def visitTerm(self, ctx: DLVParserOutput.TermContext):
        if ctx is None:
            return None
        if ctx.STRING():
            return DLVMapper.mapValueFromDLVFormat(ctx.STRING().getText()[1: -1])
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        if ctx.atom():
            atom = self.visitAtom(ctx.atom())
            if atom is None or (atom["name"] == "none" and atom["terms"] is not None and len(atom["terms"]) == 0):
                return None
            if atom['name'] == 'negative_integer':
                return -1 * int(str(atom["terms"][0]))
            if atom["name"] == 'float' or atom["name"] == 'negative_float':
                float_value = float(str(atom["terms"][0]) + "." + str(atom["terms"][1]))
                return -1 * float_value if atom["name"] == 'negative_float' else float_value
            if atom["name"] == 'complex':
                return complex(float(str(atom["terms"][0])), float(str(atom["terms"][1])))
            return atom["name"] + ('' if len(atom["terms"]) == 0 else (
                        '(' + ','.join([str(term) for term in atom["terms"]]) + ')'))
        if ctx.term():
            return [self.visitTerm(term_ctx) for term_ctx in ctx.term()]
        return None

    # Visit a parse tree produced by DLVParserOutput#witness.
    def visitWitness(self, ctx: DLVParserOutput.WitnessContext):
        if ctx is None or ctx.model() is None:
            return None
        return self.visitModel(ctx.model())

    # Visit a parse tree produced by DLVParserOutput#cost.
    def visitCost(self, ctx: DLVParserOutput.CostContext):
        if ctx is None or ctx.cost_amount() is None:
            return []
        return [self.visitCost_amount(cost_amount_ctx) for cost_amount_ctx in ctx.cost_amount()]

    # Visit a parse tree produced by DLVParserOutput#cost_amount.
    def visitCost_amount(self, ctx: DLVParserOutput.Cost_amountContext):
        if ctx is None or ctx.INTEGER() is None:
            return None
        return {
            "weight": int(ctx.INTEGER(0).getText()),
            "level": int(ctx.INTEGER(1).getText())
        }


del DLVParserOutput
