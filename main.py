import re

def sanitize_expression(expression):
    """Fixes invalid characters and symbols in the expression."""
    expression = expression.replace("–", "-")  # Replace en-dash with hyphen
    expression = expression.replace("^", "**")  # Replace ^ with ** for exponentiation
    expression = re.sub(r'(\d+)\s*\(', r'\1*(', expression)  # Fix implicit multiplication
    expression = re.sub(r'\)\s*\(', r')*(', expression)  # Fix adjacent parentheses multiplication
    return expression

def evaluate_expression(expression):
    try:
        expression = sanitize_expression(expression)  # Sanitize input
        result = eval(expression, {"__builtins__": None}, {})  # Safe evaluation
        
        # Convert float ending in .0 to an integer
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
    except Exception as e:
        return f"Error: {e}"

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            line = line.strip()
            if '=' in line:
                expression = line.split('=')[0].strip()
                result = evaluate_expression(expression)
                outfile.write(f"{line} {result}\n")
    print("Processed expressions written to", output_file)

# Example usage
input_file = "input.txt"
output_file = "output.txt"
process_file(input_file, output_file)

