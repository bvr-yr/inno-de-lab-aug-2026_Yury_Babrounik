import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeAlias

from consts import PERFORMANCE_LOG_PREFIX, TIME_DECIMALS
from test_data import TASK_2_DATA

# for convenient usage in multiple functions
RevenueData: TypeAlias = list[dict[str, str | float]]


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Measure function execution time (decorator).

    Args:
        func: Function to measure.

    Returns:
        A wrapper of original function that also prints function
        name and execution time before returning its result.

    """

    # to preserve wrapped func metadata like name, docstring and annotations
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:  # noqa: ANN401
        now = time.perf_counter()
        result = func(*args, **kwargs)
        # capture time spent right after function execution
        elapsed = time.perf_counter() - now
        # https://docs.astral.sh/ty/reference/typing-faq/#why-does-ty-say-callable-has-no-attribute-__name__
        func_name = getattr(func, "__name__", "<func_name>")
        print(
            f"{PERFORMANCE_LOG_PREFIX} Function {func_name!r} took "
            f"{elapsed:.{TIME_DECIMALS}f} seconds.",
        )
        return result

    return wrapper


@performance_logger
def get_sorted_report(data: RevenueData) -> RevenueData:
    """Sort revenue report.

    Args:
        data: Unsorted list of categories and sales values.

    Returns:
        List of categories sorted by 'total_sales' in descending order.

    """
    return sorted(data, key=lambda item: item["total_sales"], reverse=True)


def print_sorted_report(data: RevenueData) -> None:
    """Print sorted revenue report.

    Args:
        data: Unsorted list of categories and sales values.

    """
    sorted_report = get_sorted_report(data)

    print("Top categories by revenue:")
    for i, item in enumerate(sorted_report, start=1):
        print(f"{i}. {item['category']}: {item['total_sales']}")


def run_tests(data: tuple[RevenueData, ...]) -> None:
    """Run tests with provided data.

    Args:
        data: Test data provided by task condition.

    """
    print("=== PERFORMANCE TEST ===")
    for i, test in enumerate(data, start=1):
        print(f"\n\n--- TEST {i} ---")
        print_sorted_report(test)


if __name__ == "__main__":
    run_tests(TASK_2_DATA)
