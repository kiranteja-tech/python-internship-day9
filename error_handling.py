import logging

# 1. Configure logging (log file creation)
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception
class NegativeNumberError(Exception):
    pass

def divide_numbers(a, b):
    try:
        # Simulate runtime errors
        if a < 0 or b < 0:
            raise NegativeNumberError("Negative numbers are not allowed")

        result = a / b

    except ZeroDivisionError as e:
        logging.error("ZeroDivisionError occurred")
        print("Error: Cannot divide by zero")

    except TypeError as e:
        logging.error("TypeError occurred")
        print("Error: Invalid data type")

    except NegativeNumberError as e:
        logging.error(str(e))
        print("Error:", e)

    else:
        print("Division Result:", result)

    finally:
        print("Operation finished\n")

# Function calls (runtime error simulation)
divide_numbers(10, 0)
divide_numbers(10, "a")
divide_numbers(-5, 2)
divide_numbers(10, 2)
