# Generated from ..\dlv\grammar_input\DLVParserInput.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DLVParserInput import DLVParserInput
else:
    from DLVParserInput import DLVParserInput

# This class defines a complete listener for a parse tree produced by DLVParserInput.
class DLVParserInputListener(ParseTreeListener):

    # Enter a parse tree produced by DLVParserInput#codeinput.
    def enterCodeinput(self, ctx:DLVParserInput.CodeinputContext):
        pass

    # Exit a parse tree produced by DLVParserInput#codeinput.
    def exitCodeinput(self, ctx:DLVParserInput.CodeinputContext):
        pass


    # Enter a parse tree produced by DLVParserInput#line.
    def enterLine(self, ctx:DLVParserInput.LineContext):
        pass

    # Exit a parse tree produced by DLVParserInput#line.
    def exitLine(self, ctx:DLVParserInput.LineContext):
        pass


    # Enter a parse tree produced by DLVParserInput#comment.
    def enterComment(self, ctx:DLVParserInput.CommentContext):
        pass

    # Exit a parse tree produced by DLVParserInput#comment.
    def exitComment(self, ctx:DLVParserInput.CommentContext):
        pass


    # Enter a parse tree produced by DLVParserInput#schema.
    def enterSchema(self, ctx:DLVParserInput.SchemaContext):
        pass

    # Exit a parse tree produced by DLVParserInput#schema.
    def exitSchema(self, ctx:DLVParserInput.SchemaContext):
        pass


    # Enter a parse tree produced by DLVParserInput#ancestor_key.
    def enterAncestor_key(self, ctx:DLVParserInput.Ancestor_keyContext):
        pass

    # Exit a parse tree produced by DLVParserInput#ancestor_key.
    def exitAncestor_key(self, ctx:DLVParserInput.Ancestor_keyContext):
        pass


    # Enter a parse tree produced by DLVParserInput#name.
    def enterName(self, ctx:DLVParserInput.NameContext):
        pass

    # Exit a parse tree produced by DLVParserInput#name.
    def exitName(self, ctx:DLVParserInput.NameContext):
        pass


    # Enter a parse tree produced by DLVParserInput#key.
    def enterKey(self, ctx:DLVParserInput.KeyContext):
        pass

    # Exit a parse tree produced by DLVParserInput#key.
    def exitKey(self, ctx:DLVParserInput.KeyContext):
        pass


    # Enter a parse tree produced by DLVParserInput#key_properties.
    def enterKey_properties(self, ctx:DLVParserInput.Key_propertiesContext):
        pass

    # Exit a parse tree produced by DLVParserInput#key_properties.
    def exitKey_properties(self, ctx:DLVParserInput.Key_propertiesContext):
        pass


    # Enter a parse tree produced by DLVParserInput#key_concat.
    def enterKey_concat(self, ctx:DLVParserInput.Key_concatContext):
        pass

    # Exit a parse tree produced by DLVParserInput#key_concat.
    def exitKey_concat(self, ctx:DLVParserInput.Key_concatContext):
        pass


    # Enter a parse tree produced by DLVParserInput#key_autoincrement.
    def enterKey_autoincrement(self, ctx:DLVParserInput.Key_autoincrementContext):
        pass

    # Exit a parse tree produced by DLVParserInput#key_autoincrement.
    def exitKey_autoincrement(self, ctx:DLVParserInput.Key_autoincrementContext):
        pass



del DLVParserInput