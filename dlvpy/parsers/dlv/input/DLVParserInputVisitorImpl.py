if __name__ is not None and "." in __name__:
    from .DLVLexerInput import DLVLexerInput
    from .DLVParserInput import DLVParserInput
    from .DLVParserInputVisitor import DLVParserInputVisitor
else:
    from DLVLexerInput import DLVLexerInput
    from DLVParserInput import DLVParserInput
    from DLVParserInputVisitor import DLVParserInputVisitor


# This class defines a complete generic visitor for a parse tree produced by DLVParserInput.

class DLVParserInputVisitorImpl(DLVParserInputVisitor):

    # Visit a parse tree produced by DLVParserInput#codeinput.
    def visitCodeinput(self, ctx: DLVParserInput.CodeinputContext):
        schemas = []
        try:
            lines_ctx = ctx.line()
            if lines_ctx is None:
                return schemas

            schemas = []
            for line in lines_ctx:
                lineVisited = self.visitLine(line)
                if lineVisited is None:
                    continue
                schemas.append(lineVisited)
        except RuntimeError:
            schemas = []
        return schemas

    # Visit a parse tree produced by DLVParserInput#line.
    def visitLine(self, ctx: DLVParserInput.LineContext):
        comments_ctx = ctx.comment()
        if comments_ctx is None:
            return None
        return self.visitComment(comments_ctx)

    # Visit a parse tree produced by DLVParserInput#comment.
    def visitComment(self, ctx: DLVParserInput.CommentContext):
        schema_ctx: DLVParserInput.SchemaContext = ctx.schema()
        if schema_ctx is None:
            return None

        return self.visitSchema(schema_ctx)

    # Visit a parse tree produced by DLVParserInput#schema.
    def visitSchema(self, ctx:DLVParserInput.SchemaContext):
        is_schema_valid: bool = True

        schema_result = {
            "name": self.visitName(ctx.name())
        }

        ancestors = []
        for ancestor in ctx.ancestor_key():
            ancestor_value = self.visitAncestor_key(ancestor)
            if ancestor_value is None:
                return None
            ancestors.append(ancestor_value)

        errors = []
        if len(ancestors) == 1:
            if ancestors[0].strip() == schema_result["name"].strip():
                errors.append("[!] Ancestor Key \"" + schema_result["name"] + "\" of schema \"" + schema_result["name"] + "\" generate Recursion!")
                is_schema_valid = False

        schema_result["ancestors_path"] = ancestors

        if ctx.key() is None:
            errors.append("[!] No Key found for schema \"" + schema_result["name"] + "\"!")
            is_schema_valid = False

        schema_result["key"] = self.visitKey(ctx.key())
        schema_result["properties"] = [] if ctx.STRING() is None else [x.getText()[1:-1] for x in ctx.STRING()]

        if schema_result["key"] is not None:
            if "autoincrement" in schema_result["key"]:
                if not schema_result["key"]["autoincrement"]:
                    errors.append("[-] Invalid key autoincrement for schema \"" + schema_result["name"] + "\"!")
                    is_schema_valid = False
            elif "properties" in schema_result["key"]:
                for prop in schema_result["key"]["properties"]:
                    if prop not in schema_result["properties"]:
                        errors.append("[!] Key property \"" + prop + "\" isn\'t in schema properties of \"" + schema_result["name"] + "\" schema!")
                        is_schema_valid = False
            else:
                errors.append("[-] Invalid key definition for schema \"" + schema_result["name"] + "\"!")
                is_schema_valid = False

        if not is_schema_valid:
            errors.append("[!] Schema \"" + schema_result["name"] + "\" isn\'t valid!")
            print("\n".join(errors))
            return None

        return schema_result

    # Visit a parse tree produced by DLVParserInput#ancestor_key.
    def visitAncestor_key(self, ctx: DLVParserInput.Ancestor_keyContext):
        if ctx is None:
            return None
        if ctx.name() is None:
            return None
        return self.visitName(ctx.name())

    # Visit a parse tree produced by DLVParserInput#name.
    def visitName(self, ctx: DLVParserInput.NameContext):
        if ctx is None:
            return None
        if ctx.NAME() is not None:
            return ctx.NAME().getText()
        if ctx.SCHEMA_KEY_LABEL() is not None:
            return ctx.SCHEMA_KEY_LABEL().getText()
        if ctx.ANCESTOR_KEY_LABEL() is not None:
            return ctx.ANCESTOR_KEY_LABEL().getText()
        if ctx.KEY_LABEL() is not None:
            return ctx.KEY_LABEL().getText()
        if ctx.KEY_AUTOINCREMENT() is not None:
            return ctx.KEY_AUTOINCREMENT().getText()
        return None

    # Visit a parse tree produced by DLVParserInput#key.
    def visitKey(self, ctx: DLVParserInput.KeyContext):
        if ctx is None or (ctx.key_properties() is None and ctx.key_autoincrement() is None):
            return None
        return self.visitKey_autoincrement(ctx.key_autoincrement()) if ctx.key_autoincrement() is not None else self.visitKey_properties(ctx.key_properties())

    # Visit a parse tree produced by DLVParserInput#key_properties.
    def visitKey_properties(self, ctx: DLVParserInput.Key_propertiesContext):
        if ctx is None:
            return None
        key = {
            "properties": [x.getText()[1:-1] for x in ctx.STRING()]
        }

        if ctx.key_concat() is not None:
            key["concat"] = self.visitKey_concat(ctx.key_concat())

        return key


    # Visit a parse tree produced by DLVParserInput#key_concat.
    def visitKey_concat(self, ctx:DLVParserInput.Key_concatContext):
        if ctx is None:
            return None
        return ctx.STRING().getText()[1:-1]

    # Visit a parse tree produced by DLVParserInput#key_autoincrement.
    def visitKey_autoincrement(self, ctx: DLVParserInput.Key_autoincrementContext):
        if ctx is None:
            return None
        return {
            "autoincrement": True if ctx.KEY_AUTOINCREMENT().getText() == "autoincrement" else False
        }




del DLVParserInput
