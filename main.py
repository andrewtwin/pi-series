from decimal import Decimal


def gl():
    # Gregory–Leibniz series
    term = Decimal(0)
    numerator = Decimal(4)
    denominator = Decimal(1)

    while True:
        term = numerator / denominator
        yield term
        denominator += 2


def nil():
    # Nilakantha series
    term = Decimal(0)
    numerator = Decimal(4)
    d1 = 2
    d2 = 3
    d3 = 4
    denominator = Decimal(0)

    while True:
        denominator = d1 * d2 * d3
        term = numerator / denominator
        yield term
        d1 += 2
        d2 += 2
        d3 += 2


def main(sequence_length, series):
    if series == "gl":
        pi = Decimal(0)
        terms = gl()
        term = Decimal(0)
    elif series == "nil":
        pi = Decimal(3)
        terms = nil()
        term = Decimal(0)

    print(f"Running series {series} to {sequence_length:,}")
    print(f"Starting value {pi}")

    operator = ""
    i = 0

    while i < sequence_length:
        term = next(terms)
        if i % 2 == 0:
            operator = "+"
            pi += term
        else:
            operator = "-"
            pi -= term

        i += 1

        print(f"{i} {pi} {operator}{term}")


if __name__ == "__main__":
    sequence_length = 1_000_000
    series = "gl"
    main(sequence_length, series)
