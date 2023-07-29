from flask import Flask, request, jsonify 

obj = Flask(__name__)

@obj.route("/")
def welcome():
    return "Welcome to Flask"

@obj.route("/cal", methods = ['GET'])
def mathOperation():

    ### getting varible values from json file
    operation = request.json["operation"]
    num1 = request.json["number1"]
    num2 = request.json["number2"]

    if operation == 'add':
        res = num1 + num2
    elif operation == 'multiply':
        res = num1 * num2
    elif operation == 'subtract':
        res = num1 - num2
    elif operation == 'divide':
        res = num1/num2
    else:
        res = 'invalide operation'
    
    return jsonify(res)

if __name__ == '__main__':
    obj.run(debug=True)