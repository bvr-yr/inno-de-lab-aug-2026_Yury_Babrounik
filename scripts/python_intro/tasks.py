import operator as op
import sys
from random import randint


def read_int(prompt: str, *, positive: bool = False) -> int:
    """Shared helper.

    reads value from user input with a prompt,
    returning int if valid, or showing error msg

    optional bool 'positive' (default False) restricts
    valid values to be > 0
    """
    while True:
        value = input(prompt).strip()
        try:
            value_int = int(value)
            if positive and value_int < 1:
                # quote value with !r specifier
                print(f"{value!r} should be positive")
                continue

        except ValueError:
            print(f"{value!r} is not an integer")
        else:
            return value_int


def task_1() -> None:
    """Task 1: Welcome."""
    user_name = input("What is your name?\n")
    print(f"Hi there, {user_name}! Nice to meet you")


def task_2() -> None:
    """Task 2: Rectangle area."""
    a = read_int("Enter rectangle length: ", positive=True)
    b = read_int("Enter rectangle width: ", positive=True)
    # not declaring separate area var, better calculate directly in f-string
    print(f"Rectangle area is: {a * b}")


def task_3() -> None:
    """Task 3: Temperature converter."""
    ABS_ZERO = -273.15  # noqa: N806

    while True:
        # reading an int is an assumption here
        celsius = read_int("Enter the temperature in Celsius degrees: ")

        # common sense
        if celsius < ABS_ZERO:
            print(f"Temperature should not be below absolute zero ({ABS_ZERO}°C)")
        else:
            """
            .1f format specifier is used for convenient float output control,
            though an expression is already float (because of division)
            and would use default float formatting

            task example output uses ',' as float decimal sep, but this is
            likely caused by locale-specific env. specifically, ru_RU uses comma
            keep default dot
            """
            print(f"{celsius}°C is {celsius * 9 / 5 + 32:.1f}°F")
            break


def task_4() -> None:
    """Task 4: Parity check."""
    number = read_int("Enter an integer: ")
    """
    a little note on this:
        I have a little bit of rust experience, so I used to rich inline
        format expressions. But I'm surprised f-string allows to do this
    """
    print(f"Number {number} is {'even' if number % 2 == 0 else 'odd'}.")


def task_5() -> None:
    """Task 5: Guess the number."""
    rand_lo = 1
    rand_hi = 20
    max_attempts = 5

    number = randint(rand_lo, rand_hi)
    attempts = 0

    print(
        f"Guess the number from {rand_lo} to {rand_hi}. "
        f"You have {max_attempts} attempts!",
    )

    while attempts < max_attempts:
        attempts += 1
        input_number = read_int(f"Attempt {attempts}. Enter number: ")

        if input_number == number:
            print("You have guessed! Great job.")
            break

        too_what = "little" if input_number < number else "much"

        if attempts == max_attempts:
            print(f"Too {too_what}! No attempts left, you lost!")
        else:
            print(f"Too {too_what}! Attempts left: {max_attempts - attempts}\n")


def task_6() -> None:
    """Task 6: Calculator.

    optional
    """

    # unlike shared, define this nested in only place it's used
    def read_number(prompt: str) -> float:
        while True:
            value = input(prompt).strip()
            try:
                return float(value)
            except ValueError:
                print(f"{value!r} is not a number")

    # config-like dict, that can be extended with additional
    # operators provided by operator module
    operations = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "/": op.truediv,
    }

    # iterate through dict's keys and join with ','
    ops_pretty = f"({', '.join(operations)})"

    a = read_number("Enter first number: ")
    b = read_number("Enter second number: ")

    while True:
        input_op = input(f"Enter operator {ops_pretty}: ").strip()
        if input_op in operations:
            try:
                print(f"Result: {a} {input_op} {b} = {operations[input_op](a, b)}")
            except ZeroDivisionError:
                """
                simply exit with msg for now.
                we need another flow depending on what we want:
                    - change operator
                    - change 2nd number
                    - start over
                """
                print("Division by zero, abort")
                sys.exit(3)
            break

        print(f"{input_op!r} is not a valid operator")


HELP = """
Please pass a task number as an argument.

Task list:
    1. Welcome
    2. Rectangle area
    3. Temperature converter
    4. Parity check
    5. Guess the number
    6. Calculator (optional)
"""


def main() -> None:
    """Run selected task.

    using argparse would be overhead, so simply parse sys.argv
    using match-case instead of if-else cause it feels rusty to me :)
    """
    task = sys.argv[1] if len(sys.argv) > 1 else ""

    match task.strip():
        case "1":
            task_1()
        case "2":
            task_2()
        case "3":
            task_3()
        case "4":
            task_4()
        case "5":
            task_5()
        case "6":
            task_6()
        case _:
            print(HELP)
            sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(2)
