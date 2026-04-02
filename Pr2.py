import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf

def generate_time_series(n=200, phi=0.8, sigma=1.0):
    """
    n - довжина ряду
    phi - коефіцієнт автокореляції (0 < phi < 1)
    sigma - шум
    """
    series = np.zeros(n)
    noise = np.random.normal(0, sigma, n)

    for t in range(1, n):
        series[t] = phi * series[t-1] + noise[t]

    return series

generated_series = generate_time_series()

acf_values = acf(generated_series, nlags=20)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(generated_series)
plt.title("Згенерований часовий ряд")
plt.xlabel("Час")
plt.ylabel("Значення")

plt.subplot(1, 2, 2)
plt.stem(acf_values)
plt.title("Автокореляційна функція (ACF)")
plt.xlabel("Лаг")
plt.ylabel("Кореляція")

plt.tight_layout()
plt.show()

real_like_series = generate_time_series(phi=0.5)
acf_real = acf(real_like_series, nlags=20)

plt.figure(figsize=(6, 4))
plt.plot(acf_values, label="Згенерований (phi=0.8)")
plt.plot(acf_real, label="Інший ряд (phi=0.5)")
plt.legend()
plt.title("Порівняння ACF")
plt.xlabel("Лаг")
plt.ylabel("Кореляція")
plt.show()