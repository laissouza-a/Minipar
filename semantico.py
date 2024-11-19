symbol_table = {}

def interpret(program):
    for stmt in program:
        execute_stmt(stmt)

def execute_stmt(stmt):
    if stmt[0] == 'SEQ':
        for s in stmt[1]:
            execute_stmt(s)
    elif stmt[0] == 'ATRIB':
        symbol_table[stmt[1]] = evaluate_expr(stmt[2])

def evaluate_expr(expr):
    if isinstance(expr, int):
        return expr
    elif isinstance(expr, str):
        return symbol_table.get(expr, 0)
    elif isinstance(expr, tuple):
        op, left, right = expr
        left_val = evaluate_expr(left)
        right_val = evaluate_expr(right)
        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        elif op == '/':
            return left_val / right_val
