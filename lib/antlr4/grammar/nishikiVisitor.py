# Generated from ./grammar/nishiki.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .nishikiParser import nishikiParser
else:
    from nishikiParser import nishikiParser

# This class defines a complete generic visitor for a parse tree produced by nishikiParser.

class nishikiVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by nishikiParser#program.
    def visitProgram(self, ctx:nishikiParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nishikiParser#statement.
    def visitStatement(self, ctx:nishikiParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nishikiParser#MulDiv.
    def visitMulDiv(self, ctx:nishikiParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nishikiParser#AddSub.
    def visitAddSub(self, ctx:nishikiParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nishikiParser#Parens.
    def visitParens(self, ctx:nishikiParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nishikiParser#Int.
    def visitInt(self, ctx:nishikiParser.IntContext):
        return self.visitChildren(ctx)



del nishikiParser