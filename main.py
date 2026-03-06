import argparse

from antlr4 import CommonTokenStream, InputStream
from lib.antlr4.grammar.nishikiLexer import nishikiLexer
from lib.antlr4.grammar.nishikiParser import nishikiParser

from src.error_listener import (
    FriendlyErrorListener,
    RuntimeErrorListener,
    SyntaxErrorListener,
)
from src.visitor import Visitor


def evaluate(path):
    with open(path, encoding="utf-8") as source_file:
        source_text = source_file.read()

    stream = InputStream(source_text)

    lexer = nishikiLexer(stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(FriendlyErrorListener())

    token_stream = CommonTokenStream(lexer)

    parser = nishikiParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(FriendlyErrorListener())

    tree = parser.program()
    visitor = Visitor(source_text)
    return visitor.visit(tree)


def main():
    parser = argparse.ArgumentParser(description="Nishiki interpreter")
    parser.add_argument("file", help="Path to a Nishiki source file")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="Nishiki Interpreter 1.0",
    )

    args = parser.parse_args()

    try:
        result = evaluate(args.file)
        print(result)
    except SyntaxErrorListener as e:
        print(e)
    except RuntimeErrorListener as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error\n\t{str(e)}")


if __name__ == "__main__":
    main()
