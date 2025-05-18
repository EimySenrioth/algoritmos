import pandas as pd
import time
import math
import matplotlib.pyplot as plt

# Lista donde se almacenarán los datos de cada prueba
def prime_tester(n, mode="sqrt"):
    a = []
    t = 2
    while True:
        if mode == "sqrt":
            stop_condition = t > math.floor(math.sqrt(n))
        elif mode == "n_minus_1":
            stop_condition = t == n - 1 or n % t == 0
        elif mode == "n_div_2":
            stop_condition = t == n // 2 or n % t == 0
        else:
            raise ValueError("Modo inválido. Usa: 'sqrt', 'n_minus_1' o 'n_div_2'.")

        if mode == "sqrt":
            a.append([t, "T" if n % t == 0 else "F", "T" if t == math.floor(math.sqrt(n)) else "F", "---"])
        elif mode == "n_minus_1":
            a.append([t, "T" if n % t == 0 else "F", "T" if t == n - 1 else "F", "---"])
        elif mode == "n_div_2":
            a.append([t, "T" if n % t == 0 else "F", "T" if t == n // 2 else "F", "---"])

        if n % t == 0:
            a[-1][3] = f"{t} is a proper divisor of {n}"
            break
        elif stop_condition:
            a[-1][3] = f"{n} is prime"
            break
        t += 1

    return a


def run_test_cases():
    test_numbers = [13, 641, 997]
    mode_map = {
        "sqrt": "sqrt_n",
        "n_minus_1": "n_minus_1",
        "n_div_2": "n_div_2"
    }

    for n in test_numbers:
        for mode in mode_map:
            start_time = time.time()
            prime_tester(n, mode)
            elapsed_time = time.time() - start_time
            print(f"n={n}, modo={mode_map[mode]}, tiempo={elapsed_time:.6f} s")


# Ejecutar pruebas automáticamente
run_test_cases()
