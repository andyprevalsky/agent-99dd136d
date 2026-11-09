"""Compute and print the Collatz sequence starting at 27."""


def collatz(n: int) -> tuple[list[int], int]:
    """Return the Collatz sequence from n down to 1 and its transition count."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
        steps += 1
    return sequence, steps


def main() -> None:
    sequence, step_count = collatz(27)
    for value in sequence:
        print(value)
    print(f"Total steps: {step_count}")


if __name__ == "__main__":
    main()
