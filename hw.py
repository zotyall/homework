# Import Flask to create the web server
# Import request to get values from the URL
from flask import Flask, request 

# Create the Flask application
app = Flask(__name__)


# Add endpoint
@app.get("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"a": a, "b": b, "operation": "addition", "result": a + b}

# Subtract endpoint
@app.get("/subtract")
def subtract():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"a": a, "b": b, "operation": "subtraction", "result": a - b}
# multiply endpoint
@app.get("/multiply")
def multiply():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"a": a, "b": b, "operation": "multiplication", "result": a * b}
# division endpoint
@app.get("/divide")
def divide():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"a": a, "b": b, "operation": "division", "result": a / b}

# Start the web server
app.run()