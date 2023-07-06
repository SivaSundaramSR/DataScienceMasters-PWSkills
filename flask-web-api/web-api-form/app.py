from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        if ops == "add":
            ans = num1 + num2
            result = f"The sum of {num1} and {num2} is {ans}"
        if ops == "subtract":
            ans = num1 - num2
            result = f"The sum of {num1} and {num2} is {ans}"
        if ops == "multiply":
            ans = num1 * num2
            result = f"The sum of {num1} and {num2} is {ans}"
        if ops == "divide":
            ans = (1.00*num1)/num2
            result = f"The sum of {num1} and {num2} is {ans}"
        return render_template("results.html", result = result)

@app.route('/postman_action', methods=['POST'])
def math_ops_postman():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])
        if ops == "add":
            ans = num1 + num2
            result = f"The sum of {num1} and {num2} is {ans}"
        if ops == "subtract":
            ans = num1 - num2
            result = f"The sum of {num1} and {num2} is {ans}"
        if ops == "multiply":
            ans = num1 * num2
            result = f"The sum of {num1} and {num2} is {ans}"
        if ops == "divide":
            ans = (1.00*num1)/num2
            result = f"The sum of {num1} and {num2} is {ans}"
        return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")