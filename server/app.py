#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# @app.route('/signup', methods=['POST'])
@app.route('/')
def index():
    # pass
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# /print/parameter
@app.route('/print/<string:parameter>')
def print_string(parameter):
    # pass
    # return f'<p>{parameter}</p>'
    print(parameter)
    return f'{parameter}'

# /count/parameter
@app.route('/count/<int:parameter>')
def count(parameter):
    # pass
    # for number in range(parameter):
    return '<br>'.join(str(i) for i in range(1, parameter + 1))

# /math/<num1>/<operation>/<num2>.
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "%":
        result = num1 % num2
    elif operation== "div":
        result= num1 / num2
        # return f'{num1 / num2}'
    else:
        return "Invalid operation", 400

    return f"The result of {num1} {operation} {num2} is: {result}"

# @app.route('/math/<int:num1>/<string:operation>/<int:num2>.')
# def math(num1, operation, num2):
#     # pass
#     if operation== "+":
#         # pass
#         result= num1 + num2
#         # return f'{num1 + num2}'
#     if operation== "-":
#         result= num1 - num2
#         # return f'{num1 - num2}'
#     if operation== "*":
#         result= num1 * num2
#         # return f'{num1 * num2}'
#     if operation== "/":
#         result= num1 / num2
#         # return f'{num1 / num2}'
#     if operation== "%":
#         result= num1 % num2
#         # return f'{num1 % num2}'
#     return f'{result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
