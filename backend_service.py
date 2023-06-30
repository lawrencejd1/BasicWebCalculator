from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve the JSON data from the request
    data = request.get_json()
    number1 = data['number1']
    operator = data['operator']
    number2 = data['number2']

    # Perform the calculation based on the operator
    result = perform_calculation(number1, operator, number2)

    # Return the result as a JSON response
    return jsonify({'result': result})

def perform_calculation(number1, operator, number2):
    # Perform the calculation based on the operator
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if number2 != 0:
            return number1 / number2
        else:
            return 'Error: Division by zero'
    else:
        return 'Error: Invalid operator'


if __name__ == '__main__':
    app.run(port=5001)
