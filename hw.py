from flask import Flask, request 

app = Flask(__name__)

@app.get("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"a": a, "b": b, "operation": "addition", "result": a + b}

@app.get("/subtract")
def subtract():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"a": a, "b": b, "operation": "subtraction", "result": a - b}

@app.get("/multiply")
def multiply():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"a": a, "b": b, "operation": "multiplication", "result": a * b}

@app.get("/divide")
def divide():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"a": a, "b": b, "operation": "division", "result": a / b}

app.run()