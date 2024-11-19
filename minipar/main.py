import sys
from lexico import lexer
from sintatico import parser
from semantico import interpret

def read_program(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.mp>")
        sys.exit(1)

    file_path = sys.argv[1]
    program_code = read_program(file_path)

    # Análise léxica e sintática
    ast = parser.parse(program_code, lexer=lexer)

    if ast:
        # Execução semântica
        interpret(ast)

if __name__ == "__main__":
    main()
