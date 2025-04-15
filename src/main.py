line = input("Operación: ")

[lhs, operand, rhs] = line.split()

lhs = float(lhs)
rhs = float(rhs)


def operate(lhs: float, rhs: float, operand: str):
    return "Operación inválida"


result = operate(lhs, rhs, operand)
print(result)

