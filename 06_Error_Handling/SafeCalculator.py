class InvalidOperatorError(Exception):
    """Raised when the operator is not one of + - * / % **."""


def Calc(a: float, b: float, operator: str) -> float:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "%":
        return a % b
    elif operator == "**":
        return a**b
    raise InvalidOperatorError(f"'{operator}' is not a supported operator")


def getNumber(prompt: str) -> float:
    # Keep asking until the user types a valid number.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a number. Try again.")


def main() -> None:
    a = getNumber("First number: ")
    operator = input("Operator (+ - * / % **): ").strip()
    b = getNumber("Second number: ")

    try:
        result = Calc(a, b, operator)
    except ZeroDivisionError:
        print("Error: you cannot divide by zero.")
    except InvalidOperatorError as error:
        print(f"Error: {error}")
    else:
        print(f"{a} {operator} {b} = {result}")
    finally:
        print("Calculation finished.")


if __name__ == "__main__":
    main()
