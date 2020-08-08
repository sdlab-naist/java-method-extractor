import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from JavaLexer import JavaLexer
from JavaParser import JavaParser
from JavaParserListener import JavaParserListener


class MethodListener(JavaParserListener):
    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        print("{0} {1} {2}".format(ctx.start.line,
                                   ctx.start.column, ctx.IDENTIFIER()))


def main():
    parser = JavaParser(CommonTokenStream(
        JavaLexer(FileStream(sys.argv[1], encoding="utf-8"))))

    walker = ParseTreeWalker()
    listener = MethodListener()

    walker.walk(listener, parser.compilationUnit())


if __name__ == "__main__":
    main()
