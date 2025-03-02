class Calculator:

    @staticmethod
    def divide(x: int | float, y: int | float) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        if y == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return x / y

    @staticmethod
    def add(x: int | float, y: int | float) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Both arguments should be numeric')
        return x + y


if __name__ == '__main__':
    calculator = Calculator()
