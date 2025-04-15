def calculate(src: str):
    [lhs, operand, rhs] = src.split()

    lhs = float(lhs)
    rhs = float(rhs)

    if operand == "+":
        return lhs + rhs

    if operand == "-":
        return lhs - rhs

    if operand == "*":
        return lhs * rhs

    if operand == "/":
        return lhs / rhs

    return "Operación inválida"
