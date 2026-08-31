from consts import MAX_RENTAL_BATCH_LIMIT
from test_data import TASK_1_DATA


def calculate_rental_batch(
    quantity: int,
    rental_rate: float,
    discount: float = 0.0,
) -> tuple[float, bool]:
    """Calculate final rental amount and check batch limit.

    Args:
        quantity: Number of rented items.
        rental_rate: Price of one rented item.
        discount: Discount represented as decimal fraction.

    Returns:
        Tuple with final amount rounded and True if batch limit is exceeded.

    """
    final_sum = quantity * rental_rate * (1 - discount)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return round(final_sum, 2), is_limit_exceeded


def print_rental_batch(data: list[tuple[str, int, float, float]]) -> None:
    """Print rental batch report.

    Args:
        data: Test data provided by task condition.

    """
    print("=== RENTAL BATCH REPORT ===")

    # keep just indexing here, cause tuple is fixed and unpacking adds noise
    for i, batch in enumerate(data, start=1):
        title = batch[0]
        # to show named vs positional args usage
        match i:
            case 0:
                final_sum, is_limit_exceeded = calculate_rental_batch(
                    quantity=batch[1],
                    rental_rate=batch[2],
                    discount=batch[3],
                )
            case _:
                final_sum, is_limit_exceeded = calculate_rental_batch(
                    batch[1],
                    batch[2],
                    batch[3],
                )

        print(
            f"Batch {i} ({title}): "
            f"Amount: {final_sum}$. Limit exceeded: {is_limit_exceeded}",
        )


if __name__ == "__main__":
    print_rental_batch(TASK_1_DATA)
