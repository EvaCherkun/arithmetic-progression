def arithmetic_sum(n):
    """
    Обчислення суми перших n членів арифметичної прогресії.
    """
    if n <= 0:
        return 0
    a1 = 4  # перший член
    d = 3   # різниця
    an = a1 + (n - 1) * d
    return n * (a1 + an) // 2

if __name__ == "__main__":
    n = int(input("Введіть кількість членів прогресії: "))
    print(f"Сума перших {n} членів прогресії: {arithmetic_sum(n)}")
