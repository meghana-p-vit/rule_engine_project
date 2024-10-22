from ast_helpers import Node, create_ast_from_rule, evaluate_ast, combine_ast
from database import save_rule_to_db

def create_rule(rule_string):
    """Create a rule from a rule string and store it in the database"""
    rule_ast = create_ast_from_rule(rule_string)
    rule_id = save_rule_to_db(rule_string)
    if rule_id:
        print(f"Rule saved with ID: {rule_id}")
    return rule_ast

def combine_rules(rules):
    """Combine multiple rules into a single AST"""
    ast_list = [create_ast_from_rule(rule) for rule in rules]
    combined_ast = combine_ast(ast_list)
    return combined_ast

def evaluate_rule(rule_ast, user_data):
    """Evaluate the rule AST against user data"""
    return evaluate_ast(Node.from_dict(rule_ast), user_data)
