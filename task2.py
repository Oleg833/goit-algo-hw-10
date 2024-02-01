import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def monte_carlo_integration(func, a, b, num_samples=10000):
    x_values = np.random.uniform(a, b, num_samples)
    fx_values = func(x_values)
    integral_approximation = np.mean(fx_values) * (b - a)
    return integral_approximation

def my_function(x):
    return x**2 + 3*x + 10

a = 1
b = 3

x_vals = np.linspace(a, b, 100)
y_vals = my_function(x_vals)

plt.plot(x_vals, y_vals, label='f(x) = x^2 + 3x + 10')
plt.fill_between(x_vals, y_vals, alpha=0.2, label='Площа під кривою')

plt.title('Графік функції та апроксимована площа під кривою')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(a, color='red', linestyle='--', label='a')
plt.axvline(b, color='blue', linestyle='--', label='b')
plt.legend()
plt.show()


def main():
    
    a = 1
    b = 3
    num_samples = 1000000
    result = monte_carlo_integration(my_function, a, b, num_samples)
    result2, error = spi.quad(my_function, a, b)

    print(f"Апроксимоване значення інтеграла: {result:.5f}")
    print(f"Інтеграл за 'spi.quad':  {result2:.5f}")

if __name__ == "__main__":
    main()