# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)


@app.route('/add')
def sum_query():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    sum = add(a, b)
    return str(sum)


@app.route('/sub')
def sub_query():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    min = sub(a, b)
    return str(min)


@app.route('/mult')
def mult_query():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = mult(a, b)
    return str(res)


@app.route('/div')
def div_query():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    divide = div(a, b)
    return str(divide)


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route('/math/<ops>')
def do_math(ops):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    results = OPERATIONS[ops](a, b)
    return str(results)
