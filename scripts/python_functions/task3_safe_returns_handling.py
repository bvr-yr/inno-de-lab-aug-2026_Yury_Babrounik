from typing import Any

from consts import DEFAULT_RETURN_INDEX_BASE
from test_data import TASK_3_DATA


def calculate_overdue_fine(
    title: str,
    days_overdue: Any,  # noqa: ANN401
    fine_rate: float,
) -> tuple[float, float] | None:
    """Calculate total fine and index of overdue returns.

    Invalid data types, non-numeric values, and zero overdue days
    are handled and reported without propagating their exceptions.

    Args:
        title: Title of the film.
        days_overdue: Raw number of overdue days.
        fine_rate: Fine per day of overdue.

    Returns:
        Tuple with final fine value and return index,
        or None if calculaction fails.

    """
    try:
        numeric_days = float(days_overdue)
        total_fine: float = numeric_days * fine_rate
        return_index: float = DEFAULT_RETURN_INDEX_BASE / numeric_days
    except TypeError as e:
        print(f"\n\n[TYPE ERROR] Invalid data type for {title!r}: {e}")
    except ValueError as e:
        print(f"\n\n[VALUE ERROR] Unable to convert days to number for {title!r}: {e}")
    except ZeroDivisionError as e:
        # exception message may vary between Python versions
        # so hardcode if 'float division by zero' is needed
        print(f"\n\n[ZERO DIVISION ERROR] No overdue return for {title!r}: {e}")
    else:
        print(f"\nMovie: {title!r} | Total fine: {total_fine}$ | Index: {return_index}")
        return total_fine, return_index
    finally:
        print("\n--- Return transaction check done ---")


def run_tests(data: list[tuple[str, Any, Any]]) -> None:
    """Run tests with provided data.

    Args:
        data: Test data provided by task condition.

    """
    print("=== RETURNS CHECK ===")
    for item in data:
        calculate_overdue_fine(item[0], item[1], item[2])


if __name__ == "__main__":
    run_tests(TASK_3_DATA)
