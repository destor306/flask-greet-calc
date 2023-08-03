# Put your app in here.
from flask import Flask, request
from operations import add, mult, sub, div

app = Flask(__name__)

@app.route('/add')
def _add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a,b)    
    return str(result)

@app.route('/sub')
def _sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a,b)    
    return str(result)

@app.route('/mult')
def _mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a,b)    
    return str(result)

@app.route('/div')
def _div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a,b)    
    return str(result)

method ={
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<oper>')
def do_math(oper):
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = method[oper](a,b)
    return str(result)