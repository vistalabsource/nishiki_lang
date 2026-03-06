from lib.antlr4.grammar.nishikiVisitor import nishikiVisitor

from src.error_listener import format_runtime_error


class Visitor(nishikiVisitor):
    def __init__(self, source_text):
        super().__init__()
        self.source_text = source_text

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitMulDiv(self, ctx):
        x = self.visit(ctx.expr(0))
        y = self.visit(ctx.expr(1))
        op = ctx.op.text

        if op == "*":
            return x * y

        if y == 0:
            raise format_runtime_error(
                self.source_text,
                ctx.op.line,
                ctx.op.column,
                "Division by zero is not allowed.",
            )

        return x / y

    def visitAddSub(self, ctx):
        x = self.visit(ctx.expr(0))
        y = self.visit(ctx.expr(1))
        op = ctx.op.text

        if op == "+":
            return x + y

        return x - y

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
