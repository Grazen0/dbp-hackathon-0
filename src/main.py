line = input("Operación: ")

[lhs, operand, rhs] = line.split()

lhs = float(lhs)
rhs = float(rhs)


def operate(lhs: float, rhs: float, operand: str):
    return "Operación inválida"

def multiplication(lhs: float, rhs: float, operand: str):
    if operand == "*":
        return lhs*rhs
    else:
        return "Operación inválida"

result = operate(lhs, rhs, operand)
print(result)

