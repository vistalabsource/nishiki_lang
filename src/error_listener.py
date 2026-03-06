from antlr4.error.ErrorListener import ErrorListener
from colorama import Fore, init

init(autoreset=True)


class SyntaxErrorListener(Exception):
    pass


class RuntimeErrorListener(Exception):
    pass


def make_pointer(text, line, column):
    lines = text.splitlines()
    if not lines:
        return ""

    if line < 1 or line > len(lines):
        return ""

    target_line = lines[line - 1]
    pointer_line = " " * column + "^"
    return f"{target_line}\n{pointer_line}"


def format_runtime_error(text, line, column, message):
    pointer = make_pointer(text, line, column)
    return RuntimeErrorListener(
        f"{Fore.MAGENTA}Runtime Error\n"
        f"  Line: {line}\n"
        f"  Column: {column + 1}\n"
        f"  Message: {message}\n\n"
        f"{Fore.BLUE}{pointer}"
    )


class FriendlyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        text = ""
        input_stream = getattr(recognizer, "inputStream", None)
        if input_stream is not None and hasattr(input_stream, "strdata"):
            text = input_stream.strdata

        pointer = make_pointer(text, line, column)

        token = ""
        if offendingSymbol is not None and hasattr(offendingSymbol, "text"):
            token = offendingSymbol.text

        if token == "<EOF>":
            detail = "Input ended in the middle of an expression. A number or ')' is missing."
        elif token:
            detail = f"Invalid syntax near token '{token}'."
        else:
            detail = "Invalid expression syntax."

        raise SyntaxErrorListener(
            f"{Fore.MAGENTA}Syntax Error\n"
            f"  Line: {line}\n"
            f"  Column: {column + 1}\n"
            f"  Message: {detail}\n\n"
            f"{Fore.BLUE}{pointer}"
        )
