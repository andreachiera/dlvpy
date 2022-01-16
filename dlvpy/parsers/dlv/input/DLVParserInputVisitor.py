# Generated from ..\dlv\grammar_input\DLVParserInput.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DLVParserInput import DLVParserInput
else:
    from DLVParserInput import DLVParserInput

# This class defines a complete generic visitor for a parse tree produced by DLVParserInput.

class DLVParserInputVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DLVParserInput#codeinput.
    def visitCodeinput(self, ctx:DLVParserInput.CodeinputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#line.
    def visitLine(self, ctx:DLVParserInput.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#comment.
    def visitComment(self, ctx:DLVParserInput.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#schema.
    def visitSchema(self, ctx:DLVParserInput.SchemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#ancestor_key.
    def visitAncestor_key(self, ctx:DLVParserInput.Ancestor_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#name.
    def visitName(self, ctx:DLVParserInput.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#key.
    def visitKey(self, ctx:DLVParserInput.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#key_properties.
    def visitKey_properties(self, ctx:DLVParserInput.Key_propertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#key_concat.
    def visitKey_concat(self, ctx:DLVParserInput.Key_concatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLVParserInput#key_autoincrement.
    def visitKey_autoincrement(self, ctx:DLVParserInput.Key_autoincrementContext):
        return self.visitChildren(ctx)



del DLVParserInput