from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    number1 = data['number1']
    operator = data['operator']
    number2 = data['number2']
    
    result = perform_calculation(number1, operator, number2)
    
    log_calculation(number1, operator, number2, result)
    
    return jsonify({'result': result})

def perform_calculation(number1, operator, number2):
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

def log_calculation(number1, operator, number2, result):
    calculation = f'Calculation: {number1} {operator} {number2} = {result}\n'
    with open('calculation.log', 'a') as file:
        file.write(calculation)

if __name__ == '__main__':
    app.run(port=5001)
