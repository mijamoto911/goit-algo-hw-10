import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

result, error = spi.quad(f, a, b)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Graph f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()
print("Integral (method quad): ", result)

def monte_carlo_integration(f, a, b, n):
    x = np.random.uniform(a, b, n)
    y = f(x)
    area = np.mean(y) * (b - a)
    return area

n_mc = 10000

result_mc = monte_carlo_integration(f, a, b, n_mc)

print("Integral (method Monte-Carlo): ", result_mc)
