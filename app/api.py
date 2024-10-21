from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from rule_engine import create_rule, evaluate_rule, combine_rules
from ast_helpers import Node

app = Flask(__name__, template_folder='templates') # Simplified, Flask automatically looks for `templates/`
CORS(app)


# Route to serve the HTML UI
@app.route('/')
def index():
    print("Current working directory:", os.getcwd())
    return render_template('index.html')


# Endpoint to create rule
@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.get_json()
    rule_string = data.get('rule_string', '')

    if not rule_string:
        return jsonify({"error": "Rule string is missing"}), 400

    try:
        rule = create_rule(rule_string)  # Should return an AST object
        if not hasattr(rule, 'to_dict'):
            raise AttributeError("Rule object does not have a 'to_dict' method")

        return jsonify({
            "message": "Rule created successfully!",
            "ast": rule.to_dict()  # Ensure the rule object can be serialized to JSON
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Endpoint to evaluate rule
# Endpoint to evaluate rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.get_json()
    print("Received data:", data)
    rule_ast = data.get('rule_ast', {})
    user_data = data.get('user_data', {})

    if not rule_ast:
        return jsonify({"error": "Rule AST is missing"}), 400
    if not user_data:
        return jsonify({"error": "User data is missing"}), 400

    # Debug output
    print("Rule AST:", rule_ast)
    print("User Data:", user_data)

    try:
        # Ensure numeric values are treated as integers
        user_data['age'] = int(user_data['age'])
        user_data['salary'] = int(user_data['salary'])
        user_data['experience'] = int(user_data['experience'])

        # Call the existing evaluate_rule function instead
        result = evaluate_rule(rule_ast, user_data)  # Correct function call
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Endpoint to combine multiple rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.get_json()
    rules = data.get('rules', [])

    if not rules:
        return jsonify({"error": "Rules are missing"}), 400

    try:
        # Convert each rule dict to Node objects
        rule_asts = [Node.from_dict(rule) for rule in rules]
        combined_rule = combine_rules(rule_asts)  # Should return an AST object (Node)

        if not hasattr(combined_rule, 'to_dict'):
            raise AttributeError("Combined rule object does not have a 'to_dict' method")

        return jsonify({
            "message": "Rules combined successfully!",
            "ast": combined_rule.to_dict()  # Ensure the combined rule object can be serialized to JSON
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)