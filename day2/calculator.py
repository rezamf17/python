def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Tidak bisa membagi dengan nol")
    return n1 / n2
if __name__ == "__main__":
    print("Addition: 10 + 5 =", add(10, 5))
    print("Subtraction: 10 - 5 =", subtract(10, 5))
    print("Multiplication: 10 * 5 =", multiply(10, 5))
    print("Division: 10 / 5 =", divide(10, 5))
    print("Division by zero: 10 / 0 =", divide(10, 0))
