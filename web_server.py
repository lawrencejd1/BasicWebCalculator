from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Enter a Single Operand Problem</h1>
        <form method="POST" action="/calculate">
            <input type="number" name="number1" placeholder="First Number" required><br><br>
            <select name="operator" required>
                <option value="+">+</option>
                <option value="-">-</option>
                <option value="*">*</option>
                <option value="/">/</option>
            </select><br><br>
            <input type="number" name="number2" placeholder="Second Number" required><br><br>
            <input type="submit" value="Calculate">
        </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve input values from the form
    number1 = float(request.form['number1'])
    operator = request.form['operator']
    number2 = float(request.form['number2'])

    # URL of the backend service
    backend_url = 'http://localhost:5001/calculate'  # Assuming backend service is running on port 5001

    # Send a POST request to the backend service with input values
    response = requests.post(backend_url, json={'number1': number1, 'operator': operator, 'number2': number2})

    # Extract the result from the response
    result = response.json()['result']

    # Return the result as a response
    return f'<h1>Result: {result}</h1>'

if __name__ == '__main__':
    app.run()
