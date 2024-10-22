import re

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # Reference to another Node
        self.right = right  # Reference to another Node
        self.value = value  # Optional value for operand nodes

    def to_dict(self):
        """Convert the Node to a dictionary (for easier JSON serialization)"""
        return {
            "type": self.type,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
            "value": self.value
        }

    @staticmethod
    def from_dict(data):
        """Convert a dictionary to a Node"""
        left = Node.from_dict(data['left']) if data.get('left') else None
        right = Node.from_dict(data['right']) if data.get('right') else None
        return Node(type=data['type'], left=left, right=right, value=data.get('value'))

def create_ast_from_rule(rule_string):
    """Create AST from a rule string."""
    tokens = re.split(r'(\s+)', rule_string)  # Split by whitespace
    stack = []
    current_node = None

    for token in tokens:
        token = token.strip()
        if not token:
            continue
        if token in ['AND', 'OR']:
            current_node = Node(type='operator', value=token)
            if stack:
                current_node.left = stack.pop()
            stack.append(current_node)
        else:
            # For operands (conditions)
            parts = re.split(r'(<|<=|>|>=|=|!=)', token)  # Split by operators
            if len(parts) == 3:
                left_operand = parts[0].strip()
                operator = parts[1].strip()
                right_operand = parts[2].strip()
                operand_node = Node(type='operand', value={
                    'left': left_operand,
                    'operator': operator,
                    'right': right_operand
                })
                stack.append(operand_node)

    # The root of the AST will be the last item in the stack
    return stack.pop() if stack else None


def evaluate_ast(ast, user_data):
    if ast.type == 'operator':
        left_value = evaluate_ast(ast.left, user_data)
        right_value = evaluate_ast(ast.right, user_data)

        print(f"Evaluating operator: {ast.value} with left_value: {left_value}, right_value: {right_value}")

        if ast.value == 'AND':
            return left_value and right_value
        elif ast.value == 'OR':
            return left_value or right_value
    elif ast.type == 'operand':
        left = ast.value['left']
        operator = ast.value['operator']
        right = ast.value['right']

        user_value = user_data.get(left)

        print(f"Evaluating operand: {left} {operator} {right} (user_value: {user_value})")

        # Check if right should be an int or str
        right_value = int(right) if right.isdigit() else right

        if operator == '>':
            return user_value > right_value
        elif operator == '=':
            return user_value == right_value
        elif operator == '<':
            return user_value < right_value
        # Add more operators as needed

    return False


def combine_ast(rules):
    """Combine multiple ASTs into a single AST (e.g., using OR as the root operator)"""
    if not rules:
        return None
    combined = rules[0]
    for rule in rules[1:]:
        combined = Node("operator", left=combined, right=rule, value="OR")
    return combined
