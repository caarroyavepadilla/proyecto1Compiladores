from flask import Flask, render_template, request, session
import sys
from antlr4 import *
import antlr4 as antlr4
from decafLexer import decafLexer
from decafListener import decafListener
from decafParser import decafParser
from decafVisitor import decafVisitor
from antlr4.tree.Trees import Trees
import tables as visitor
import  typeSystem as tables

app  = Flask(__name__)
app.secret_key = "el topo mayor"


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods = ["POST"])
def get_code():
    errors = []
    code = ""
    session.code = ""
    code = request.form["codigo"]
    session.code = code
    print("errores", errors)
    if code!= " ":
        text = antlr4.InputStream(code)
        lexer = decafLexer(text)
        stream = CommonTokenStream(lexer)
        parser = decafParser(stream)
        tree = parser.program()
        printer = decafListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        x = visitor.myDecafVisitor()
        x.visit(tree)
        errors = visitor.ERRORS
    else:
        errors = []
    return render_template("home.html", errors = errors, code = code)



if __name__ == "__main__":
    app.run(host='localhost', port = 5000, debug = True)